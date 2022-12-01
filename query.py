from models import db, ZooKeeper, Enclosure, Animal, Photo, PhotoCapturedAnimal
from peewee import JOIN

def join_trough_many_to_many():

    # photos_with_phil = (Photo.select(Photo, PhotoCapturedAnimal, Animal)
    # .join(PhotoCapturedAnimal)
    # .join(Animal)
    # .where(Animal.name == "phil"))
    
    # for photo in photos_with_phil:
    #     print(photo.name)

    photos_with_phil = (Photo.select(Photo, PhotoCapturedAnimal, Animal)
    .where(Animal.name == "phil"))
    
    for photo in photos_with_phil:
        print(photo.name)

def main():
    db.connect()
    print("connected")

    join_trough_many_to_many()
    print("\nclosing")

    db.close()


if __name__ == "__main__":
    main()