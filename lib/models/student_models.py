from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self):
        return f"{self.id}: {self.name}"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="tasks")

    def __repr__(self):
        return f"{self.id}: {self.description}"


