from mentor import Mentor
from mentorando import Mentorando
import sqlite3

class Mentoria:
    def __init__(self, mentor:Mentor, mentorando:Mentorando, data:str, id=None):
        self.id = id
        self.mentor = mentor
        self.mentorando = mentorando
        self.data = data

    def to_dict(self):
        return{
            "id": self.id,
            "id_mentor": self.mentor.id,
            "mentor": self.mentor.to_dict(),
            "id_mentorando": self.mentorando.id,
            "mentorando": self.mentorando.to_dict(),
            "data": self.data
        }
    
    def save(self, db_connection:sqlite3.Connection):
        if self.id is None:
            query = "INSERT INTO mentorias (id_mentor, id_mentorando, data_mentoria) VALUES (?, ?, ?)"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.mentor.id, self.mentorando.id, self.data))
            self.id = cursor.lastrowid
        else:
            query = "UPDATE mentorias SET nome_mentor=?, id_mentorando=?, data_mentoria=? WHERE id_mentorias=?"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.mentor.id, self.mentorando.id, self.data, self.id))
        db_connection.commit()

    def delete(self, db:sqlite3.Connection):
        query = "DELETE FROM mentorias WHERE id_mentoria=?"
        cursor = db.cursor()
        cursor.execute(query, (self.id, ))
        db.commit()

@staticmethod
def get_by_id(id:int, db:sqlite3.Connection):
    query = "SELECT * FROM mentorias WHERE id_mentoria=?"
    cursor = db.cursor()
    result = cursor.execute(query, (id, )).fetchone()
    if result:
        mentor = Mentor.get_by_id(result[1], db)
        mentorando = Mentorando.get_by_id(result[2], db)
        return Mentoria(id=result[0], mentor=mentor, mentorando=mentorando, data=result[3])
    else:
        return None
    
@staticmethod
def get_all(db:sqlite3.Connection):
    query = "SELECT * FROM mentorias"
    cursor = db.cursor()
    results = cursor.execute(query).fetchall()
    mentorias = []
    for result in results:
        mentor = Mentor.get_by_id(result[1], db)
        mentorando = Mentorando.get_by_id(result[2], db)
        mentorias.append(Mentoria(id=result[0], mentor=mentor, mentorando=mentorando, data=result[3]).to_dict)
        return mentorias