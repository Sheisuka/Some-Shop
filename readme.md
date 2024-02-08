Инструкция по запуску

touch .env
echo 'DJANGO_SECRET_KEY=<YOUR_KEY>' >> .env
echo 'DJANGO_DEBUG=<True or False>' >> .env
python3 -m venv venv  
source venv/bin/activate  
pip3 install -r requirements.txt  
cd lyceum  
python3 manage.py runserver
