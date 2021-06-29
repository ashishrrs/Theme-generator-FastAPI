from sqlalchemy.orm import Session
from typing import Optional
from fastapi import FastAPI, File, UploadFile
from starlette.background import BackgroundTasks

import shutil
from fastapi import HTTPException, status
import sys

sys.path.append('..')
import models, schemas


def get_all(sort: bool, db: Session):
    if sort:
        blogs = db.query(models.Banner).order_by(models.Banner.priority.asc()).all()
    else:
        blogs = db.query(models.Banner).order_by(models.Banner.priority.desc()).all()
    return blogs


def get_all_by_category(is_widget: bool, sort: bool, db: Session):
    if is_widget:
        if sort:
            blogs = db.query(models.Banner).filter(models.Banner.is_widget == True).order_by(
                models.Banner.priority.asc()).all()
        else:
            blogs = db.query(models.Banner).filter(models.Banner.is_widget == True).order_by(
                models.Banner.priority.desc()).all()
    else:
        if sort:
            blogs = db.query(models.Banner).filter(models.Banner.is_widget == False).order_by(
                models.Banner.priority.asc()).all()
        else:
            blogs = db.query(models.Banner).filter(models.Banner.is_widget == False).order_by(
                models.Banner.priority.desc()).all()
    return blogs


def create(request: schemas.Banner, db: Session):
    new_blog = models.Banner(title=request.title, description=request.description, url=request.url,
                             is_widget=request.is_widget, priority=1,
                             published=request.published)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    new_blog.priority = new_blog.id
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    banner = db.query(models.Banner).filter(models.Banner.id == id)

    if not banner.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    banner.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Banner, db: Session):
    upd_banner = db.query(models.Banner).filter(models.Banner.id == id)

    if not upd_banner.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    upd_banner.update({'title': request.title, 'description': request.description, 'url': request.url,
                       'is_widget': request.is_widget,
                       'published': request.published})
    db.commit()
    return 'updated'


def get_published(db: Session, published: bool, is_widget: bool):
    if published:
        if is_widget:
            blogs = db.query(models.Banner).filter(models.Banner.published == True).filter(
                models.Banner.is_widget == True).all()
        else:
            blogs = db.query(models.Banner).filter(models.Banner.published == True).filter(
                models.Banner.is_widget == False).all()

    else:
        if is_widget:
            blogs = db.query(models.Banner).filter(models.Banner.published == False).filter(
                models.Banner.is_widget == True).all()
        else:
            blogs = db.query(models.Banner).filter(models.Banner.published == False).filter(
                models.Banner.is_widget == False).all()

    return blogs


def swapper(id1: int, id2: int, is_widget1: bool, is_widget2: bool, db: Session):
    upd_banner = db.query(models.Banner).filter(models.Banner.id == id1)

    if not upd_banner.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id1} not found")
    upd_banner1 = db.query(models.Banner).filter(models.Banner.id == id2)
    if not upd_banner1.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id2} not found")
    if is_widget2 != is_widget1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Cannot swap widget with a non widget type banner")

    temp = upd_banner.first().priority
    upd_banner.first().priority = upd_banner1.first().priority
    upd_banner1.first().priority = temp
    db.commit()
    blogs = db.query(models.Banner).filter(models.Banner.is_widget == is_widget2).order_by(
        models.Banner.priority.asc()).all()

    return blogs


def img_up(id: int, db: Session, file: UploadFile = File(...)):
    new_url = db.query(models.Banner).filter(models.Banner.id == id)
    if not new_url.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    file.filename = str(str(id) + "_" + file.filename)
    with open("media/" + file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
    url = str("media/" + file.filename)
    # if "/media/doggo.jpg" != new_url.url_image:
    #     BackgroundTasks.add_task(remove_file,url)

    new_url.update({"url_image": url})
    db.commit()
    return 'updated'
