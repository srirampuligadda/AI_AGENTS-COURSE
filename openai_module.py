from openai import OpenAI
import os
from dotenv import load_dotenv


#Load Environment Variables
load_dotenv()

#Create an instance of the OpenAI class
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text_basic(prompt:str, model:str="gpt-3.5-turbo", system_prompt:str="You are a helpful assistant."):

    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
                ]
        )
        response_message = response.model_dump()['choices'][0]['message']['content']
        # response_message = response['choices'][0]['message']['content']
        # print(response_message)
        return response_message
    except Exception as e:
        print(f"Error generating text: {e}")
        return None