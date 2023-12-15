from . import models, crawler
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
import os

def generate(user_data: models.UserData, target: models.Target, options: models.Options) -> str:
    key = os.environ.get("OPENAI_API_KEY")

    system_message = f"""
    You are an assistant helping job seekers write cover letters for a job position. The company name is {target.company_name} and 
    the job position is {target.job_title}. The name of the hiring manager is {target.hiring_manager}. You must write a cover 
    letter composed of {options.paragraphs} paragraphs that is at most {options.words} words long. The cover letter must be 
    written in a {options.tone} tone. You should {options.focus_intensity} focus on the {options.focus} when writing the cover 
    letter. Also, you have to consider the following key aspects and try to incorporate them into the cover letter: {options.keys}. 
    If you consider that some of these aspects are not relevant, you can ignore them. Ensure that the cover letter is written in 
    the same language as the job posting. Please await for the user's information before starting to write the cover letter.
    Here's the job posting:
    {target.job_posting}
    """

    user_message = f"""
    The user's name is {user_data.name} and their surname is {user_data.surname}. They are {user_data.age} years old.
    This is their educational background: {user_data.education}.
    This is their past work experience: {user_data.experience}.
    This is their skills: {user_data.skills}.
    These are their interests: {user_data.interests}.
    They speak the following languages: {user_data.languages}.

    This is their `about me` section: {user_data.about}.

    Please proceed to write the cover letter as per the instructions aforementioned.
    """

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
            {"role": "system", "content": user_message},
        ]
    )

    cover_letter_text = completion.choices[0].message.content

    cover_letter = models.CoverLetter(content=cover_letter_text)
    return cover_letter
