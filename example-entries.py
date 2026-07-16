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
