ffmpeg -i biden.mp4 -vf fps=1/2 -start_number 0 -ss 00:00:00 -qscale:v 2 .\out\frame%04d.png

for %f in (.\out\*.png) do python ..\downloader\llava_client.py "图片里面是什么内容？" "%f"


curl http://192.168.3.81:5010/v1/api/completions -d '{
  "model": "Meta-Llama-3-8B-Instruct",
  "prompt": "Why is the sky blue?",
  "stream": false
}'

curl http://192.168.3.81:5010/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer aaa"   -d '{
    "model": "Meta-Llama-3-8B-Instruct",
    "stream": "false",
    "messages": [
      {
        "role": "system",
        "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
      },
      {
        "role": "user",
        "content": "Compose a poem that explains the concept of recursion in programming."
      }
    ]
  }'