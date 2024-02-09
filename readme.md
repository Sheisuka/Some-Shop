
[![pipeline status](https://gitlab.crja72.ru/django/2024/spring/course/students/67134-xxtornexx2016-course-1112/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2024/spring/course/students/67134-xxtornexx2016-course-1112/-/commits/main)

# Инструкция по запуску через bash  
  
## Конфигурация  
mv .env.example .env  
echo 'DJANGO_SECRET_KEY=<YOUR_KEY>' > .env  
echo 'DJANGO_DEBUG=<Flag>' >> .env  
  
## Подготовка окружения
python3 -m venv venv  
source venv/bin/activate  
pip3 install -r requirements/prod.txt  
  
## Запуск сервера  
cd lyceum  
python3 manage.py runserver
