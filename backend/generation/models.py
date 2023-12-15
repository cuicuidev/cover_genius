from pydantic import BaseModel
from enum import Enum
from typing import Optional, Iterable

class Tone(str, Enum):
    professional = "professional"
    technical = "technical"
    casual = "casual"

class Focus(str, Enum):
    company = "company"
    role = "role"
    user = "user"

class FocusIntensity(str, Enum):
    slightly = "slightly"
    moderately = "moderately"
    strongly = "strongly"
    uniquely = "uniquely"
    
class Options(BaseModel):
    tone: Tone = Tone.professional
    focus: Focus = Focus.role
    focus_intensity: FocusIntensity = FocusIntensity.slightly
    keys: Iterable[str] = []
    paragraphs: int = 3
    words: int = 500

class Target(BaseModel):
    company_name: str = "unknown"
    hiring_manager: str = "unknown"
    job_title: str = "unknown"
    job_posting: str = "unknown"

class GenerationForm(BaseModel):
    target: Target
    options: Options = Options()

class CoverLetter(BaseModel):
    content: str

class UserData(BaseModel):
    name: str = "unknown"
    surname: str = "unknown"
    age: Optional[int] = None

    education: str = "unknown"
    experience: str = "unknown"
    
    skills: str = "unknown"
    interests: str = "unknown"
    languages: str = "unknown"
    
    about: str = "unknown"
