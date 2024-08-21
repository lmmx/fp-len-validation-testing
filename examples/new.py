from pydantic import BaseModel, NewPath, ValidationError


class Unrealistic(BaseModel):
    path: NewPath


try:
    Unrealistic(path="x" * 1000)
except ValidationError as ve:
    pass
except OSError:
    raise RuntimeError("This should not raise an OSError")
