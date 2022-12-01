from models import (db, ZooKeeper, Enclosure, Animal, Photo, PhotoCapturedAnimal)
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
            Animal,
            Photo,
            PhotoCapturedAnimal
        ]
    )
    zoo_keepers = ["Aidan", "Sharon", "Bob"]
    enclosures = [["barrel", 2], ["desert_enclosure", 1], ["savanna_enclosure", 2], ["jungle_enclosure", 2], ["jungle_enclosure", 2]]
    animals = [["phil", "meerkat", 2], ["wendy", "meerkat", 2], ["simon", "meerkat", 4], ["johny", "tiger", 3], ["bob", "snake", 4], ["carly", "parrot", 5]]

    for person_name in zoo_keepers:
        ZooKeeper.create(name = person_name)
        # alternatively
        # zookeeper = ZooKeeper(name = person_name)
        # zookeeper.save()
    
    for enclosure in enclosures:
        Enclosure.create(name = enclosure[0], feeder = enclosure[1])
    
    for animal in animals:
        wendy = Animal.create(name = animal[0], type=animal[1], enclosure=animal[2])


    photos_captured_animals = [["wendy", "phil"]]

    for captured_animal_list in photos_captured_animals:
        photo = Photo.create(name = "photo1")
        
        for captured_animal_name in captured_animal_list:
            animal = Animal.get(Animal.name == captured_animal_name)
            photo.captured_animals.add(animal)
