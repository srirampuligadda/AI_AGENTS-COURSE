#Hardcoded Agent

from openai_module import generate_text_basic
from sample_functions import get_weather

current_weather = get_weather("Hyderabad")
prompt = f"""Should I take an umbrella if I am going out in Hyderabad today basing on the weather conditions : {current_weather}?"""

response = generate_text_basic(prompt, model="gpt-4")

print(response)