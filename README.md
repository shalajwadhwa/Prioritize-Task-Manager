# Prioritize Task Manager
Easily organize Tasks using Prioritize.  
[Try Out Prioritize](https://shalajwadhwa.eu.pythonanywhere.com)

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Contributing Guidelines](#contributing-guidelines)
* [Sources](#sources)

## General Info
Prioritize is a Flask app that works on the principle of the Eisenhower Matrix. Inspired by the classic To-do app, Prioritize segregates tasks by asking users if their task is important/urgent. Prioritize is a basic app and is created for beginners to learn and experiment with Flask.

## Technologies
* Python 3.9
* SQLite
* Flask
* Bootstrap 5

## Setup
* [Windows](#steps-for-windows)
* [Linux](#steps-for-linux)

### Steps for Windows:
1. Download and install Python 3.9 (https://www.python.org/)  
(Make sure to select 'add Python to Path' during installation)

2. Install virtualenv
```
pip install virtualenv
```

3. Open source code in Command Prompt
```
cd 'enter folder location here'
```

4. Setup the Virtual Environment  
(we are naming it 'env' in this example)
```
virtualenv env
```

5. Activate the Virtual Environment
```
env/Scripts/activate
```

6. Install the requirements
```
pip install -r requirements.txt
```

7. Create the SQLite database
```
python
```
```
from app.models import db
```
```
db.create_all()
```
```
exit()
```

8. Run the app
```
python run.py
```

### Steps for Linux:
1. Same steps as for [Windows](#steps-for-windows) except for step number 5.  
Use the following for step 5
```
source env/bin/activate
```

## Contributing Guidelines
Feel free to contribute!

## Sources
Bootstrap : https://getbootstrap.com/  

DiceBear (used for favicon and user profiles) : https://avatars.dicebear.com/
