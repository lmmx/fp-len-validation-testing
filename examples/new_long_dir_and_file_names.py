from pydantic import BaseModel, NewPath, ValidationError


class Unrealistic(BaseModel):
    path: NewPath


long_dir_and_file = f"{'a' * 1000}/{'b' * 1000}"

try:
    Unrealistic(path=long_dir_and_file)
except ValidationError as ve:
    pass  # Too long
except OSError:
    raise RuntimeError("This should not raise an OSError")
