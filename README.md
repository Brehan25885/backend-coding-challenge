# backend-coding-challenge
# backend-coding-challenge

```bash
$ # Get the code
$ git clone https://github.com/Brehan25885/backend-coding-challenge.git

$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate

$ pip3 install -r requirements.txt


$ # Create .env file in same settings.py path

$ vim .env 
SECRET_KEY=
ENVIRONMENT =DEVELOPMENT or STAGING or PRODUCTION
$ #to get secret key
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
$ #to migrate datase
$ python manage.py migrate


$ # Start the application (development mode)
$ python manage.py runserver # default port 8000

$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$ # Access the web app in browser: http://127.0.0.1:8000/

$ python manage.py runserver # default port 8000

## to test endpoint in this repo
$curl -v http://localhost:8000/languages-repos/


```

