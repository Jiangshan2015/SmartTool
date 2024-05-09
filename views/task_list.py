import time
from notifypy import Notify

while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
    if time_now == "15:25:00": #此处设置每天定时的时间
        # 此处3行替换为需要执行的动作
        print("hello")
        notification = Notify()
        notification.title = "Cool Title"
        notification.message = "Even cooler message."
        # notification.audio = "path/to/audio/file.wav"

        notification.send()
        subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 定时发送测试"
        print(subject)

        time.sleep(2) # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次




