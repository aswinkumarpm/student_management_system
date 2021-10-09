# student_management_system
Clone The Repository. Github Link: https://github.com/aswinkumarpm/student_management_system
Create a virtual Enviornment for python3 and Using upgraded version of Pip,  install the requirements using the requirements.txt.

Create a Super User using python manage.py createsuperuser command
and then run the server.

Go to the Admin Panel ,http://127.0.0.1:8000/admin/login/?next=/admin/ and login with username : 'admin', password: 'q'. or you can use yourown created Admin username and password.


Run the server using python manage.py runserver
Go to the URL: http://127.0.0.1:8000/api/v1/students/

It will display the django restframework with list of students and also we can create the student in a same form.

The Other URL for creating the student : http://127.0.0.1:8000/api/v1/students/create/

Go to the URL: http://127.0.0.1:8000/api/v1/students/marks/
It will display the student marks.


The Other URL for creating the student marks  : http://127.0.0.1:8000/api/v1/students/marks/create/. In postman pass the existing student id to create student marks for particular student id.

To show a student details, go to this URL: http://127.0.0.1:8000/api/v1/students/1/. We can edit the details in a form in the bottom section.


The delete button is on the top right side to delete particular student details.



To show a student mark, go to this URL: http://127.0.0.1:8000/api/v1/students/marks/1/. We can edit the details in a form in the bottom section.

The delete button is on the top right side to delete particular student mark details.




















