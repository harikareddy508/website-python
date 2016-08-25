==================================================================
STEPS TO RUN APPLICATION
==================================================================

1) Run pip install -r requirements.txt
2) If you want to start with clean database
    a) open python shell in project directory
    b) execute 'from app import db'
    c) execute 'db.create_all()', which will create neccessary tables and db files
3) After setting up database run 'python app.py': It will have application ready, which can be accessed at
    http://localhost:5000


IMPORTANT NOTES:
1) Instead of providing explicit search button I provide search box which will search persons with description,
       I implemented it more like instant search


DESIGN DECISIONS:
1) It is always very important to design your application separating front end and backend completely. So, we can use
    same set of services for web and also mobile applications.
2) I used Python as the language because of it's simplicity
3) I believe in designing beautiful interfaces!!