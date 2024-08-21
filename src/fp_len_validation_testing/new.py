from pydantic import BaseModel, NewPath


class Unrealistic(BaseModel):
    path: NewPath
