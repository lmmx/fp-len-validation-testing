from pydantic import BaseModel, NewPath, ValidationError


class Unrealistic(BaseModel):
    path: NewPath


try:
    Unrealistic(path="/sys/foo")
except ValidationError as ve:
    pass  # Parent directory is read-only
except:
    raise RuntimeError("This should not raise a non-ValidationError")
else:
    raise RuntimeError("This should raise a ValidationError")
