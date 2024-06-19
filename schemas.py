from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    
    
class STask(STaskAdd):
    id: int
    
    class Config:
        from_attributes = True # for pydantic - model_validate()


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
