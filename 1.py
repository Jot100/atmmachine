class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    # Mutator methods
    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_animal_type):
        self.__animal_type = new_animal_type

    def set_age(self, new_age):
        self.__age = new_age


# Program to create a Pet object and prompt user for input
def main():
    # Prompt user for pet information
    pet_name = input("Enter the name of your pet: ")
    pet_type = input("Enter the type of your pet (e.g., Dog, Cat, Bird): ")
    pet_age = int(input("Enter the age of your pet: "))

    # Create a Pet object
    my_pet = Pet(pet_name, pet_type, pet_age)

    # Display pet information using accessor methods
    print("\nPet Information:")
    print("Name:", my_pet.get_name())
    print("Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())

    # Prompt user to update pet information
    new_name = input("\nEnter a new name for your pet: ")
    my_pet.set_name(new_name)

    new_type = input("Enter a new type for your pet: ")
    my_pet.set_animal_type(new_type)

    new_age = int(input("Enter a new age for your pet: "))
    my_pet.set_age(new_age)

    # Display updated pet information
    print("\nUpdated Pet Information:")
    print("Name:", my_pet.get_name())
    print("Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())


# Run the program
if __name__ == "__main__":
    main()
