from pydantic import BaseModel, FilePath, ValidationError


class Overconfident(BaseModel):
    path: FilePath


try:
    failure = Overconfident(path="x" * 1000)
except ValidationError as ve:
    failure = True

assert failure is True
