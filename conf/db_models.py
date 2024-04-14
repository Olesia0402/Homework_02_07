from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(100), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.group_id', ondelete='CASCADE', onupdate='CASCADE'))
    group = relationship('Group', backref='students')


class Teacher(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(100), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String(50), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.teacher_id', ondelete='CASCADE', onupdate='CASCADE'))
    teacher = relationship('Teacher', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    grade_id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    grade_date = Column('grade_date', Date, nullable=True)
    student_id = Column('student_id', ForeignKey('students.student_id', ondelete='CASCADE', onupdate='CASCADE'))
    subject_id = Column('subject_id', ForeignKey('subjects.subject_id', ondelete='CASCADE', onupdate='CASCADE'))
    student = relationship('Student', backref='grades')
    subject = relationship('Subject', backref='grade')