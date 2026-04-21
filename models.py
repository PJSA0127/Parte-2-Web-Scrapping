from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

quote_tag_association = Table(
    'quote_tag',
    Base.metadata,
    Column('quote_id', Integer, ForeignKey('quotes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    quotes = relationship("Quote", back_populates="author")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    quotes = relationship("Quote", secondary=quote_tag_association, back_populates="quotes")

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    sentiment_score = Column(Float, nullable=True) # from -1.0 to 1.0
    sentiment_label = Column(String, nullable=True) # Positivo, Neutral, Negativo

    author = relationship("Author", back_populates="quotes")
    tags = relationship("Tag", secondary=quote_tag_association, back_populates="quotes")
