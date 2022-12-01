from models import db, ZooKeeper, Enclosure, Animal

def print_animal_names() -> None:
    ...

def print_animal_names_in_savanna_enclosure() -> None:
    ...

def print_animal_names_in_given_enclosure(enclosure_name: str) -> None:
    ...

# query N+1
def print_animal_names_in_given_enclosure_n1(enclosure_name: str) -> None:
    ...

def main():
    db.connect()
    print("connected")

    print("\nanimal names")
    print_animal_names()
    print("\nprinting savanna names")
    print_animal_names_in_savanna_enclosure()
    print("\nprinting given enclosure names")
    print_animal_names_in_given_enclosure("jungle_enclosure")
    print("\nprinting given enclosure names")
    print_animal_names_in_given_enclosure_n1("jungle_enclosure")
    print("\nclosing")
    db.close()


if __name__ == "__main__":
    main()