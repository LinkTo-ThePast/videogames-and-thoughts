from fastapi import FastAPI
from models.diary_entry import DiaryEntry

# let's define a class from which we can instantiate an object
class Entry:
    # constructor -> define properties and the self
    def __init__(self, author, date, videogame_title, text_entry):
        self.author = author
        self.date = date
        self.videogame_title = videogame_title
        self.text_entry = text_entry
    
    def from_object_to_json(self):
        return {
            "author": self.author,
            "published_date": self.date,
            "videogame_title": self.videogame_title,
            "text_entry": self.text_entry
        }

entry_example = Entry(author="Wicho", date="Yesterday", videogame_title="Persona 5 Royal", text_entry="Aquellos que se revelan y no aceptan la situacion actual.")

# initialize application
app = FastAPI()

# routing
@app.get("/")
def get_root():
    return {"ahh": "you're back!"}

@app.get("/health")
def status():
    return {"status": "ok"}

# route for getting a post or diary entry?
@app.get("/api/diary-entries/entry-1")
def get_entries():
    return entry_example.from_object_to_json()



@app.post("/api/v1/diary-entries/")
def adding_diary_entry(diary_entry: DiaryEntry) -> DiaryEntry:
    return diary_entry
    