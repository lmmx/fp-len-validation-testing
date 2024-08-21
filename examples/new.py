from pydantic import BaseModel, NewPath, ValidationError


class Unrealistic(BaseModel):
    path: NewPath


try:
    failure = Unrealistic(path="x" * 1000)
except ValidationError as ve:
    failure = True

assert failure is True
