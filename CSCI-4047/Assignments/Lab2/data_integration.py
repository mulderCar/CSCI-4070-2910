#File Name data_integration.py

## This is to import SQL Alchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_model import Base, Pokemon

# set up the db session
SQLALCHEMY_DATABASE_URL = "sqlite:///./Assignments/Lab2/lab_data.db"  # Update with your file name
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# bind the ORM to our classes
Base.metadata.create_all(bind=engine)

# Session to interact with the db
Session = sessionmaker(bind=engine)
session = Session()

# Create Function
def create_pokemon(dex_number, name, form, type1, type2, total, hp, attack, defense, special_attack, special_defense, speed, generation):
    new_pokemon = Pokemon(
        DexNumber=dex_number, Name=name, Form=form, Type1=type1, Type2=type2,
        Total=total, HP=hp, Attack=attack, Defense=defense, SpecialAttack=special_attack,
        SpecialDefense=special_defense, Speed=speed, Generation=generation
    )
    session.add(new_pokemon)
    session.commit()
    print(f"{name} added successfully.")

def read_pokemon(by, value):
    if by == 'id':
        result = session.query(Pokemon).filter_by(Id=value).first()
    elif by == 'dexnumber':
        result = session.query(Pokemon).filter_by(DexNumber=value).first()
    elif by == 'name':
        result = session.query(Pokemon).filter_by(Name=value).first()
    elif by == 'type':
        result = session.query(Pokemon).filter((Pokemon.Type1 == value) | (Pokemon.Type2 == value)).all()
    elif by == 'generation':
        result = session.query(Pokemon).filter_by(Generation=value).all()
    else:
        print("Invalid search criteria.")
        return None

    if result:
        print("Results found.")
        return result  # Make sure to return results to be handled in the menu
    else:
        print("No results found.")
        return None

# Update Function
def update_pokemon(id, name=None, dex_number=None, form=None, type1=None, type2=None,
                    total=None, hp=None, attack=None, defense=None, special_attack=None,
                    special_defense=None, speed=None, generation=None):
    pokemon = session.query(Pokemon).filter_by(Id=id).first()
    if pokemon:
        if name is not None: pokemon.Name = name
        if dex_number is not None: pokemon.DexNumber = dex_number
        if form is not None: pokemon.Form = form
        if type1 is not None: pokemon.Type1 = type1
        if type2 is not None: pokemon.Type2 = type2
        if total is not None: pokemon.Total = total
        if hp is not None: pokemon.HP = hp
        if attack is not None: pokemon.Attack = attack
        if defense is not None: pokemon.Defense = defense
        if special_attack is not None: pokemon.SpecialAttack = special_attack
        if special_defense is not None: pokemon.SpecialDefense = special_defense
        if speed is not None: pokemon.Speed = speed
        if generation is not None: pokemon.Generation = generation
        session.commit()
        print(f"Pokemon with ID {id} updated successfully.")
    else:
        print("Pokemon not found.")

# Delete Function
def delete_pokemon(id):
    pokemon = session.query(Pokemon).filter_by(Id=id).first()
    if pokemon:
        confirmation = input(f"Are you sure you want to delete {pokemon.Name}? (yes/no): ")
        if confirmation.lower() == 'yes':
            session.delete(pokemon)
            session.commit()
            print(f"Pokemon with ID {id} deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Pokemon not found.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Create Pokemon")
        print("2. Read Pokemon")
        print("3. Update Pokemon")
        print("4. Delete Pokemon")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dex_number = int(input("Enter Dex Number: "))
            name = input("Enter Name: ")
            form = input("Enter Form: ")
            type1 = input("Enter Type 1: ")
            type2 = input("Enter Type 2 (leave blank if none): ")
            total = int(input("Enter Total: "))
            hp = int(input("Enter HP: "))
            attack = int(input("Enter Attack: "))
            defense = int(input("Enter Defense: "))
            special_attack = int(input("Enter Special Attack: "))
            special_defense = int(input("Enter Special Defense: "))
            speed = int(input("Enter Speed: "))
            generation = int(input("Enter Generation: "))
            create_pokemon(dex_number, name, form, type1, type2 or None, total, hp, attack, defense, special_attack, special_defense, speed, generation)

        elif choice == '2':
            by = input("Find by (Id/DexNumber/Name/Type/Generation): ").lower()
            value = input("Enter value: ")
            result = read_pokemon(by, value)
            if result:
                if isinstance(result, list):  # If we get multiple results, print them all
                    for item in result:
                        print(f"ID: {item.Id}, Dex Number: {item.DexNumber}, Name: {item.Name}, Form: {item.Form}, Type1: {item.Type1}, Type2: {item.Type2}, Total: {item.Total}, HP: {item.HP}, Attack: {item.Attack}, Defense: {item.Defense}, Special Attack: {item.SpecialAttack}, Special Defense: {item.SpecialDefense}, Speed: {item.Speed}, Generation: {item.Generation}")
                else:  # If we get a single result, print it
                    print(f"ID: {result.Id}, Dex Number: {result.DexNumber}, Name: {result.Name}, Form: {result.Form}, Type1: {result.Type1}, Type2: {result.Type2}, Total: {result.Total}, HP: {result.HP}, Attack: {result.Attack}, Defense: {result.Defense}, Special Attack: {result.SpecialAttack}, Special Defense: {result.SpecialDefense}, Speed: {result.Speed}, Generation: {result.Generation}")
            else:
                print("No Pokémon found.")

        elif choice == '3':
            id = int(input("Enter ID to update: "))
            name = input("Enter new Name (leave blank to keep unchanged): ")
            dex_number = input("Enter new Dex Number (leave blank to keep unchanged): ")
            form = input("Enter new Form (leave blank to keep unchanged): ")
            type1 = input("Enter new Type 1 (leave blank to keep unchanged): ")
            type2 = input("Enter new Type 2 (leave blank to keep unchanged): ")
            total = input("Enter new Total (leave blank to keep unchanged): ")
            hp = input("Enter new HP (leave blank to keep unchanged): ")
            attack = input("Enter new Attack (leave blank to keep unchanged): ")
            defense = input("Enter new Defense (leave blank to keep unchanged): ")
            special_attack = input("Enter new Special Attack (leave blank to keep unchanged): ")
            special_defense = input("Enter new Special Defense (leave blank to keep unchanged): ")
            speed = input("Enter new Speed (leave blank to keep unchanged): ")
            generation = input("Enter new Generation (leave blank to keep unchanged): ")
            update_pokemon(
                id, name if name else None, int(dex_number) if dex_number else None, form if form else None,
                type1 if type1 else None, type2 if type2 else None, int(total) if total else None,
                int(hp) if hp else None, int(attack) if attack else None, int(defense) if defense else None,
                int(special_attack) if special_attack else None, int(special_defense) if special_defense else None,
                int(speed) if speed else None, int(generation) if generation else None
            )

        elif choice == '4':
            id = int(input("Enter ID to delete: "))
            delete_pokemon(id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()