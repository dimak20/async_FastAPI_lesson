from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from . import schemas, crud
from .utils import PackagingType

router = APIRouter()


@router.get("/cheese_types/", response_model=list[schemas.CheeseType])
def read_cheese_types(db: Session = Depends(get_db)):
    return crud.get_all_cheese_types(db=db)


@router.post("/cheese_types/", response_model=schemas.CheeseType)
def create_cheese_type(
    cheese_type: schemas.CheeseTypeCreate,
    db: Session = Depends(get_db),
):
    db_cheese_type = crud.get_cheese_type_by_name(db=db, name=cheese_type.name)

    if db_cheese_type:
        raise HTTPException(
            status_code=400, detail="Such name for CheeseType already exists"
        )

    return crud.create_cheese_type(db=db, cheese_type=cheese_type)


@router.get("/cheese/", response_model=list[schemas.Cheese])
def read_cheese(
    packaging_type: PackagingType | None = None,
    cheese_type: str | None = None,
    db: Session = Depends(get_db),
):
    return crud.get_cheese_list(
        db=db, packaging_type=packaging_type, cheese_type=cheese_type
    )


@router.get("/cheese/{cheese_id}/", response_model=schemas.Cheese)
def read_single_cheese(cheese_id: int, db: Session = Depends(get_db)):
    db_cheese = crud.get_cheese(db=db, cheese_id=cheese_id)

    if db_cheese is None:
        raise HTTPException(status_code=404, detail="Cheese not found")

    return db_cheese


@router.post("/cheese/", response_model=schemas.Cheese)
def create_cheese(cheese: schemas.CheeseCreate, db: Session = Depends(get_db)):
    return crud.create_cheese(db=db, cheese=cheese)
