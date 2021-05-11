from newsapi import NewsApiClient
from app_package import db
from app_package.db_models import Tag, Article, ArticleTag#, ArticleKeyword
from datetime import datetime
our_api_key = "1683bb4b024944fd8d1337224874b754"

class Scraper():
    '''
    Reads tags from the tag table, and then writes articles that the news API gives to the article table.
    '''

    def __init__(self):
        self.newsapi = NewsApiClient(api_key=our_api_key)
        #100 is maximum. Controls how many articles the API fetches per query.
        self.page_size = 20

    def get_article_raw(self, tags):
        article_collection = {}
        #provides default articles from top headlines if no active tags
        if len(tags)==0:
            article_collection["Top"]=self.get_top_empty()
        for tag in tags:
            num_of_stories, top_stories = self.get_top_tagged(tag.text)
            #if there aren't enough top stories for the active tag, supplement with grabbing from all articles
            if num_of_stories<self.page_size:
                article_collection[tag]=self.newsapi.get_everything(q=tag.text, page_size=self.page_size)["articles"]+top_stories
            else:
                article_collection[tag]=top_stories
        return article_collection

    def get_top_tagged(self, tag):
        query_result = self.newsapi.get_top_headlines(q=tag, page_size=self.page_size)
        return query_result["totalResults"], query_result["articles"]

    def get_top_empty(self):
        return self.newsapi.get_top_headlines(page_size=self.page_size)["articles"]

    def get_tags(self):
        return Tag.query.filter_by(is_confirmed=True).all()

    # TODO: This function will eventually be used to generate keywords from the article, but as that requires a new API, will not be complete for a bit.
    def get_keywords(self):
        pass

    def write_articles(self, article_collection):
        for tag in article_collection.keys():
            for article in article_collection[tag]:
                #Handles articles that are already in the DB. This implementation updates rather than skips over
                if len(Article.query.filter_by(url=article["url"]).all())>0:
                    Article.query.filter_by(url=article["url"]).delete()
                #Some articles don't have a text preview, so this is used to provide one, and prevent content_length from throwing an error.
                if article["content"]==None:
                    article["content"]="No Preview Available"
                fetched_url = article["url"]
                fetched_source = article["source"]["name"]
                fetched_author = article["author"]
                fetched_title = article["title"]
                fetched_description  = article["description"]
                fetched_thumbnail_url  = article["urlToImage"]
                fetched_publish_date =  datetime.strptime(article["publishedAt"], '%Y-%m-%dT%H:%M:%SZ')
                content_length = len(article["content"])
                #200 is the max length the content section can have. Other characters are left in a "... [+num chars]"" section at the end.
                if content_length >200:
                    fetched_chars_num = int(article["content"][203:-7])+200 #num of chars is listed from the 203'rd character, and is followed by _chars] (_ is a space). This works for all articles over 200 chars long.
                else:
                    fetched_chars_num = content_length
                db.session.add(Article(url=fetched_url, source=fetched_source, title=fetched_title, description=fetched_description, thumbnail_url=fetched_thumbnail_url, publish_date=fetched_publish_date, chars_num=fetched_chars_num))
                #Handles article/tag pairs that are already in the DB. The values are the same, so no need to update.
                if len(ArticleTag.query.filter_by(article_url=fetched_url, tag_text=tag.text).all())>0:
                    pass
                else:
                    db.session.add(ArticleTag(article_url=fetched_url, tag_text=tag.text))
                db.session.commit()

    def run(self):
        active_tags = self.get_tags()
        articles_with_tags = self.get_article_raw(active_tags)
        self.write_articles(articles_with_tags)
