import os 
from createDatabase import createDatabase
from fillDatabase import fillDatabase


if os.path.exists("trondelagTeater.db"):
    os.remove("trondelagTeater.db")

createDatabase()
