#v0.0.12

from random import choice, randint, sample
from sys import exit
# import pygame
import settings as set

citron_growth = {
    "planted": 0,
    "sprouted": 18,
    "taller": 36,
    "flowering": 54,
    "berries": 72
}

default_name = {
    "egg": "amorpho egg",
    "baby": "ghastly",
    "adult": "ghost",
    "complete": "doppelganger"
}

egg_hatch_wait = randint(5140, 5396)

food = [
    "citron" # kasib berry
]

identity = [
    "clever",
    "skillful",
    "smart"
]

items = [
    "ghost gem",
    "spell tag",
    "spooky plate"
]

moves = {
    "physical": {
        "name": "phantom force", "power": 90, "accuracy": 100, "moves": 16},
    "special": {
        "name": "shadow ball", "power": 80, "accuracy": 100, "moves": 24},
    "status": {
        "name": "confuse ray", "power": 0, "accuracy": 0, "moves": 16}
}

pets = [ # pets, although these features might be incorporated in another way
    "bat",
    "half fish",
    "skeleton dog"
]

stats = { # conditional on the stage of the demon / soul / spirit
    "attack": 0,
    "defense": 0,
    "hp": 0,
    "special attack": 0,
    "special defense": 0,
    "speed": 0
}

food = {
    "food1": {"mood": +1, "speed": +24}, # green
    "food2": {"mood": +1, "flight": +24}, # purple
    "food3": {"mood": +1, "strength": +24}, # red
    "food4": {"mood": +1, "swimming": +24}, # yellow
    "food5": {
        "intelligence": +20, "flight": +40, "luck": +20, "speed": +8,
        "strength": +8, "swimming": +8
    }, # bat / black / ghost
    "food6": {
        "intelligence": +20, "flight": -16, "luck": +20, "speed": +4,
        "strength": +36, "swimming": +8
    }, # bear / power / red / roaring
    "food7": {
        "intelligence": +20, "flight": -12, "luck": +20, "speed": +32,
        "strength": +16, "swimming": -4
    }, # boar / dashing / green / run
    "food8": {
        "intelligence": +20, "flight": -8, "luck": +20, "speed": +40,
        "strength": +8, "swimming": -8
    }, # cheetah / face washing / green / run
    "food9": {
        "intelligence": +20, "flight": +60, "luck": +20, "speed": -24,
        "strength": +16, "swimming": +20
    }, # condor / flapping wings / fly / purple
    "food10": {
        "intelligence": +20, "flight": -12, "luck": +20, "speed": +32,
        "strength": +16, "swimming": -4
    }, # deer / drawing / green / run
    "food11": {
        "intelligence": +20, "flight": +4, "luck": +20, "speed": +8,
        "strength": +32, "swimming": +20
    }, # breathing fire / dragon / gold / legendary
    "food12": {
        "intelligence": +20, "flight": -16, "luck": +20, "speed": +20,
        "strength": +36, "swimming": -8
    }, # elephant / performing sit-ups / power / red
    "food13": {
        "intelligence": +20, "flight": -12, "luck": +20, "speed": +32,
        "strength": +16, "swimming": -4
    }, # gorilla / pounding chest / power / red
    "food14": {
        "intelligence": +20, "flight": 0, "luck": +20, "speed": +8,
        "strength": +24, "swimming": +32
    } # black / ghost / half fish
}

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
        self.flight = 0
        self.speed = 0
        self.strength = 0
        self.swimming = 0

        # nature attributes
        self.intelligence = 0
        self.luck = 0
        self.stamina = 0

        # speech
        self.word = self.make_word()

        # acquired habit
        self.habit = " "

        # v0.0.12
        self.ability = choice(set.ABILITIES)
    
    def check_stats(self, stat):
        """
        """

        name = self.get_name()

        stats = [
            "ab", "ag", "b", "ma", "mo", "nam", "nat", "o", "r", "t", "w"
        ]

        if stat == "ab":
            ability = self.get_ability()
            print(f"{name} has the {ability} ability")

        elif stat == "ag":
            age = self.get_age()
            self.increase_age()
            self.determine_age(age)
        
        elif stat == "b":
            belly = self.get_belly()
            print(f"{name} seems to be {belly}")
        
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
        
        elif stat == "o":
            print("[ab]ility, [ag]e, [b]elly, [ma]stery, [mo]od, [nam]e")
            print("[nat]ure, [r]ings, [t]houghts, or [w]hat")
        
        elif stat == "r":
            rings = self.get_rings()
            print(f"{name} has {rings} rings")
        
        elif stat == "t":
            word = self.get_word()
            print(f"{name} says {word}")

        elif stat == "w":
            print(f"{name} is a cephalopod...reptile...thing...")
        
        elif stat not in stats:
            print("that's not an stat that can be checked")

        else:
            print("def check_stats error")
    
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
            print("def determine_age error")
    
    def determine_mood(self, mood):
        """
        """

        if mood <= 3:
            print(f"{self.name} is not happy")

        elif 3 < mood < 7:
            print(f"{self.name} seems okay")

        elif 6 < mood < 10:
            print(f"{self.name} seems happy")

        elif mood >= 10:
            print(f"{self.name} seems excited")

        else:
            print("def determine_mood error")
    
    def feed_food(self, food):
        """
        """

        foods = [
            "avocado", "banana", "black olive", "eggplant", "kiwi",
            "red cherries", "strawberry"
        ]

        if food == "o":
            print(foods)

        elif food == "avocado":
            # food1 in settings.py
            self.mood += 1
            self.speed += 24
            print(f"mood is now {self.mood}, speed is now {self.speed}")

        elif food == "banana":
            # food4 in settings.py
            self.mood += 1
            self.swimming += 24
            print(f"mood is now {self.mood}, swimming is now {self.swimming}")
        
        elif food == "black olive":
            # food5 in settings.py
            self.intelligence += 20
            self.flight += 40
            self.luck += 20
            self.speed += 8
            self.strength += 8
            self.swimming += 8
            print(f"{self.name} is feeling spooky...")
            print(f"intelligence is now {self.intelligence}")
            print(f"flight is now {self.flight}, luck is now {self.luck}")
            print(f"speed is now {self.speed}, strenght is now {self.strength}")
            print(f"swimming is now {self.swimming}")
        
        elif food == "eggplant":
            # food2 in settings.py
            self.mood += 1
            self.flight += 24
            print(f"mood is now {self.mood}, flight is now {self.flight}")

        elif food == "kiwi":
            # food7 in setings.py
            self.intelligence += 20
            self.flight -= 12
            self.luck += 20
            self.speed += 32
            self.strength += 16
            self.swimming -= 4
            print(f"{self.name} is feeling quick, and started running around")
            self.habit = "running around"
            print(f"intelligence is now {self.intelligence}")
            print(f"flight is now {self.flight}, luck is now {self.luck}")
            print(f"speed is now {self.speed}, strenght is now {self.strength}")
            print(f"swimming is now {self.swimming}")
        
        elif food == "red cherrires":
            # food6 in settings.py
            self.intelligence += 20
            self.flight -= 16
            self.luck += 20
            self.speed += 4
            self.strength += 36
            self.swimming += 8
            print(f"{self.name} is feeling strong, and started roaring")
            self.habit = "roaring"
            print(f"intelligence is now {self.intelligence}")
            print(f"flight is now {self.flight}, luck is now {self.luck}")
            print(f"speed is now {self.speed}, strenght is now {self.strength}")
            print(f"swimming is now {self.swimming}")
        
        elif food == "strawberry":
            # food3 in settings.py
            self.mood += 1
            self.strength += 24
            print(f"mood is now {self.mood}, strength is now {self.strength}")

        elif food not in foods:
            print(f"that can't be fed to {self.name}")

        else:
            print("def feed_food error")
    
    def get_ability(self):
        """
        """

        return self.ability
    
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

        return self.flight, self.strength, self.speed, self.swim
    
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

        self.flight = 0
        self.strength = 0
        self.speed = 0
        self.swimming = 0
    
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
    
    def track_stats(self):
        """
        """

        stat_list = [
            self.flight,
            self.intelligence,
            self.luck,
            self.speed,
            self.stamina,
            self.strength,
            self.swimming
        ]

        for stat in stat_list:

            if stat >= 100:

                if stat == self.fight:
                    print("flight level increased!")

                elif stat == self.intelligence:
                    print("intellifence level increased!")

                elif stat == self.luck:
                    print("luck level increased!")

                elif stat == self.speed:
                    print("speed level increased!")

                elif stat == self.stamina:
                    print("stamina level increased!")

                elif stat == self.strength:
                    print("strength level increased!")

                elif stat == self.swimming:
                    print("swimming level increased!")

                else:
                    print("def track_stat error")
    
    def run(self):
        """
        """

        while True:
            choice = input("what would you like to do? type o for options > ")

            choices = [
                "feed", "o", "stats", "sleep"
            ]

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

            elif choice not in choices:
                print("you can't do that")

            else:
                print("def run error")

if __name__ == "__main__":
    pet = Pet()
    pet.run()
