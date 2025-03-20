# animal.py

class Animal:
    def __init__(self, name: str, group: str, enviroment: str, skills: list):
        """
        Initialize an Animal object with its name, group, number of legs, and skills.
        """
        self.name = name
        self.group = group
        self.enviroment = enviroment 
        self.skills = skills

    def __str__(self):
        """
        Return a string representation of the Animal object.
        """
        return f"Animal(Name: {self.name}, Group: {self.group}, Legs: {self.enviroment}, Skills: {', '.join(self.skills)})"


# Creating instances of the Animal class
animals = [
    Animal('Cat', 'Mammals', 'land' , ['jumping', 'climbing', 'hunting']),
    Animal('Eagle', 'Birds', 'sky', ['flying', 'hunting', 'sharp vision']),
    Animal('Frog', 'Amphibians', 'land', ['jumping', 'swimming']),
    Animal('Shark', 'Fish', 'sea', ['swimming', 'hunting']),
    Animal('Snake', 'Reptiles', 'land', ['slithering', 'camouflage'])
]

# Printing all animals
for animal in animals:
    print(animal)
