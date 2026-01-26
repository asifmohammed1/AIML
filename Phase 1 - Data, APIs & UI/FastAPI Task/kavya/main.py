from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, get_db
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")
@app.post("/employees/", response_model=schemas.Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# READ 
@app.get("/employees/", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = db.query(models.Employee).offset(skip).limit(limit).all()
    return employees

# READ(single)
@app.get("/employees/{emp_id}", response_model=schemas.Employee)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found")
    return employee

# UPDATE
@app.put("/employees/{emp_id}", response_model=schemas.Employee)
def update_employee(emp_id: int, updated_emp: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found")
    update_data = updated_emp.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    
    db.commit()
    db.refresh(db_employee)
    return db_employee

# DELETE
@app.delete("/employees/{emp_id}", status_code=status.HTTP_200_OK)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found")
    
    db.delete(db_employee)
    db.commit()
    return {"message": f"Employee {emp_id} deleted successfully"}