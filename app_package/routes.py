from flask import render_template, url_for, flash, redirect
from app_package import app
from app_package.forms import TagManagerForm
from app_package import db
from app_package.db_models import Article, Tag, ArticleTag, ArticleAction, ArticleKeyword
from app_package.scraper import Scraper
import sys



@app.route('/')
@app.route('/home')
def home():
    articles = [article.__dict__ for article in Article.query.order_by(Article.time_shown.desc()).all()]
    return render_template('home.html', articles=articles)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/tag-manager', methods=['GET', 'POST'])
def tag_manager():
    old_confirmed_tags = [tag.text for tag in Tag.query.filter_by(is_confirmed=True).all()]

    tag_manager_form = TagManagerForm()
    # set the preselected to the currently confirmed tags:
    # note that this accepts a list of tuples: (value, label)
    tag_manager_form.tag_input.choices = [(tag, tag) for tag in old_confirmed_tags]

    if tag_manager_form.submit.data: # User presses Update
        new_confirmed_tags = tag_manager_form.tag_input.data

        if len(new_confirmed_tags)>0:
            Tag.query.filter_by(is_confirmed=True).delete() 
            # remove all confirmed tags and add again:
            for chosen_tag_text in new_confirmed_tags:
                db.session.add(Tag(text=chosen_tag_text, is_confirmed=True))
                db.session.commit()
            
            flash('Your interest tags were successfully updated!', 'success')
            return redirect(url_for('home'))
        
        else:
            flash('Please enter at least one tag!', 'danger')

    return render_template('tag_manager.html', title='Tag Manager', form=tag_manager_form)
