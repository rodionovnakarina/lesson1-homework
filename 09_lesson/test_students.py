import pytest
from sqlalchemy 
import 
create_engine, 
Column, Integer, 
String
from 
sqlalchemy.ext.declarative 
import 
declarative_base
from 
sqlalchemy.orm 
import 
sessionmaker

# Строка 
подключения к БД
DATABASE_URL = 
"postgresql://myuser:Mikhail130111@localhost:5432/mydatabase"

Base = 
declarative_base()

class 
Student(Base):
    __tablename__ 
= "students"
    id = 
Column(Integer, 
primary_key=True, 
autoincrement=True)
    name = 
Column(String, 
nullable=False)

# Создаем движок 
и сессию
engine = 
create_engine(DATABASE_URL)
Session = 
sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def session():
    
Base.metadata.create_all(engine) 
 # создаем 
таблицу
    s = Session()
    yield s
    s.close()
    
Base.metadata.drop_all(engine) 
 # удаляем 
таблицу после 
тестов

def 
test_add_student(session):
    student = 
Student(name="Ivan")
    
session.add(student)
    
session.commit()
    
    result = 
session.query(Student).filter_by(name="Ivan").first()
    assert result 
is not None
    assert 
result.name == 
"Ivan"

def 
test_update_student(session):
    student = 
session.query(Student).filter_by(name="Ivan").first()
    student.name 
= "Petr"
    
session.commit()
    
    result = 
session.query(Student).filter_by(name="Petr").first()
    assert result 
is not None
    assert 
result.name == 
"Petr"

def 
test_delete_student(session):
    student = 
session.query(Student).filter_by(name="Petr").first()
    
session.delete(student)
    
session.commit()
    
    result = 
session.query(Student).filter_by(name="Petr").first()
    assert result 
is None
"postgresql://myuser:Mikhail130111@localhost:5432/mydata# 
09_lesson/test_students.py

import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения к твоей БД
DATABASE_URL = 
"postgresql://myuser:Mikhail130111@localhost:5432/mydatabase"

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Создаем движок и сессию
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def session():
    Base.metadata.create_all(engine)  # создаем таблицу
    s = Session()
    yield s
    s.close()
    Base.metadata.drop_all(engine)  # удаляем таблицу после тестов

def test_add_student(session):
    student = Student(name="Ivan")
    session.add(student)
    session.commit()
    
    result = session.query(Student).filter_by(name="Ivan").first()
    assert result is not None
    assert result.name == "Ivan"

def test_update_student(session):
    student = session.query(Student).filter_by(name="Ivan").first()
    student.name = "Petr"
    session.commit()
    
    result = session.query(Student).filter_by(name="Petr").first()
    assert result is not None
    assert result.name == "Petr"

def test_delete_student(session):
    student = session.query(Student).filter_by(name="Petr").first()
    session.delete(student)
    session.commit()
    
    result = session.query(Student).filter_by(name="Petr").first()
    assert result is None

