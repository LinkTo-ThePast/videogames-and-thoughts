from datetime import datetime
from pydantic import BaseModel


class DiaryEntry(BaseModel):
    id: int
    author: str
    title: str
    content: str
    published_date: datetime
    videogame_title: str
    platform: str
    
