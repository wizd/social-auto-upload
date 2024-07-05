import asyncio
import os
from pathlib import Path
from datetime import datetime, timedelta

import sys
sys.path.append(sys.path[0] + '/..')

from conf import BASE_DIR
from douyin_uploader.main import douyin_setup, DouYinVideo
from utils.files_times import generate_schedule_time_next_day, get_title_and_hashtags


if __name__ == '__main__':
    filepath = Path(BASE_DIR) / "videos"
    account_file = Path(BASE_DIR / "douyin_uploader" / "account.json")
    # 获取视频目录
    folder_path = Path(filepath)
    # 获取文件夹中的所有文件
    files = list(folder_path.glob("*.mp4"))
    file_num = len(files)
    #publish_datetimes = generate_schedule_time_next_day(file_num, 600, daily_times=[650])
    cookie_setup = asyncio.run(douyin_setup(account_file, handle=False))
    for index, file in enumerate(files):
        title, tags = get_title_and_hashtags(str(file))
        # 打印视频文件名、标题和 hashtag
        print(f"视频文件名：{file}")
        print(f"标题：{title}")
        print(f"Hashtag：{tags}")
        # app = DouYinVideo(title, file, tags, publish_datetimes[index], account_file)
        # 当前时间
        now = datetime.now()

        # 定义两小时十分钟的时间间隔
        two_hours_ten_minutes = timedelta(hours=2, minutes=30)

        # 计算两小时十分钟之后的时间
        future_time = now + two_hours_ten_minutes
        app = DouYinVideo(title, file, tags, future_time, account_file)
        asyncio.run(app.main(), debug=False)
        os.remove(str(file))