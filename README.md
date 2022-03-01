# python-hangman

CLI hangman. You can save your progress mid-game and access it later using a six digit code.

After you start, write letters one by one, you cannot write the whole word.

Game can be stopped using the "stop" command, but the progress won't save

tl;dl: "help" command is your friend

# Prerequisities

- Python 3
- MongoDB
- pymongo package from pip

# Running

1. Run MongoDB
```shell
mongod
```

2. Import the hangman pictures and example words to the DB using MongoDB Compass
   1. Create hangman database
   2. Import the words.json to words collection
   3. Import the versions.json to versions collection

3. Start the app
```shell
python3 main.py
```
