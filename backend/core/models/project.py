from core.models.base import BaseModel


class Project(BaseModel):
    name: str
    description: str
    is_active: bool
    is_archived: bool
    lead_employee_id: int
