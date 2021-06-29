from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi import FastAPI, File, UploadFile
import sqlalchemy.orm
import sys

sys.path.append('..')
import database, schemas
from repository import banner

router = APIRouter(
    prefix="/banner",
    tags=['Banners']
)

get_db = database.get_db


@router.get('/', response_model= List[schemas.Bannero])
def all(sort: Optional[bool] = True, db: sqlalchemy.orm.Session = Depends(get_db)):
    return banner.get_all(sort, db)


@router.get('/get_by_category')
def all(is_widget: bool, sort: Optional[bool] = True, db: sqlalchemy.orm.Session = Depends(get_db)):
    return banner.get_all_by_category(is_widget, sort, db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Bannero)
def create(request: schemas.Banner, db: sqlalchemy.orm.Session = Depends(get_db)):
    return banner.create(request, db)


@router.post('/upload image')
async def upload_image(id: int, db: sqlalchemy.orm.Session = Depends(get_db), image: UploadFile = File(...)):
    print(image.filename)
    return banner.img_up(id, db, image)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: sqlalchemy.orm.Session = Depends(get_db)):
    return banner.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Banner, db: sqlalchemy.orm.Session = Depends(get_db)):
    return banner.update(id, request, db)


@router.get('/published', )
def get_published(db: sqlalchemy.orm.Session = Depends(get_db), published: bool = True, is_widget: bool = True):
    return banner.get_published(db, published, is_widget)


@router.get('/position',response_model= List[schemas.Bannero])
def swapper(id1: int, id2: int, is_widget1: bool, is_widget2: bool, db: sqlalchemy.orm.Session = Depends(get_db)):
    return banner.swapper(id1, id2, is_widget1, is_widget2, db)
