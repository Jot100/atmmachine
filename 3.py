class PersonalInformation:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    # Mutator methods
    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, new_address):
        self.__address = new_address

    def set_age(self, new_age):
        self.__age = new_age

    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number


# Program to create instances of the PersonalInformation class
def main():
    # Create an instance for your information
    my_info = PersonalInformation("Your Name", "Your Address", 25, "123-456-7890")

    # Create two instances for friends/family members
    friend1_info = PersonalInformation("Friend" )
