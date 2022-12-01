from peewee import Model, SqliteDatabase, CharField, ForeignKeyField

db = SqliteDatabase("zoo.db")

class BaseModel(Model):
    class Meta:
        database = db

class ZooKeeper(BaseModel):
    ...

class Enclosure(BaseModel):
    ...
class Animal(BaseModel):
    ...
