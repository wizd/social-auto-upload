from imgs2desc import process_video_frames
from openai import OpenAI

input_dir = ".\\out"  # 替换为实际的输入目录路径
question = "图片是一张视频的截图，请描述图片中的内容，输出为中文。"  # 替换为实际的问题
num_concurrent = 4  # 指定并发数量，可根据需要调整

video_description = process_video_frames(input_dir, question, num_concurrent)
print(video_description)


client = OpenAI(base_url="http://192.168.3.81:5010/v1", api_key="aaa")

user_prompt = f"""请根据下面包括在四个反引号内的视频截图的描述,简单概括视频内容。 

````
{video_description}
````
"""

completion = client.chat.completions.create(
  model="Meta-Llama-3-8B-Instruct",
  messages=[
    {"role": "system", "content": "你是一个视频发布者。"},
    {"role": "user", "content": user_prompt}
  ]
)

print(completion.choices[0].message.content)