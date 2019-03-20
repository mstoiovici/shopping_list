# shopping_list

This is a shopping-list app built with Python3 and Flask.
The app has the following features: add new entry, delete entry and delete entire list.

In order to run it locally use command: 
   - python main.py
   
I used Cloud SDK to deploy it on Google App Engine by ussing following commands:
   - git clone GitHub repository 
   - gcloud app deploy --project=shopping-list-235021 
   - gcloud app logs tail -s default (to view app logs)  

The app can be found online at https://shopping-list-235021.appspot.com but doesn't work properly for POST requests.
I get the following error:
   - sqlite3.OperationalError: attempt to write a readonly database.

Work in progress: 
- change writing permissions to my database
- add user authentication
