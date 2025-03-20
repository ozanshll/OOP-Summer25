# animal.py

class Animal:
    def __init__(self, name: str, group: str, number_of_legs: int, skills: list):
        """
        Initialize an Animal object with its name, group, number of legs, and skills.
        """
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __str__(self):
        """
        Return a string representation of the Animal object.
        """
        return f"Animal(Name: {self.name}, Group: {self.group}, Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)})"


# Creating instances of the Animal class
animals = [
    Animal('Cat', 'Mammals', 4, ['jumping', 'climbing', 'hunting']),
    Animal('Eagle', 'Birds', 2, ['flying', 'hunting', 'sharp vision']),
    Animal('Frog', 'Amphibians', 4, ['jumping', 'swimming']),
    Animal('Shark', 'Fish', 0, ['swimming', 'hunting']),
    Animal('Snake', 'Reptiles', 0, ['slithering', 'camouflage'])
]

# Printing all animals
for animal in animals:
    print(animal)
