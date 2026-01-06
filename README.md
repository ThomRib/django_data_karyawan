# django_data_karyawan
CRUD DJANGO
1
py -3 -m venv venv

source ./venv/Scripts/activate 

or create file active.bat and past code 

@ECHO OFF
CMD /k "cd /d D:\program_baru\venv\Scripts & activate & cd /d D:\program_baru\crud_karyawan & python manage.py runserver 0.0.0.0:8000"

pip install "Django==2.2.17"

django-admin startproject karyawan .(1)

python manage.py startapp admin

python manage.py runserver





