from typing import List, Optional
from pydantic import BaseModel


class BannerBase(BaseModel):
    title: str
    description: str
    url: str
    published: bool
    is_widget: bool


class Banner(BannerBase):
    class Config():
        orm_mode = True


class Bannero(BannerBase):
    id: int
    priority: int

    class Config():
        orm_mode = True


class Temp(BaseModel):
    title: str
    description: str
    url: str
    url_image: str

    class Config():
        orm_mode = True
