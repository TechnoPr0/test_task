from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import enum
from datetime import datetime


class Base(DeclarativeBase):
    pass


class GenderEnum(enum.Enum):
    Male = 'Male'
    Female = 'Female'


class Employee(Base):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(index=True)
    birth_date: Mapped[datetime]
    gender: Mapped[GenderEnum] = mapped_column(nullable=False)

    def save_to_db(self, session):
        session.add(self)
        session.commit()
        print(f"Employee '{self.full_name}' added successfully!")

    def calculate_age(self):
        age = (datetime.now() - self.birth_date).days // 365
        return age

    def bulk_insert(session, employees):
        session.bulk_save_objects(employees)
        session.commit()
        print(f'{len(employees)} employes has been added successfully!')
