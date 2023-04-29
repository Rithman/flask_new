from sqlalchemy import Column, Table, Integer, ForeignKey

from blog.models.database import db


article_tag_assosiation_table = Table(
    "article_tag_assosiation",
    db.metadata,
    Column("article_id", Integer, ForeignKey("article.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tag.id"), nullable=False)
)