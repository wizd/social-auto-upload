from openai import OpenAI

client = OpenAI(base_url="http://192.168.3.81:5010/v1", api_key="aaa")

def openai_inference(sys_prompt, user_prompt):
    completion = client.chat.completions.create(
    model="Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    )

    return completion.choices[0].message.content