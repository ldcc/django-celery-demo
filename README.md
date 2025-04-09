# Django + Celery 实战

## 环境

```shell
docker run -d -p 15672:15672 -p 5672:5672 rabbitmq:3-management

conda create -n django
conda activate django
pip install django
pip install djangorestframework
pip install celery
pip install django-celery-beat
pip install amqp
pip install django-cryptography
pip install python-crontab
```

## 测试

```shell
# 数据库配置
#python manage.py makemigrations
#python manage.py migrate

# Django 应用启动
python manage.py runserver

# Celery Beat 定时任务调度
celery -A host_management beat -l info

# Celery Worker 处理异步任务
celery -A host_management worker -l info
```
