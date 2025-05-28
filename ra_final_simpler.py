#Hardcoded Agent
from SimplerLLM.language.llm import LLM, LLMProvider
from json_helpers import extract_json

llm_instance = LLM.create(provider=LLMProvider.OPENAI,model_name="gpt-4")



from prompts import react_system_prompt
from sample_functions import get_weather

available_actions = {
    "get_weather": get_weather
}

prompt = """How is the weather in Malvern?"""

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

    response = llm_instance.generate_response(messages=messages)
    print(f"Response from model: {response}")
     #we want to instruct the model to call the action or the function
    json_function = extract_json(response)
    print(f"Extracted JSON Functions {json_function}")

    # print(f"Extracted JSON Functions {json_function}")

    if json_function:    {
      "python.analysis.extraPaths": [
        "/Users/srirampuligadda/Documents/workspace/AI_AGENTS-COURSE"
      ]
    }
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

   