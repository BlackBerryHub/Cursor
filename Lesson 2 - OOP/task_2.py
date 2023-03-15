"""
Create regular class taking 8 params on init - name, last_name, phone_number,
address, email, birthday, age, sex
Override a printable string representation of Profile class and return:
list of the params mentioned above
"""


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex) :
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        # keys() for params, values() for values in this params, items() for tuples
        return str(list(self.__dict__.items()))


profile = Profile("Marat", "Khusnutdinov", "0663549312", "Lviv, Lukasha 4", "blackberry4800@gmail.com", "25.01.2000",
                  "23", "Male")
print(profile)
