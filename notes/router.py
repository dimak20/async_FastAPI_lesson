from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from . import crud, schemas


router = APIRouter()


@router.get("/notes/", response_model=list[schemas.Note])
async def read_cheese_types(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_notes(db=db)


@router.post("/notes/", response_model=schemas.Note)
async def read_cheese_types(
    note: schemas.NoteIn,
    db: AsyncSession = Depends(get_db),
):
    return await crud.create_note(db=db, note=note)
