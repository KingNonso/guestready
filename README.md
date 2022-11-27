# GuestReady

## Python Version
python == 3.9.5 

## Django Version
django == 4.1.3 

### Code Formatter: Black
### Static Type Checking: Mypy


## Setting up the project
* Make sure you have git, pip and virtualenv installed
* Clone the git repo by running `git clone git@github.com:KingNonso/guestready.git`
* run `virtualenv env` to create a new virtual environment
* activate env by running `source env/bin/activate` or  `env/scripts/activate` for windows
* run `pip install -r requirements.txt` to install all required app extensions

### Database
For the ease of setting up... I used sqlite3. Just to keep things simple (never use in prod).

* run `python manage.py migrate` to create the database tables
* run `python manage.py loaddata rental/fixtures/rentals.json` to install fixtures to db
* run `python manage.py test --no-input --keepdb` to run tests
