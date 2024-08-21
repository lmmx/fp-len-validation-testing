from pydantic import BaseModel, FilePath


class Overconfident(BaseModel):
    path: FilePath
