# Backend+Front-end Setup

```sh
python -m venv .venv
``` 

Then activate the virtual environment. After that run pre-scripts:

```sh
python manage.py makemigrations
python manage.py migrate
```

Then run the server

```sh
python manage.py runserver 0.0.0.0:5197
```

This will host it on the network at `device_ip:port`