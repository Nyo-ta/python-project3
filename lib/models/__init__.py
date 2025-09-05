from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student_models import Base, Student, Task

engine = create_engine("sqlite:///students.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


