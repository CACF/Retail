# Retail

# For Developers
**Prerequisites:**
- Ensure Python is installed on your computer.
- Install GitHub Desktop on your machine.

**Repository Setup:**
1. Clone the GitHub repository to your computer using GitHub Desktop.

**Command Line Instructions:**


3. Open the command prompt in the repository folder.
4. Execute the following commands:
   - pip install virtualenv
   - virtualenv venv
   - venv\Scripts\activate
   - create database in mysql
   - if you want your own configuration of datebase .you can change it from runlocal.sh

**Install Dependencies:**
5. Run the command `pip install -r requirements.txt`.

6. Execute the following commands:
   -python manage.py migrate
   -python manage.py makemigrations
**Run the Application:**
7. Execute the command `sh runLocal.sh` to start the application locally.
