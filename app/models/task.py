from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[datetime | None] = mapped_column(nullable=True, default=None)
    

    def to_dict(self):
        task_as_dict = {}
        task_as_dict['id'] = self.id
        task_as_dict["title"] = self.title
        task_as_dict["description"] = self.description
        task_as_dict["is_complete"] =  self.completed_at is not None 
        return task_as_dict


    @classmethod
    def from_dict(cls,task_data):
        new_data = cls(title = task_data["title"],
                    description = task_data["description"],
                    completed_at = task_data.get("completed_at") # Or explicitly set to None otherwise  KEYERROR
                    )
        return new_data
    
