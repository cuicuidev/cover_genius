import traceback, os

# Importing OpenAI object
from openai import OpenAI

# Importing FastAPI object
from fastapi import FastAPI

# Importing settings
from settings import API_VERSION, AUTHORS

# Importing routers
from user.router import router as user_router
from generation.router import router as generation_router 

#####################################################################################################################

app = FastAPI()
app.include_router(user_router)
app.include_router(generation_router)

#####################################################################################################################
@app.get("/")
async def root():
	check = {
		"route": "/",
		"status": "OK",
		"message": "Server is running",
		"version": API_VERSION,
		"authors": AUTHORS,
		"documentation": "/docs"	
	}
	return check

@app.get("/health")
async def health():
	openai, details = connect_to_openai()
	health = {
		"health": "OK",
	}

	if not openai:
		health["health"] = "Failure to connect to OpenAI"
		health["details"] = details

	return health

#####################################################################################################################

def connect_to_openai():
	details = ""
	try:
		key = os.environ.get("OPENAI_API_KEY")
		if key is None:
			with open(".env", "r") as f:
				lines = f.readlines()
			for line in lines:
				key, value = line.split("=")
				if key == "OPENAI_API_KEY":
					break

		key = key.strip()
		openai = OpenAI(api_key=key)
		return openai, details
	except Exception as e:
		details = f"Error: {e}, details: {traceback.format_exc()}"
		return False, details
