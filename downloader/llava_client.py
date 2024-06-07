import argparse
import base64
import requests
import json

def llava_inference(question, image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    data = {
        "model": "llava:34b-v1.6-q6_K",
        "prompt": question,
        "images": [encoded_image],
        "stream": False
    }

    response = requests.post('http://172.30.55.208:11434/api/generate', json=data)

    if response.status_code == 200:
        result = response.json()
        return result['response']
    else:
        raise Exception(f"请求失败，状态码：{response.status_code}")

def main():
    parser = argparse.ArgumentParser(description='Ollama 客户端多模态推理')
    parser.add_argument('question', type=str, help='问题')
    parser.add_argument('image_path', type=str, help='图片路径')
    args = parser.parse_args()

    try:
        result = llava_inference(args.question, args.image_path)
        print(result)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
