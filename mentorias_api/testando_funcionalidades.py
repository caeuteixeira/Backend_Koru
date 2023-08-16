from mentor import Mentor
from mentorando import Mentorando
from mentoria import Mentoria
from db_connector import DBConnector

db = DBConnector("mentorias.db")

print(Mentor.get_by_id(1, db.connect()).to_dict())
print(Mentor.get_all(db.connect))

print(Mentorando.get_by_id(1, db.connect()).to_dict())
print(Mentorando.get_all(db.connect))

print(Mentoria.get_by_id(1, db.connect()).to_dict())
print(Mentoria.get_all(db.connect))