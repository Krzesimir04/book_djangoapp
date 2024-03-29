# Physiotherapist's website with reservation function

![main page](./img/main_page.png)

## Usage

At the beginnig you should register.

<img src="./img/register.png" alt="Register button" width="300"/>

Then buttons are changed and you can easley book a free term.

<img src="./img/reservation.png" alt="Register button" width="300"/>

On the next page you can choose when you have time for your massage.

<img src="./img/date_page.png" alt="Register button" width="800"/>

At this moment you can choose your visit and book it. Your reservation will be seen on the right side of the page and on the main page you will see if you have any reservation (without red frame).

<img src="./img/reservation_2_page.png" alt="Register button" width="800"/>

<img src="./img/visible_reservation.png" alt="Register button" width="400"/>


## Installation on local machine

If you want to test app on your machine you can download repo, make virtual enviroment, download packages and runserver on your computer (you must have python 3.8 installed).

```
git init
git pull https://github.com/Krzesimir04/book_djangoapp
python -m venv env
source env/bin/activate
cd book_proj/
pip install -r requirements.txt
python manage.py runserver
```
If you are on windows use `./env/Scripts/activate` instead of `source env/bin/activate`.

## Additional information

- You can book only 5 visits
- Password validation is turned off
- Python versions used with django: https://docs.djangoproject.com/en/4.1/faq/install/#what-python-version-can-i-use-with-django
