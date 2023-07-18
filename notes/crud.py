from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


async def get_all_notes(db: AsyncSession):
    query = select(models.Note)
    notes_list = await db.execute(query)
    return [note[0] for note in notes_list.fetchall()]


async def create_note(db: AsyncSession, note: schemas.NoteIn):
    query = insert(models.Note).values(
        text=note.text,
        completed=note.completed,
    )
    result = await db.execute(query)
    await db.commit()
    resp = {**note.model_dump(), "id": result.lastrowid}
    return resp
