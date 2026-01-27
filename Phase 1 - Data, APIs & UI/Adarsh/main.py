from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Employee
from schemas import EmployeeCreate, EmployeeResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(
        name=employee.name,
        department=employee.department,
        salary=employee.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@app.get("/employees", response_model=list[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()

    if emp is None:
        return {"error": "Employee not found"}

    emp.name = employee.name
    emp.department = employee.department
    emp.salary = employee.salary

    db.commit()
    db.refresh(emp)

    return emp

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()

    if emp is None:
        return {"error": "Employee not found"}

    db.delete(emp)
    db.commit()

    return {"message": "Employee deleted successfully"}
