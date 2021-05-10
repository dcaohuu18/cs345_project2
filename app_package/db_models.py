from app_package import db
from datetime import datetime


class Article(db.Model):
    url = db.Column(db.String(2048), primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(70))
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(1000))
    thumbnail_url = db.Column(db.String(2048), nullable=False, default="/static/default_thumbnail.jpg")
    publish_date = db.Column(db.DateTime)
    chars_num = db.Column(db.Integer)
    is_fake_news = db.Column(db.Boolean, default=False)
    time_shown = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # referenced by other tables:
    articleTags = db.relationship('ArticleTag', backref='ArticleTag_article', lazy=True)
    articleKeywords = db.relationship('ArticleKeyword', backref='ArticleKeyword_article', lazy=True)
    articleActions = db.relationship('ArticleAction', backref='ArticleAction_article', lazy=True)

    def __repr__(self):
        return f"Article({self.url})"
    

class Tag(db.Model):
    text = db.Column(db.String(500), primary_key=True)
    is_confirmed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Tag('{self.text}', {'confirmed' if self.is_confirmed else 'potential'})"


class ArticleTag(db.Model):
    # references Article and Tag:
    article_url = db.Column(db.String(2048), db.ForeignKey('article.url'), primary_key=True)
    tag_text = db.Column(db.String(500), db.ForeignKey('tag.text'), primary_key=True)

    def __repr__(self):
        return f"ArticleTag(article_url: {self.article_url}, tag: '{self.tag_text}')"


class ArticleKeyword(db.Model):
    # references Article:
    article_url = db.Column(db.String(2048), db.ForeignKey('article.url'), primary_key=True)
    keyword = db.Column(db.String(200), primary_key=True)

    def __repr__(self):
        return f"ArticleKeyword(article_url: {self.article_url}, keyword: '{self.keyword}')"


class ArticleAction(db.Model):
    # references Article:
    article_url = db.Column(db.String(2048), db.ForeignKey('article.url'), primary_key=True)
    action = db.Column(db.String(100), primary_key=True)
    last_update_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return f"ArticleAction(article_url: {self.article_url}, action: {self.action})"
