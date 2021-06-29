from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base
from sqlalchemy_utils import URLType
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.orm import relationship


class Banner(Base):
    __tablename__ = 'banners'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    url_image = Column(URLType, default="/media/doggo.jpg")
    published = Column(Boolean, default=True)
    is_widget = Column(Boolean, default=True)
    priority = Column(Integer)
