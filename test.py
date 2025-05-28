from openai_module import generate_text_basic

prompt = "how to make coffee"

response = generate_text_basic(prompt, "gpt-4")
print(response)