from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Audio(db.Model):
    id: int = db.Column(db.Integer, primary_key=True,auto_generate=True)
    name: str = db.Column(db.String(255))
    bpm: float = db.Column(db.Float)
    file_path: str = db.Column(db.String(255))
    length: int = db.Column(db.Integer)

    def __init__(self, name, bpm, file_path, length):
        self.name = name
        self.bpm = bpm
        self.file_path = "filepath/id"
        self.length = 10000

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_bpm(self) -> float:
        return self.bpm

    def set_bpm(self, bpm: float) -> None:
        self.bpm = bpm

    def get_length(self) -> float:
        return self.length



