from pydantic import BaseModel
from enum import Enum
from typing import Optional

class TargetType(str, Enum):
	job_posting = "job posting"
	company = "company"
	educaional_institution = "educaional institution"

class Tone(str, Enum):
	professional = "professional"
	technical = "technical"
	casual = "casual"

class Target(BaseModel):
	target_name: str
	recruiter_name: Optional[str]
	url: Optional[str]
	type: TargetType
	description: Optional[str] = None

class Options(BaseModel):
	tone: Optional[Tone] = None
	paragraphs: Optional[int] = None
	words: Optional[int] = None

class GenerationForm(BaseModel):
	target: Target
	options: Optional[Options] = None

class CoverLetter(BaseModel):
	cover_letter: str

class UserData(BaseModel):
	name: str
	surname: str
	about: Optional[str] = None
