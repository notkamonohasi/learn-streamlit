from enum import Enum

from pydantic import BaseModel, Field


class Status(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class ApiInput(BaseModel):
    id: str = Field(..., description="ID")
    name: str = Field(..., description="name")
    age: int = Field(..., ge=0, description="age")


class ApiOutput(BaseModel):
    status: Status = Field(..., description="user status")
