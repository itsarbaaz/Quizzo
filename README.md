# Quizzo


A dynamic online quiz organizing website built with Django, leveraging the power of Python.  
The project utilizes Bootstrap4 for captivating front-end design and PostgreSQL for robust back-end data storage.

## Current Features

### Features for site access::

- To access the Quiz, the user needs to be logged in.
- A user must provide their username, first and last names, email address, and password in order to sign up.
- The user will simply need to input their username and password to log in.

### Quiz Features:

- The test has multiple-choice questions for each question.
- Each question is shown to a user only once.
- Questions are displayed randomly for every user.
- A new question will be presented to the user and the prior question will be recorded as attempted if the user accidentally presses refresh or returns to the previous page.
- After each attempted question, whether the response was correct or not, a message will be shown.

### Leaderboard features:

- The leaderboard is a list that has been shortened based on the users' scores.
- If two users score the same, the one who signed up earlier will rank higher than the user who signed up later.
- Anybody can access the leaderboard. No login is needed.

### Administrative features:

- Questions can only be added by admin.
- Admin may modify the questions and the appropriate response.
- Admin can see a list of all questions.
- The administrator can search questions using the question or choice text.
- Depending on whether or not a question has been published, an administrator can filter the inquiries.

## Getting started with development

Dependencies:

- Python 3.6.x
- Django 4.2.x

### 1. Clone this repository

```bash
git clone https://github.com/itsarbaaz/Quizzo.git
cd Quizzo
```


### 2. Create the virtual environment and Activate it 

```bash
## run following command from `Quizzo` directory
python -m venv env
env/bin/activate

```

### 3. Install python packages

```bash
pip install -r requirements.txt
```

### 4. Configure the database
_In settings.py file, Locate the DATABASES section, which contains the configuration for the database.Update the configuration to use PostgreSQL by providing the necessary settings ._

### 5. Run database migrations

```bash
cd Quizzo
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run development server

```bash
python manage.py runserver
```

## Contributors

- [Arbaaz Khan](https://github.com/itsarbaaz)
