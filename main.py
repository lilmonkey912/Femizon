
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

app = create_app() # we initialize our flask app using the __init__.py 

if __name__ == '__main__':
  with app.app_context():
        db.create_all()
  app.run(host='0.0.0.0',port=8080, debug = True)
  
