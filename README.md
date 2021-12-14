# Instagram

#### Created By Rodger Kamau on 12-12-2021

## Description

Instagram like app will allow users to post view like and comment on photos among different users of the web app. Users get to view photos updated by other users. They can also click on a photo and view more details about it. It was developed using python-django

## Setup Requirements

- Git
- Web-browser or your choice
- Github
- Django 3.2.7
- Python 3.8
- PostgreSQL
- Cloudinary (for image upload)

```
   - CLOUD_NAME
   - API_KEY
   - API_SECRET
```

## Setup Installation

- Copy the github repository url
- Clone to your computer
- Open terminal and navigate to the directory of the project you just cloned to your computer
- Run the following command to start the server using virtual environment

```
python3.8 -m venv --without-pip virtual
```

- To activate the virtual environment

```
source virtual/bin/activate
```

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

```
pip install -r requirements.txt
```

- To copy .env.example to .env

```
cp .env.example .env
```

- Edit the .env file and replace the values with your own Cloudinary credentials and database credentials

- To run the server

```
python manage.py runserver

```

- Open the browser and navigate to http://127.0.0.1:8000/ to see the application in action

## Technologies Used

The following languages have been used on this project:

- HTML
- CSS
- Bootstrap
- Python
- Django
- PostgreSQL

## Setup/Installation Requirements

- Live link to view the project <a target="_blank" href="https://instagramiz.herokuapp.com/">View Instagram</a>


## Known Bugs

The image uploading function is not working but it runs locally

## Support and contact details 🙂

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: rodgerkamau@student.moringaschool.com
- Phone: +254712345678