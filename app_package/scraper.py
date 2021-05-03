from newsapi import NewsApiClient
from app_package import db
from app_package.db_models import Tag, Article
from datetime import datetime
our_api_key = "1683bb4b024944fd8d1337224874b754"

class Scraper():
    '''
    Reads tags from the tag table, and then writes articles that the news API gives to the article table.
    '''

    def __init__(self):
        self.newsapi = NewsApiClient(api_key=our_api_key)

    def get_article_raw(self, tags):
        article_collection = {}
        for tag in tags:
            article_collection[tag]=self.newsapi.get_everything(q=tag.tag_text)["articles"]
        return article_collection


    def get_tags(self):
        return Tag.query.filter_by(tag_status="On").all()

    def write_articles(self, article_collection):
        for tag in article_collection.keys():
            for article in article_collection[tag]:
                if len(Article.query.filter_by(article_url=article["url"]).all())>0:
                    Article.query.filter_by(article_url=article["url"]).delete()
                url = article["url"]
                source = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description  = article["description"]
                thumbnail_url  = article["urlToImage"]
                publish_date =  datetime.strptime(article["publishedAt"], '%Y-%m-%dT%H:%M:%SZ')
                content_length = len(article["content"])
                #200 is the max length the content section can have. Other characters are left in a "... [+num chars]"" section at the end.
                if content_length >200:
                    chars_num = int(article["content"][203:-7])+200 #num of chars is listed from the 203'rd character, and is followed by _chars] (_ is a space). This works for all articles over 200 chars long.
                else:
                    chars_num = content_length
                db.session.add(Article(article_url=url, article_source=source, article_title=title, article_date=publish_date, article_content=description, article_thumbnail_url=thumbnail_url))
                db.session.commit()

    def main(self):
        active_tags = self.get_tags()
        articles_with_tags = self.get_article_raw(active_tags)
        self.write_articles(articles_with_tags)
