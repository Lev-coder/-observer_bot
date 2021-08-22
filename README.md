# observer_bot
this program allows you to watch some file on the Internet

if the file has been changed, then the bot will inform you about it (but the message will not come to you immediately after changing the file)

this program checks the document (resource) at regular intervals.

## How to start this bot ?

I used [MySQL](https://www.mysql.com/) for this project, so you will need to run it on your computer


if you need to change the parameters of the connection to the database, then go to the file
database/Database.py
```python
class Database:
    _databaseName = "TheDatabase"
    _host = "localhost"
    _user = "root"
    _password = ""
    ...
```
you will need to create a file config.py and create a variable TOKEN in file config.py

after that you will need to set the token you received from [@BotFather](https://t.me/botfather)

you should get something like this
```python
TOKEN = "fdsfstl4kgklf_magic_symbols_lmldmflsmorf"
```
go to the folder with the project

use this command
```bash
python main.py
```
at this point the program should work

### Technologies

Windows 10 ( if you are using Linux you may have problems with venv )

MySQL 5


