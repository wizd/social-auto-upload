import os
import concurrent.futures

from llava_client import llava_inference

def process_video_frames(input_dir, question, num_concurrent=4):
    # 获取输入目录下所有的 .png 文件，并按名字排序
    image_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])
    
    # 初始化时间轴和输出结果
    timeline = []
    output = ""
    
    # 定义一个辅助函数，用于调用 llava_inference 并返回结果和图片索引
    def process_image(index, image_file):
        image_path = os.path.join(input_dir, image_file)
        description = llava_inference(question, image_path)
        return index, description
    
    # 使用 concurrent.futures 模块实现并发调用
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_concurrent) as executor:
        # 提交所有的推理任务
        futures = [executor.submit(process_image, i, image_file) for i, image_file in enumerate(image_files)]
        
        # 等待所有任务完成并获取结果
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    
    # 根据图片索引对结果进行排序
    results.sort(key=lambda x: x[0])
    
    # 将结果排版成时间轴格式
    for i, (_, description) in enumerate(results):
        seconds = i * 2
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        timestamp = f"[{hours:02d}:{minutes:02d}:{seconds:02d}]"
        timeline.append(f"{timestamp}:\n\n{description}\n\n")
    
    # 将时间轴格式化为输出结果
    output = "\n".join(timeline)
    
    return output