import sys
from random import choice, randint
from sqlalchemy import create_engine, distinct
from sqlalchemy.orm import sessionmaker
from models import Employee, GenderEnum
from datetime import datetime, timedelta
from config import *


engine = create_engine(SQL_BASE)
session_factory = sessionmaker(bind=engine)


def create_table():
    with session_factory() as session:
        Employee.metadata.create_all(engine)
        session.commit()
        print("The table has been created!")


def insert_data(full_name, birth_date, gender):
    to_datetime = datetime.strptime(birth_date, '%Y-%m-%d')
    birth_date = to_datetime.date()

    with session_factory() as session:
        employee = Employee(
            full_name=full_name,
            birth_date=birth_date,
            gender=gender
        )
        employee.save_to_db(session)


def employes_list():
    with session_factory() as session:
        unique_employes = session.query(
            Employee.full_name,
            Employee.birth_date,
            Employee.gender).distinct(Employee.full_name,
                                      Employee.birth_date).order_by(Employee.full_name).all()
        for full_name, birth_date, gender in unique_employes:
            employee = Employee(full_name=full_name,
                                birth_date=birth_date,
                                gender=gender)
            print(
                f"Full name: {full_name}, \
                Birth date: {birth_date}, \
                Gender: {gender}, \
                Age: {employee.calculate_age()}")


def generate_date(start, end):
    delta = end - start
    random_days = randint(0, delta.days)
    return start + timedelta(days=random_days)


def generate_employes():
    last_names = LAST_NAMES
    quantity_of_entries = QUANTITY_OF_ENTRIES
    temp_last_names = []
    employees_batch = []
    with session_factory() as session:
        if session.query(Employee).count() > 0:
            quantity_of_entries = QUANTITY_OF_ENTRIES // 1000
            for last_name in last_names:
                if isinstance(last_name, tuple) and last_name[0][0] == 'F' or last_name[0] == 'F':
                    temp_last_names.append(last_name)
            last_names = temp_last_names
            temp_last_names = []

        for i in range(quantity_of_entries):
            if len(temp_last_names) == 0:
                temp_last_names = last_names[:]
            gender = choice(['Male', 'Female'])
            last_name = choice(temp_last_names)
            temp_last_names.remove(last_name)
            patronomic = choice(PATRINYMICS)

            if quantity_of_entries // 2 < i:
                gender = 'Male'
                first_name = choice(FIRST_MALE_NAMES)
                if isinstance(last_name, tuple):
                    last_name = last_name[0]
                if isinstance(patronomic, tuple):
                    patronomic = patronomic[0]
            else:
                gender = 'Female'
                first_name = choice(FIRST_FEMALE_NAMES)
                if isinstance(last_name, tuple):
                    last_name = last_name[1]
                if isinstance(patronomic, tuple):
                    patronomic = patronomic[1]

            full_name = f"{last_name} {first_name} {patronomic}"
            birth_date = generate_date(
                START_GENERATED_DATE, END_GENERATED_DATE)
            employee = Employee(full_name=full_name,
                                birth_date=birth_date,
                                gender=gender)
            employees_batch.append(employee)
            if len(employees_batch) >= 1000:
                Employee.bulk_insert(session, employees_batch)
                employees_batch = []
    if employees_batch:
        Employee.bulk_insert(session, employees_batch)


def filter_by_letter(letter='F'):
    start_time = datetime.now()
    with session_factory() as session:
        employees = session.query(Employee).filter(
            Employee.full_name.like(f"{letter}%"))
    end_time = datetime.now()
    timedelta = end_time - start_time
    print(f"quantity of entries for letter {letter}: {employees.count()}")
    print(f"Program execution time: {timedelta.microseconds}")


def delete_db():
    with session_factory() as session:
        session.query(Employee).delete()
        session.commit()
        print('Delete succesfully')


def main():
    try:
        l = sys.argv[1]
    except IndexError:
        l = '1'
    if l == '1':
        create_table()
    elif l == '2':
        try:
            insert_data(sys.argv[2], sys.argv[3], sys.argv[4])
        except IndexError:
            print('Error arguments')
    elif l == '3':
        employes_list()
    elif l == '4':
        generate_employes()
    elif l == '5':
        filter_by_letter()
    elif l == '0':
        delete_db()


if __name__ == "__main__":
    main()
