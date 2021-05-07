from flask import render_template, url_for, flash, redirect
from app_package import app
from app_package.forms import TagManagerForm
from app_package.db_models import Article, Tag, ArticleTag, ArticleAction, ArticleKeyword
from app_package.scraper import Scraper

boxes = [
    {
        'source': 'New York Times',
        'title': 'News Box 1',
        'content': 'Dummy dummy news',
        'thumbnail_url': 'http://i3.ytimg.com/vi/snAhsXyO3Ck/maxresdefault.jpg',
        'date': 'April 23, 2021'
    },
    {
        'source': 'Washington Post',
        'title': 'News Box 2',
        'content': 'Bezos Bezos news',
        'thumbnail_url': '/static/default_thumbnail.jpg',
        'date': 'April 22, 2021'
    }
]

'''
def set_up_boxes():
    article_info_list=[]
    for story in Article.query.all():
        article_info = {
            "source" : story.source,
            "title" : story.title,
            "content" : story.description,
            "thumbnail_url" : story.thumbnail_url,
            "date" : story.publish_date
        }
        article_info_list.append(article_info)
    return article_info_list

news_scraper = Scraper()
news_scraper.main()

boxes = set_up_boxes()
'''

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', boxes=boxes)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/tag-manager', methods=['GET', 'POST'])
def tag_manager():
    tag_manager_form = TagManagerForm()
    if tag_manager_form.validate_on_submit():
        flash('Your interest tags were successfully updated!', 'success')
        return redirect(url_for('home')) # redirect to home
    return render_template('tag_manager.html',
                            title='Tag Manager',
                            form=tag_manager_form)
