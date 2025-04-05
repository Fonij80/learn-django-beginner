# Learn_Django_Beginner

### Django Cheat Sheet
- Create Virtual Environment (VE):
  - ```python3 -m venv .venv```
- Activate VE:
  - ```source .venv/bin/activate```
- Deactivate VE:
  - ```deactivate```
- Update pip:
  - ```python -m pip install –upgrade pip```
- Install Django:
  - ```python -m pip install django~=<version>```
- Create Project:
  - ```django-admin startproject <project_name> .```
- Run Project:
  - ```python manage.py runserver```
- Apply Available Migrations:
  - ```python manage.py migrate```
- Create An App:
  - ```python manage.py startapp <app_name>```
- Output Content of Current VE:
  - ```pip freeze > requirements.txt```
- Run Tests:
  - ```python manage.py test```