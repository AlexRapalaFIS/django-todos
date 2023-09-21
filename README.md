# Django Todo

Before setting up make sure to have the following things installed. Windows users will need to install using different methods.

1. `brew install pyenv`
2. `pyenv install 3.9.13`
3. `pyenv global 3.9.13`
4. `brew install postgresql`
5. `brew services start postgresql`
6. `createdb todos-django`

Create a Django Todo app

1. `poetry install`
2. `poetry run python manage.py migrate`
3. `poetry run python manage.py runserver`
