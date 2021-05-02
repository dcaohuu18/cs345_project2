from app_package import db


class Tag(db.Model):
    tag_text = db.Column(db.String(500), primary_key=True)
    tag_status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Tag('{self.tag_text}', '{self.tag_status}')"


class Article(db.Model):
    article_url = db.Column(db.String(2048), primary_key=True)
    article_source = db.Column(db.String(500))
    article_title = db.Column(db.String(200), nullable=False)
    article_date = db.Column(db.DateTime)
    article_content = db.Column(db.Text, nullable=False)
    article_thumbnail_url = db.Column(db.String(2048), default="default_thumbnail.jpeg")
    # foreign key:
    # other table references:
    # col = db.relationship('other_table', backref='other_table_col', lazy=True)

    # references other table:
    # col = db.Column(db.type, db.ForeignKey('other_table.col'))

    def __repr__(self):
        return f"Article('{self.article_title}', '{self.article_date}')"
