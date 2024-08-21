from pydantic import BaseModel, FilePath, ValidationError


class Overconfident(BaseModel):
    path: FilePath


try:
    Overconfident(path="x" * 1000)
except ValidationError as ve:
    pass
except OSError:
    raise RuntimeError("This should not raise an OSError")
