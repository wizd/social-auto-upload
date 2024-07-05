import asyncio
from datetime import datetime, timedelta
import os
from pathlib import Path

import sys
sys.path.append(sys.path[0] + '/..')
from conf import BASE_DIR
from tencent_uploader.main import weixin_setup, TencentVideo
from utils.constant import TencentZoneTypes
from utils.files_times import generate_schedule_time_next_day, get_title_and_hashtags


if __name__ == '__main__':
    filepath = Path(BASE_DIR) / "videos"
    account_file = Path(BASE_DIR / "tencent_uploader" / "account.json")
    # 获取视频目录
    folder_path = Path(filepath)
    # 获取文件夹中的所有文件
    files = list(folder_path.glob("*.mp4"))
    file_num = len(files)
    #publish_datetimes = generate_schedule_time_next_day(file_num, 1, daily_times=[16])
    cookie_setup = asyncio.run(weixin_setup(account_file, handle=True))
    category = TencentZoneTypes.LIFESTYLE.value  # 标记原创需要否则不需要传
    for index, file in enumerate(files):
        title, tags = get_title_and_hashtags(str(file))
        # 打印视频文件名、标题和 hashtag
        print(f"视频文件名：{file}")
        print(f"标题：{title}")
        print(f"Hashtag：{tags}")

        # 当前时间
        now = datetime.now()

        # 定义两小时十分钟的时间间隔
        two_hours_ten_minutes = timedelta(hours=2, minutes=30)

        # 计算两小时十分钟之后的时间
        future_time = now + two_hours_ten_minutes
                          
        app = TencentVideo(title, file, tags, future_time, account_file, category)
        asyncio.run(app.main(), debug=False)
        os.remove(str(file))