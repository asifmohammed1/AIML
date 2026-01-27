from sqlalchemy.orm import Session
from . import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()

def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    db_employee = get_employee(db, emp_id)
    if db_employee:
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, emp_id: int):
    db_employee = get_employee(db, emp_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
