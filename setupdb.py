from models import (db, ZooKeeper, Enclosure, Animal)
import os

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "zoo.db")
    if os.path.exists(database_path):
        os.remove(database_path)

def populate_test_data():
    db.connect()

    db.create_tables(
        [
            ZooKeeper,
            Enclosure,
            Animal
        ]
    )
    zoo_keepers = ["Aidan", "Sharon", "Bob"]
    enclosures = [["barrel", 2], ["desert_enclosure", 1], ["savanna_enclosure", 2], ["jungle_enclosure", 2], ["jungle_enclosure", 2]]
    animals = [["phil", "meerkat", 2], ["wendy", "meerkat", 2], ["simon", "meerkat", 4], ["johny", "tiger", 3], ["bob", "snake", 4], ["carly", "parrot", 5]]