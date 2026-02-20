from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    email: str
    roll_no: str
    cgpa: float | None = None
    department: str

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int
    class Config:
        orm_mode = True