def get_weather(city: str):
    if city == "Malvern":
        return "The weather in Malvern, PA is sunny with a high of 75°F."
    if city == "Hyderabad":
        return "The weather in Hyderabad, India is rainy with a high of 85°F."
    if city == "San Jose":
        return "The weather in San Jose, CA is cloudy with a high of 65°F."
    else:
        return "Sorry, I don't have weather information for that city."
