from sqlalchemy import func, desc, select

from conf.db import session
from conf.db_models import Group, Student, Teacher, Subject, Grade


def select_1():
    result = session.query(Student.student_id, Student.student_name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.student_id).order_by(desc('average_grade')).limit(5).all()
    return result

def select_2():
    result = session.query(Student.student_id, Student.student_name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).filter(Grade.subject_id == 3).group_by(Student.student_id).order_by(desc('average_grade')).limit(1).all()
    return result

def select_3():
    result = (session.query(Group.group_name, Subject.subject_name, func.round(func.avg(Grade.grade), 2).label('average_grade'))) \
    .select_from(Student) \
    .join(Grade, Grade.student_id == Student.student_id) \
    .join(Subject, Grade.subject_id == Subject.subject_id) \
    .join(Group, Student.group_id == Group.group_id) \
    .group_by(Group.group_name, Subject.subject_name) \
    .order_by(func.avg(Grade.grade).desc()).all()
    return result

def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).all()
    return result

def select_5():
    result = session.query(Subject.subject_id, Subject.subject_name, Subject.teacher_id, Teacher.teacher_name) \
        .select_from(Subject).join(Teacher, Subject.teacher_id == Teacher.teacher_id).filter(Subject.teacher_id == 4).all()
    return result

def select_6():
    result = session.query(Student.student_id, Student.student_name, Student.group_id, Group.group_name) \
        .select_from(Student).join(Group, Student.group_id == Group.group_id).filter(Student.group_id == 2).all()
    return result

def select_7():
    result = session.query(Student.student_name, Group.group_name, Grade.grade) \
        .select_from(Grade) \
        .join(Student) \
        .join(Group) \
        .filter(Group.group_id == 2) \
        .filter(Grade.subject_id == 6).all()
    return result

def select_8():
    result = (session.query(Teacher.teacher_name, func.round(func.avg(Grade.grade), 2).label('average_grade')))\
        .select_from(Teacher)\
        .join(Subject, Subject.teacher_id == Teacher.teacher_id)\
        .join(Grade, Subject.subject_id == Grade.subject_id)\
        .group_by(Subject.teacher_id, Teacher.teacher_name)\
        .order_by(func.avg(Grade.grade)).all()
    return result

def select_9():
    result = session.query(Student.student_name, Student.group_id, Group.group_name, Subject.subject_name)\
        .select_from(Student)\
        .join(Grade, Student.student_id == Grade.student_id)\
        .join(Subject, Subject.subject_id == Grade.subject_id)\
        .join(Group, Student.group_id == Group.group_id)\
        .filter(Student.student_id == 13).all()
    return result

def select_10():
    result = session.query(Student.student_name, Teacher.teacher_name, Subject.subject_name)\
        .select_from(Student)\
        .join(Grade, Student.student_id == Grade.student_id)\
        .join(Subject, Subject.subject_id == Grade.subject_id)\
        .join(Group, Student.group_id == Group.group_id)\
        .join(Teacher, Subject.teacher_id == Teacher.teacher_id)\
        .filter(Student.student_id == 13).filter(Teacher.teacher_id == 1).all()
    return result

def select_11():
    result = (session.query(Teacher.teacher_name, Student.student_name, func.round(func.avg(Grade.grade), 2).label('average_grade')))\
        .select_from(Teacher)\
        .join(Subject, Subject.teacher_id == Teacher.teacher_id)\
        .join(Grade, Subject.subject_id == Grade.subject_id)\
        .join(Student, Grade.student_id == Student.student_id)\
        .filter(Student.student_id == 30).filter(Teacher.teacher_id == 2)\
        .group_by(Teacher.teacher_name, Student.student_name)\
        .order_by(func.avg(Grade.grade)).all()
    return result

def select_12():
    result = session.query(Student.student_name, Group.group_name, Subject.subject_name, Grade.grade, Grade.grade_date)\
        .select_from(Student)\
        .join(Group, Group.group_id == Student.group_id)\
        .join(Grade, Student.student_id == Grade.student_id)\
        .join(Subject, Grade.subject_id == Subject.subject_id)\
        .filter(Group.group_id == 1).filter(Subject.subject_id == 2)\
        .order_by(desc(Grade.grade_date)).all()
    return result


if __name__ == '__main__':
    # print(select_1())
    # print(select_2())
    # print(select_3())
    # print(select_4())
    # print(select_5())
    # print(select_6())
    # print(select_7())
    # print(select_8())
    # print(select_9())
    # print(select_10())
    # print(select_11())
    print(select_12())
