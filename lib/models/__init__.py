from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .student_models import Base, Student, Task

engine = create_engine("sqlite:///lib/students.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


