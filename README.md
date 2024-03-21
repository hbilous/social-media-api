# Social media API

API service for social media management written on DRF

## Installing using GitHub

```python
git clone https://github.com/hbilous/social-media-api.git
cd social_media_api
python -m venv venv
venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Getting access

* Create user via api/user/register
* Get access token via api/user/token

## Features

* JWT Authenticated
* Admin panel /admin/
* Documentation is located at /api/doc/swagger/
* Create posts
* Comment and likes post
* Follow users