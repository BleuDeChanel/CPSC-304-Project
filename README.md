# CPSC-304-Project : Tennis ClubMembership

Once you pull the starter file,
1) Go to the directory where manage.py file is in. (...\CPSC-304-Project\tennis_club_app\project)
2) Type pip install psycopg2 on shell/terminal
3) Type python manage.py inspectdb
4) You should see all tables


Run local server with:
python3 manage.py runserver

# To view models using admin tool:
1) Start local sever
2) http://127.0.0.1:8000/admin/ in your browser
3) Use the login Mark provided.

User : cpsc304admin
Pass : DBsAreEasy

# Apply database changes with:
python3 manage.py makemigrations

python3 manage.py migrate




Notes:
After running python manage.py inspectdb it gave an auto generated models module. So I put this into the tenniscenter app.
The command also gave these instructions:
 This is an auto-generated Django model module.
 You'll have to do the following manually to clean this up:
   * Rearrange models' order
   * Make sure each model has one field with primary_key=True
   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
 Feel free to rename the models, but don't rename db_table values or field names.

For references,

Read part 2 to 5
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

Making queries in django
https://docs.djangoproject.com/en/2.0/topics/db/queries/
