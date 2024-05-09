from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):
    print(text)

scheduler = BlockingScheduler()
# # 在 2019-8-30 运行一次 job 方法
# scheduler.add_job(job, 'date', run_date=date(2019, 8, 30), args=['text1'])
# # 在 2019-8-30 01:00:00 运行一次 job 方法
# scheduler.add_job(job, 'date', run_date=datetime(2019, 8, 30, 1, 0, 0), args=['text2'])
# # 在 2019-8-30 01:00:01 运行一次 job 方法
scheduler.add_job(job, 'cron', hour='15-16', minute='44', args=['job2'])

scheduler.start()