# lect10-db

1. Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`  
    Enter yes to all prompts.  
2. Initialize PSQL database: `sudo service postgresql initdb`  
3. Start PSQL: `sudo service postgresql start`  
2. Make a new superuser: `sudo -u postgres createuser --superuser $USER`  
    If you get an error saying "could not change directory", that's okay! It worked!
3. Make a new database: `sudo -u postgres createdb $USER`  
        If you get an error saying "could not change directory", that's okay! It worked!
4. Make sure your user shows up:  
    a) `psql`  
    b) `\du` look for ec2-user as a user  
    c) `\l` look for ec2-user as a database  
5. Make a new user:  
    a) `psql` (if you already quit out of psql)  
    b) Type this with a new unique password: `create user some_username_here superuser password 'some_unique_new_password_here';`  
    c) `\q` to quit out of sql  
