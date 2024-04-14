import argparse
import sys

from conf.db import session
from conf.db_models import Group, Student, Teacher, Subject, Grade


def create_record(args):
    if args.model == "Teacher":
        record = Teacher(teacher_name=args.name)
    elif args.model == "Group":
        record = Group(group_name=args.name)
    elif args.model == "Student":
        record = Student(student_name=args.name)
    elif argsmodel == "Subject":
        record = Subject(subject_name=args.name)
    elif args.model == "Grade":
        record = Grade(grade=args.name)
    else:
        return "Invalid model specified."
    session.add(record)
    session.commit()
    return f"{args.model} created successfully."

def list_records(args):
    if args.model == "Teacher":
        records = session.query(Teacher).all()
    elif args.model == "Group":
        records = session.query(Group).all()
    elif args.model == "Student":
        records = session.query(Student).all()
    elif args.model == "Subject":
        records = session.query(Subject).all()
    elif args.model == "Grade":
        records = session.query(Grade).all()
    else:
        return "Invalid model specified."
    for record in records:
        print(record)

def update_record(args):
    if args.model == "Teacher":
        record = session.query(Teacher).filter_by(teacher_id=args.idx).first()
        record.teacher_name = args.name
    elif args.model == "Group":
        record = session.query(Group).filter_by(group_id=args.idx).first()
        record.group_name = args.name
    elif args.model == "Student":
        record = session.query(Student).filter_by(student_id=args.idx).first()
        record.student_name = args.name
    elif args.model == "Subject":
        record = session.query(Subject).filter_by(subject_id=args.idx).first()
        record.subject_name = args.name
    elif args.model == "Grade":
        record = session.query(Grade).filter_by(grade_id=args.idx).first()
        record.grade = args.name
    else:
        return "Invalid model specified."
    session.commit()
    return f"{args.model} updated successfully."


def remove_record(args):
    if args.model == "Teacher":
        record = session.query(Teacher).filter_by(teacher_id=args.idx).first()
    elif args.model == "Group":
        record = session.query(Group).filter_by(group_id=args.idx).first()
    elif args.model == "Student":
        record = session.query(Student).filter_by(student_id=args.idx).first()
    elif args.model == "Subject":
        record = session.query(Subject).filter_by(subject_id=args.idx).first()
    elif args.model == "Grade":
        record = session.query(Grade).filter_by(group_id=args.idx).first()
    else:
        return "Invalid model specified."

    if record:
        session.delete(record)
        session.commit()
        return f"{args.model} deleted successfully."

def main():
    parser = argparse.ArgumentParser(description="CLI program for CRUD operations with the database")
    parser.add_argument("--action", "-a", choices=["create", "list", "update", "remove"], required=True, help="Action to perform")
    parser.add_argument("--model", "-m", choices=["Group", "Student", "Teacher", "Subject", "Grade"], required=True, help="Model to operate on")
    parser.add_argument("--id", type=int, help="ID of the record to update or remove")
    parser.add_argument("--name", "-n", nargs="+", help="Name of the record to create or update")
    args = parser.parse_args()

    if args.action == "create":
        create_record(args)
    elif args.action == "list":
        list_records(args)
    elif args.action == "update":
        update_record(args)
    elif args.action == "remove":
        remove_record(args)

if __name__ == "__main__":
    main()
