#Hardcoded Agent

from openai_module import generate_text_with_conversation
from prompts import react_system_prompt
from sample_functions import get_weather
from json_helpers import extract_json


available_actions = {
    "get_weather": get_weather
}



prompt = """Should I move to Malvern?"""

messages = [
      {"role": "system", "content": react_system_prompt},
      {"role": "user", "content": prompt}
]

turn_count = 1
max_turns = 5
while turn_count < max_turns:
    print(f"Loop: {turn_count}")
    print("--------------------")
    turn_count += 1

    response = generate_text_with_conversation(messages, model="gpt-4")

    #we want to instruct the model to call the action or the function
    json_function = extract_json(response)

    # print(f"Extracted JSON Functions {json_function}")

    if json_function:
            function_name = json_function[0]['function_name']
            function_parms = json_function[0]['function_parms']
            print(f"Function name: {function_name}")
            if function_name not in available_actions:
                raise Exception(f"Unknown action: {function_name}: {function_parms}")
            print(f" -- running {function_name} {function_parms}")
            action_function = available_actions[function_name]
            #call the function
            result = action_function(**function_parms)
            function_result_message = f"Action_Response: {result}"
            messages.append({"role": "user", "content": function_result_message})
            print(function_result_message)
    else:
        break