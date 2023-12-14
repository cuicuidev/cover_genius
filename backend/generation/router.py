from fastapi.routing import APIRouter

from . import main
from . import models

router = APIRouter(prefix="/generation", tags=["generation"])

DUMMY_USER_DATA = models.UserData(
	name = "John",
	surname = "Doe",
	about = "I'm a software engineer. I like to code. I enjoy music, movies, and books. I am a fan of the Lord of the Rings. I excel at Python and Rust. I specialize in machine learning and backend development. I have worked with many different technologies, including Docker, Kubernetes, and AWS. I have a Master's degree in Computer Science. I have worked at Uber and Netflix. Also, I have many contributions to the linux kernel and I am close friends with Linus Torvalds.",
)

DUMMY_TARGET = models.Target(
	target_name = "OpenAI",
	recruiter_name = "Sam Altman",
	url = "https://openai.com/jobs/?ref=ai-jobs.net",
	type = models.TargetType.job_posting,
	description = "OpenAI is an AI research and deployment company. Our mission is to ensure that artificial general intelligence benefits all of humanity. The OpenAI Charter describes the principles that guide us as we execute on our mission. Our research goal is to build safe AGI, and ensure AGI's benefits are as widely and evenly distributed as possible. We expect AI technologies to be hugely impactful in the short term, but their impact will be outstripped by that of the first AGIs. We're a non-profit and our full-time staff of 100+ researchers are based primarily in San Francisco. We're supported by several hundred staff based around the world. We're also advised by some of the world's leading AI researchers. OpenAI LP is our parent organization; the for-profit arm manages our investments. We've raised $1B in committed funding, and we're hiring for a number of roles.",
)

DUMMY_OPTIONS = models.Options(
	tone = models.Tone.casual,
	paragraphs = 4,
	words = 900,
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
	#target = generation_form.target
	#options = generation_form.options

	user_data = DUMMY_USER_DATA
	target = DUMMY_TARGET
	options = DUMMY_OPTIONS

	cover_letter = main.generate(user_data=user_data, target=target, options=options)
	return cover_letter
