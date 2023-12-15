from fastapi.routing import APIRouter

from . import main
from . import models

router = APIRouter(prefix="/generation", tags=["generation"])

DUMMY_USER_DATA = models.UserData(
	name = "Benito",
	surname = "Camelas",
	about = "I'm a software engineer. I like to code. I enjoy music, movies, and books. I am a fan of the Lord of the Rings. I excel at Python and Rust. I specialize in machine learning and backend development. I have worked with many different technologies, including Docker, Kubernetes, and AWS. I have a Master's degree in Computer Science. I have worked at Uber and Netflix. Also, I have many contributions to the linux kernel and I am close friends with Linus Torvalds.",
)

@router.get("/")
async def root_generation():
	check = {
		"route": "/generation",
		"status": "OK",
		"message": "This is the generation route"
	}
	return check

@router.post("/generate")
async def generate(generation_form: models.GenerationForm) -> models.CoverLetter:
	target = generation_form.target
	options = generation_form.options

	user_data = DUMMY_USER_DATA

	cover_letter = main.generate(user_data=user_data, target=target, options=options)
	return cover_letter
