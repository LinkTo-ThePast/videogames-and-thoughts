from fastapi import FastAPI
from models.diary_entry import DiaryEntry


entry_example = DiaryEntry(
    author="Wicho",
    title="Rebeldía",
    content="Aquellos que se revelan ante las injusticas del mundo...",
    published_date="02/agosto/2026",
    videogame_title="Persona 5 Royal",
    platform="PS5",    
    )

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
def get_entries() -> DiaryEntry:
    return entry_example._from_object_to_json()


@app.post("/api/v1/diary-entries/")
def adding_diary_entry(diary_entry: DiaryEntry) -> DiaryEntry:
    return diary_entry
    