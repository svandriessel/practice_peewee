from peewee import Model, SqliteDatabase, CharField, ForeignKeyField, ManyToManyField

db = SqliteDatabase("zoo.db")

class BaseModel(Model):
    class Meta:
        database = db

class ZooKeeper(BaseModel):
    name = CharField()

class Enclosure(BaseModel):
    name = CharField()
    feeder = ForeignKeyField(ZooKeeper, backref="enclosures_to_feed")

class Animal(BaseModel):
    name = CharField()
    type = CharField()
    enclosure = ForeignKeyField(Enclosure, backref="animals")

class Photo(BaseModel):
    name = CharField()
    captured_animals = ManyToManyField(Animal, backref="photos_captured_on")

PhotoCapturedAnimal = Photo.captured_animals.get_through_model() #photo_animal_trough