from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Employee
from schemas import EmployeeCreate, EmployeeResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create employee
@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    emp = Employee(
        name=employee.name,
        role=employee.role,
        salary=employee.salary
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


# Read all employees
@app.get("/employees", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


# Update employee
@app.put("/employees/{emp_id}", response_model=EmployeeResponse)
def update_employee(emp_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        return {"error": "Employee not found"}

    emp.name = employee.name
    emp.role = employee.role
    emp.salary = employee.salary

    db.commit()
    db.refresh(emp)
    return emp


# Delete employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        return {"error": "Employee not found"}

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}
