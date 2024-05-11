from sqlalchemy import Column, Integer, String, Boolean, Enum
from enum import Enum as PythonEnum
from app.core.database import Base
from .common import CommonModel

class UserRole(str, PythonEnum):
	user = "user"
	admin = "admin"

class User(CommonModel):
	__tablename__ = "users"

	email = Column(String, unique=True, index=True)
	password = Column(String)
	first_name = Column(String, nullable=True)
	last_name = Column(String, nullable=True)
	role = Column(Enum(UserRole), default=UserRole.user)
	phone_number = Column(String)  # New field
	def __repr__(self):
		return f"{self.email}"


class FileStatus(Base):
    __tablename__ = "file_status"

    id = Column(Integer, primary_key=True)
    description = Column(String(50))
    is_active = Column(Boolean)

    def __repr__(self):
        return f"<FileStatus(id={self.id}, description={self.description}, is_active={self.is_active})>"



metadata = Base.metadata


