from random import choice, randint, sample
from sys import exit
# import pygame

class Pet():
    """
    """

    def __init__(self):
        """
        """

        # attributes
        self.age = randint(0, 36)
        self.belly = choice(["full", "hungry"])
        self.mood = randint(0, 10)
        self.name = input("name your thing > ")
        self.rings = randint(0, 100)
        
        # mastery attributes
        self.fly = randint(0, 10)
        self.power = randint(0, 10)
        self.run_stat = randint(0, 10)
        self.swim = randint(0, 10)

        # nature attributes
        self.intelligence = randint(0, 10)
        self.luck = randint(0, 10)
        self.stamina = randint(0, 10)

        # speech
        self.word = self.make_word()

    def get_age(self):
        """
        """

        return self.age
    
    def get_belly(self):
        """
        """

        return self.belly
    
    def get_mastery(self):
        """
        """

        return self.fly, self.power, self.run_stat, self.swim
    
    def get_mood(self):
        """
        """

        return self.mood
    
    def get_name(self):
        """
        """

        return self.name
    
    def get_nature(self):
        """
        """

        return self.intelligence, self.luck, self.stamina
    
    def get_rings(self):
        """
        """

        return self.rings
    
    def get_word(self):
        """
        """

        return self.word
    
    def make_word(self):
        """
        """

        lower = "achiopsw"
        upper = "ACHIOPSW"
        # numbers = "123456789"
        # symbols = "[]{}()*;/,._-"
        characters = lower + upper
        word_length = 4
        word = "".join(sample(characters, word_length))
        return word
    
    def set_age(self):
        """
        """

        self.age = randint(0, 36)
    
    def set_belly(self):
        """
        """

        self.belly = choice(["full", "hungry"])
    
    def set_mastery(self):
        """
        """

        self.fly = randint(0, 10)
        self.power = randint(0, 10)
        self.run_stat = randint(0, 10)
        self.swim = randint(0, 10)
    
    def set_mood(self):
        """
        """

        self.mood = randint(0, 10)
    
    def set_name(self):
        """
        """

        self.name = input("name your thing > ")
    
    def set_nature(self):
        """
        """

        self.intelligence = randint(0, 10)
        self.luck = randint(0, 10)
        self.stamina = randint(0, 10)

    
    def set_rings(self):
        """
        """

        self.rings = randint(0, 100)
    
    def set_word(self):
        """
        """

        self.word = self.make_word()
    
    def check_status(self, status):
        """
        """

        name = self.get_name()

        if status == "a":
            age = self.get_age()
            print(f"{name} is {age} months old")
        
        elif status == "b":
            belly = self.get_belly()
            print(f"{name} seems to be {belly}")
        
        elif status == "h":
            print("[a]ge, [b]elly, [ma]stery, [mo]od, [nam]e, [nat]ure, [r]ings, [s]leep, [t]houghts, or [w]hat")
        
        elif status == "ma":
            fly, power, run, swim = self.get_mastery()
            print(f"{name} can fly (level {fly}), lift (level {power}), run (level {run}), & swim (level {swim})")
        
        elif status == "mo":
            mood = self.get_mood()

            if mood <= 3:
                print(f"{name} doesn't seem too good")

            elif 3 < mood < 7:
                print(f"{name} seems okay")

            elif 6 < mood < 10:
                print(f"{name} seems to be doing good")

            else:
                print(f"{name} seems great")
        
        elif status == "nam":
            print(f"it's name is {name}")

        elif status == "nat":
            intelligence, luck, stamina = self.get_nature()
            print(f"{name} is intelligent (level {intelligence}), lucky (level {luck}), & enduring (level {stamina})")
        
        elif status == "r":
            rings = self.get_rings()
            print(f"{name} has {rings} rings")
        
        elif status == "s":
            print(f"{self.name} fell asleep")
            exit()
        
        elif status == "t":
            word = self.get_word()
            print(f"{name} says {word}")

        elif status == "w":
            print(f"{name} is a cephalopod...reptile...thing...")
        
        else:
            print("that's not an stat that can be checked")
    
    def run(self):
        """
        """

        while True:
            status = input("what would you like to check? or type h for help > ")
            self.check_status(status)

if __name__ == "__main__":
    pet = Pet()
    pet.run()
