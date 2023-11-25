from celery import Celery

# 初始化
app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='redis://localhost:6379/0')

# 更新配置
# 方式一
app.conf.task_serializer = 'json'
# 方式二
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Asia/Shanghai',
    enable_utc=True,
)
# 方式三
app.config_from_object('celery_demo.celery_config')
