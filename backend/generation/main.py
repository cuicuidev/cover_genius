from . import models
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
import os

def generate(user_data: models.UserData, target: models.Target, options: models.Options) -> str:
	key = os.environ.get("OPENAI_API_KEY")
	
	system_message = f"You are an assistant. Your job is to write cover letters for the users so they can apply to {target.target_name}, a {target.type}.\
	 The tone must be {options.tone}. Keep the letter under {options.paragraphs} paragraphs and {options.words} words. \
	 This is the {target.type} site: {target.url}. Wait for the user to give you some information about themselves."

	user_message = f"Hi, I am {user_data.name} {user_data.surname}. Here is some information about me: {user_data.about}"

	if key is None:
		with open(".env", "r") as f:
			lines = f.readlines()

		for line in lines:
			key, value = line.split("=")
			if key == "OPENAI_API_KEY":
				API_KEY = value.strip()
				break
	
	openai = OpenAI(api_key=API_KEY)
	
	completion = openai.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": system_message}, 
			{"role": "user", "content": user_message},
		]
	)

	cover_letter_text = completion.choices[0].message.content

	cover_letter = models.CoverLetter(cover_letter=cover_letter_text)
	return cover_letter
