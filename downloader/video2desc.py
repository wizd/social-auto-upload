from inference import openai_inference
from imgs2desc import process_video_frames

input_dir = ".\\out"  # 替换为实际的输入目录路径
question = "图片是一张视频的截图，请描述图片中的内容，输出为中文。"  # 替换为实际的问题
num_concurrent = 4  # 指定并发数量，可根据需要调整

video_description = process_video_frames(input_dir, question, num_concurrent)
print(video_description)


user_prompt = f"""请根据下面包括在四个反引号内的视频截图的描述,简单描述整个视频是关于什么内容的。由于视频经过多模态大语言模型的识别，可能存在谬误，请修正可能的识别错误。 

````
{video_description}
````
"""

out1 = openai_inference("你是一个视频发布者。", user_prompt)

print(out1)