from datetime import datetime
from pydantic import BaseModel


class DiaryEntry(BaseModel):
    id: int = 123
    author: str
    title: str
    content: str
    published_date: str
    videogame_title: str
    platform: str
    
    
    def _from_object_to_json(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "published_date": self.published_date,
            "videogame_title": self.videogame_title,
            "platform": self.title
        }
    
