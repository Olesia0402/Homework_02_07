import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.db_models import Group, Student, Teacher, Subject, Grade


fake = Faker('uk-UA')


def insert_data_for_groups():
    for _ in range(3):
        group = Group(group_name = fake.word())
        session.add(group)

def insert_data_for_teachers():
    for _ in range(5):
        teacher = Teacher(teacher_name = fake.name())
        session.add(teacher)

def insert_data_for_subjects():
    teachers = session.query(Teacher).all()

    for _ in range(8):
        subject = Subject(
            subject_name = fake.word(),
            teacher_id = random.choice(teachers).teacher_id
            )
        session.add(subject)

def insert_data_for_students():
    groups = session.query(Group).all()
    for _ in range(50):
        student = Student(
            student_name = fake.name(),
            group_id = random.choice(groups).group_id
        )
        session.add(student)
        
def insert_data_for_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for _ in range(100):
        gra = Grade(
            grade = random.randint(0, 100),
            grade_date = fake.date_this_decade(),
            student_id = random.choice(students).student_id,
            subject_id = random.choice(subjects).subject_id
            )
        session.add(gra)


if __name__ == '__main__':
    try:
        # insert_data_for_groups()
        # insert_data_for_teachers()
        # session.commit()
        # insert_data_for_subjects()
        # session.commit()
        # insert_data_for_students()
        # session.commit()
        insert_data_for_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()