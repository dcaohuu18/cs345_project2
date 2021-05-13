from flask import render_template, url_for, flash, redirect, request
from app_package import app
from app_package.forms import TagManagerForm, DarkToggleForm
from app_package import db
from app_package.db_models import Article, Tag, ArticleTag, ArticleAction, ArticleKeyword, DisplayPref
from app_package.scraper import Scraper
from app_package.jinja_helper_funcs import reformat_datetime, base_url, est_read_time
from datetime import datetime, timedelta
from sqlalchemy import and_, or_, not_
import sys


jinja_helpers_map = {
    'reformat_datetime': reformat_datetime,
    'base_url': base_url,
    'est_read_time': est_read_time
}


def handle_dark_toggle(theme_obj, dark_toggle_form):
    # Preset the 'checked' property of the checkbox
    # This is just how the box is displayed: checked or unchecked
    # It's not related to the actual value: True or False
    if theme_obj.value=='dark.css':
        dark_toggle_form.is_dark.render_kw = {'checked': True}

    # When the form is submitted:
    # Update the value of theme in the DB based on the checkbox's status:
    if request.method=='POST' and request.form['form_name']=='dark_toggle_form':
        if dark_toggle_form.is_dark.data:
            theme_obj.value = 'dark.css'
        else:
            theme_obj.value = 'light.css'
            # override the 'checked' (display) property of the checkbox:
            # (for some reason, it renders to 'checked' even though the user just unchecked it)
            dark_toggle_form.is_dark.render_kw = {'checked': False}

    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home(): 
    # select only articles that have confirmed tags and were added in the last 3 days:
    articles = [a.__dict__ for a in db.session.query(Article
                                                    ).join(ArticleTag).join(Tag
                                                    ).filter(and_(Tag.is_confirmed==True,
                                                                  Article.time_added>datetime.now()-timedelta(days=3))
                                                    ).order_by(Article.time_added.desc()
                                                    ).all()]
    
    theme = DisplayPref.query.filter_by(attribute='theme').first()
    dark_toggle_form = DarkToggleForm()

    handle_dark_toggle(theme, dark_toggle_form)
    
    return render_template('home.html', articles=articles, theme=theme.value, 
                            dark_toggle_form=dark_toggle_form, **jinja_helpers_map)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/tag-manager', methods=['GET', 'POST'])
def tag_manager():
    # ------------------------
    # HANDLE TAG INPUT FORM:
    old_confirmed_tags = {tag.text for tag in Tag.query.filter_by(is_confirmed=True).all()}

    tag_manager_form = TagManagerForm()
    # set the preselected to the currently confirmed tags:
    # note that this accepts a list of tuples: (value, label)
    tag_manager_form.tag_input.choices = [(tag, tag) for tag in old_confirmed_tags]

    if request.method=='POST' and request.form['form_name']=='tag_manager_form':
        new_confirmed_tags = set(tag_manager_form.tag_input.data)

        if len(new_confirmed_tags)>0:
            removed_tags = old_confirmed_tags.difference(new_confirmed_tags)
            # Delete removed_tags from ArticleTag and Tag:
            db.session.query(ArticleTag).filter(ArticleTag.tag_text.in_(removed_tags)).delete()
            db.session.query(Tag).filter(Tag.text.in_(removed_tags)).delete()

            added_tags = new_confirmed_tags.difference(old_confirmed_tags)
            # Insert added_tags to Tag:
            for add_tag_text in added_tags:
                db.session.add(Tag(text=add_tag_text, is_confirmed=True))
            
            db.session.commit()

            if added_tags: # is not empty
                Scraper().run() # scrape new articles based on the new confirmed tags
            flash('Your interest tags were successfully updated!', 'success')
            
            return redirect(url_for('home'))
        
        else:
            flash('Please enter at least one tag!', 'danger')

    # ------------------------
    # HANDLE DARK THEME TOGGLE:
    theme = DisplayPref.query.filter_by(attribute='theme').first()
    dark_toggle_form = DarkToggleForm()

    handle_dark_toggle(theme, dark_toggle_form)

    return render_template('tag_manager.html', title='Tag Manager', theme=theme.value, 
                            dark_toggle_form=dark_toggle_form, tag_manager_form=tag_manager_form, 
                            **jinja_helpers_map)

