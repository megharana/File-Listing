# Follow below steps for setting up the web application

- Clone the code using command <git clone https://github.com/megharana/File-Listing.git>

- Go to the "File-Listing" folder.

- navigate to the File-Listing folder in Terminal

- setup virtual directory using command <python3 -m venv /path/to/new/virtual/environment>

- Set up Database:

  - Open mysql workbench.
  - make mysql connection with following credentials:
  - Hostname: 127.0.0.1
  - Port: 3306
  - Username: root
  - Password: Set any desired Password

  - create a schema with a name "media"

* activate virtual Environment using command : <source venv/bin/activate> in terminal or <C:\Users\suryav> \venv\Scripts\activate> in cmd  
  (reference :https://docs.python-guide.org/dev/virtualenvs/)

* Use this command <pip install -r requirements.txt> -- to install all python packages needed

* open "medialisting/medialisting/settings.py" and in 79th line set Password which was set during DB setup for Mysql connection.

* traverse upto "File-Listing/medialisting" folder in terminal or in cmd
* Run following commands:

  - python manage.py makemigrations
  - python manage.py makemigrations fileupload
  - python manage.py migrate

  - python manage.py runserver -- for actiavting server

* navigate to following url : <http://127.0.0.1:8000/upload/> to view the page
* please find the screenshot in screenshot folder
