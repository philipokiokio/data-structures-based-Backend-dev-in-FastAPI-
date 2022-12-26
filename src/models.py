from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from src.database import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String, unique=True)
    address = Column(String)
    phone=Column(String)
    posts = relationship("BlogPost", back_populates='user', cascade="all, delete")




class BlogPost(Base):
    __tablename__ = "blog_post"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    user = relationship("User")