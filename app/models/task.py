from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[datetime:datetime] = mapped_column(nullable=True)
    #is_complete: Mapped[bool]

    def to_dict(self):
        task_as_dict = {}
        task_as_dict["title"] = self.title,
        task_as_dict["description"] = self.description,
        task_as_dict["completed_at"] = self.completed_at
        return task_as_dict


    @classmethod
    def from_dict(cls,task_data):
        new_data = cls(title=task_data["title"],
                    description=task_data["description"],
                    completed_at=task_data["completed_at"])
        return new_data
    
