from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
import datetime
from database.models import DBPost

def create (db: Session, request: PostBase):
    new_post = DBPost (
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
     )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

    