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
        self.age = 0
        self.belly = choice(["full", "hungry"])
        self.mood = 0
        self.name = input("name your thing > ")
        self.rings = randint(0, 100)
        
        # mastery attributes
        self.fly = 0
        self.power = 0
        self.speed = 0
        self.swim = 0

        # nature attributes
        self.intelligence = 0
        self.luck = 0
        self.stamina = 0

        # speech
        self.word = self.make_word()
    
    def determine_age(self, age):
        """
        """

        if age <= 12:
            print(f"{self.name} is less than a year old")

        elif 12 < age <= 24:
            print(f"{self.name} is 1 year old")

        elif 24 < age <= 36:
            print(f"{self.name} is 2 years old")

        else:
            print("error")
    
    def determine_mood(self, mood):
        """
        """

        if mood <= 3:
            print(f"{self.name} is not happy")

        elif 3 < mood < 7:
            print(f"{self.name} seems okay")

        elif 6 < mood < 10:
            print(f"{self.name} seems happy")

        else:
            print(f"{self.name} seems excited")
    
    def feed_food(self, food):
        """
        """

        if food == "o":
            print("avocado, banana, eggplant, strawberry")

        elif food == "avocado":
            self.mood += 1
            self.speed += 24
            print(f"mood is now {self.mood}, speed is now {self.speed}")

        elif food == "banana":
            self.mood += 1
            self.swimming += 24
            print(f"mood is now {self.mood}, swimming is now {self.swimming}")
        
        elif food == "eggplant":
            self.mood += 1
            self.flight += 24
            print(f"mood is now {self.mood}, flight is now {self.flight}")

        elif food == "strawberry":
            self.mood += 1
            self.strength += 24
            print(f"mood is now {self.mood}, strength is now {self.strength}")
    
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

        return self.fly, self.power, self.speed, self.swim
    
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
    
    def increase_age(self):
        """
        """

        self.age += 1
        if self.age == 37:
            print(f"{self.name} has died")
            exit()
    
    def make_word(self):
        """
        """

        lower = "achiopsw"
        upper = "ACHIOPSW"
        characters = lower + upper
        word_length = 4
        word = "".join(sample(characters, word_length))
        return word
    
    def set_age(self):
        """
        """

        self.age = 0
    
    def set_belly(self):
        """
        """

        self.belly = choice(["full", "hungry"])
    
    def set_mastery(self):
        """
        """

        self.fly = 0
        self.power = 0
        self.speed = 0
        self.swim = 0
    
    def set_mood(self):
        """
        """

        self.mood = 0
    
    def set_name(self):
        """
        """

        self.name = input("name your thing > ")
    
    def set_nature(self):
        """
        """

        self.intelligence = 0
        self.luck = 0
        self.stamina = 0

    
    def set_rings(self):
        """
        """

        self.rings = randint(0, 100)
    
    def set_word(self):
        """
        """

        self.word = self.make_word()
    
    def check_stats(self, stat):
        """
        """

        name = self.get_name()

        if stat == "a":
            age = self.get_age()
            self.increase_age()
            self.determine_age(age)
        
        elif stat == "b":
            belly = self.get_belly()
            print(f"{name} seems to be {belly}")
        
        elif stat == "h":
            print("[a]ge, [b]elly, [ma]stery, [mo]od, [nam]e, [nat]ure, [r]ings, [t]houghts, or [w]hat")
        
        elif stat == "ma":
            fly, power, run, swim = self.get_mastery()
            print(f"{name} can fly (level {fly}), lift (level {power}), run (level {run}), & swim (level {swim})")
        
        elif stat == "mo":
            mood = self.get_mood()
            self.determine_mood(mood)
        
        elif stat == "nam":
            print(f"it's name is {name}")

        elif stat == "nat":
            intelligence, luck, stamina = self.get_nature()
            print(f"{name} is intelligent (level {intelligence}), lucky (level {luck}), & enduring (level {stamina})")
        
        elif stat == "r":
            rings = self.get_rings()
            print(f"{name} has {rings} rings")
        
        elif stat == "t":
            word = self.get_word()
            print(f"{name} says {word}")

        elif stat == "w":
            print(f"{name} is a cephalopod...reptile...thing...")
        
        else:
            print("that's not an stat that can be checked")
    
    def run(self):
        """
        """

        while True:
            choice = input("what would you like to do? type o for options > ")

            if choice == "feed":
                food = input("what would you like to feed it? type o for options > ")
                self.feed_food(food)

            elif choice == "o":
                print("check is [stats], [feed] it food, or put it to [sleep]")
            
            elif choice == "stats":
                stat = input("what would you like to check? type o for options > ")
                self.check_stats(stat)

            elif choice == "sleep":
                print(f"{self.name} fell asleep")
                exit()

            else:
                print("you can't do that")

if __name__ == "__main__":
    pet = Pet()
    pet.run()
