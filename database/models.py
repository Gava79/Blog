from.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean, Text
from sqlalchemy.orm import relationship

class DBPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title= Column(String)
    content = Column(String)
    creator = Column(String)
    timestamp = Column (String)


