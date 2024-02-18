[![pipeline status](https://gitlab.crja72.ru/django/2024/spring/course/students/67134-xxtornexx2016-course-1112/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2024/spring/course/students/67134-xxtornexx2016-course-1112/-/commits/main)

# Yandex.Lyceum Django course

Online-store-like website  
Description to be completed


# Deployment
If you want to deploy the app you should follow these steps

### Set configuration
Create .env file by renaming the example one  
```bash
mv .env.example .env
```
Enter your Django api key to the appropriate field
```txt
DJANGO_SECRET_KEY=django-secret-key
```

### Set up a virtual environment
Make sure you got a new pip version
```bash
python3 -m pip3 install --upgrade pip3
```
Create venv dir and activate it
```bash
python3 -m venv venv  
source venv/bin/activate  
```
Install dependencies sufficient to run the app
```bash
pip3 install -r requirements/prod.txt  
```

### Run the app
Switch to the project dir
```bash
cd lyceum
```
Run
```bash
python3 manage.py runserver
```

