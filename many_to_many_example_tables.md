# Many to many fields

- Usage in querying is different from what actually happens on the background.
- What happens: in between table
- Usage: INSERT queries as if there's no table in between

Or more stricly speaking:

> The ManyToManyField provides a field-like API over many-to-many fields

---

## Scenario

Store products and clients in database
Store relation between these (many to many: 1 product can be owned by multiple users, 1 user can own multiple objects)

---

## In between table

### Client

| name |
| --- |
| piet |
| henk |
| caryl |
| Mini |

### Client_product / Possession

| name_owner | name_object_owned |
|---|---|
| piet | vissenkom|
| piet | plank|

### Product

| name |
| --- |
| vissenkom |
| kast |
| plank |

---

### Peewee models

```python
# referance earlier slides for BaseModel
class Client(BaseModel):
    name = CharField(primary_key=True)

class Product(BaseModel):
    name = CharField(primary_key=True)

class Possession(BaseModel):
    name_owner = ForeignKeyField(Client, backref="owned_objects")
    name_object_owned = ForeignKeyField(Product, backref="owners")
```

---

### queries

#### INSERT queries

#### SELECT queries

```python
products_of_phil = (Product.select(Product, Possession, Client)
.join(Possession)
.join(Client)
.where(Client.name == "phil"))

for product in products_of_phil:
    print(product.name)
```

---

## Many to many field

---

### Peewee models

```python
# referance earlier slides for BaseModel
class Client(BaseModel):
    name = CharField(primary_key=True)

class Product(BaseModel):
    name = CharField(primary_key=True)
    owners = ManyToManyField(Client, backref="owned_objects")

Possession = Product.owners.get_through_model()
```

---

### Queries

#### INSERT queries

#### SELECT querries are not impacted (much)

```python
products_of_phil = (Product.select(Product, Possession, Client)
.join(Possession)
.join(Client)
.where(Client.name == "phil"))

for product in products_of_phil:
    print(product.name)
```

---

Querying the models it's almost like this is how your tables look:

### client

| name | owned_objects |
|---|----|
| piet | [vissenkom, plank] |
| henk | [] |
| caryl | [] |
| Mini | [] |

### product

| name | owners |
| --- | --- |
| vissenkom | [piet, ] |
| kast | [] |
| plank | [piet, ] |

---

### But this is not the case

The tables in the database are actually the same as in the example with the inbetween table

---
