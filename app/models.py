from pydantic import BaseModel
from typing import Dict

class CommentResponse(BaseModel):
    task_id: str
    status: str
    result: str | None = None

class ExplanationResponse(BaseModel):
    task_id: str
    status: str
    result: Dict[str, str]
