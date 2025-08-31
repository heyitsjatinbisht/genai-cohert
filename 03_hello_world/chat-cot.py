import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI()

# Chain of Thought prompting


SYSTEM_PROMPT= """
You are an helpful AI assistant who is specialized in solving user query.
For the given user input , analyse the input and break down the problem steps by steps.

The steps are you get a user input, you analyse , you think , you think again and think for several times and then return the output with explanation.

Follow the steps in sequence that is "analyse" , "think", "output", "validate" and finaly "result"

Rules:
1. Follow the strict JSON output format.
2. Always perform one step at a time and wait for the next input.
3. Carefully explain the steps and give a clear and concise output.

Example:
Input: What is 2 + 2.
Output: {{"step": "analyse", "content": "Alright! The user is interested in math query and he wants to know the sum of 2 and 2."}}
Output: {{"step": "think", "content": "To perform this addition , I must go from left to right and add 2 and 2."}}
Output: {{"step": "validate", "content":"Seems like the answer is correct and it is 4."}}
Output: {{"step": "result", "content":"2 + 2 = 4 and this is calculated by adding 2 and 2."}}

"""

# response = client.chat.completions.create(
#     model="gpt-4.1-mini",
#     messages=[
#         {"role": "system", "content":SYSTEM_PROMPT},
#         {"role": "user", "content": "What is capital of Maharastra"},
#         {"role": "assistant", "content": json.dumps({"step": "analyse", "content": "The user is asking for the capital city of Maharashtra, which is a state in India."})},
#         {"role": "assistant", "content": json.dumps({"step": "think", "content": "To answer this, I need to recall the capital city of Maharashtra state. From general knowledge, the capital of Maharashtra is Mumbai."})},
#         {"role": "assistant", "content": json.dumps({"step": "validate", "content": "Mumbai is widely recognized and officially the capital city of Maharashtra. This information is consistent across reliable sources."})},
#         {"role": "assistant", "content": json.dumps({"step": "result", "content": "The capital of Maharashtra is Mumbai."})},
       
#     ]
# )

# print(response.choices[0].message.content)


messages = [
    {"role": "system", "content":SYSTEM_PROMPT},
]

query = input("> ")

messages.append({"role": "user", "content": query})


while True:
    response = client.chat.completions.create(
        model="gpt-4.1",
        response_format={"type": "json_object"},
        messages=messages
    )
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    parsed_response = json.loads(response.choices[0].message.content)
    
    if parsed_response.get("step") != "result":
        print("🧠", parsed_response.get("content"))
        continue
    
    print("🤖", parsed_response.get("content"))
    break