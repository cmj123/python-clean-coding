### Notes
#1. Functions are separated with two line spaces
#2. Mehtods are separated with only one line space
#3. Within a method, have 1 line space between functions in the menthod
#4. Write comments
#5. After creating a class, there must be 2 lines spaces before the next piece of code
#6. 

class Person:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_data(self):
        # Printing height and weight of a person
        print("Height: ", self.height, "Weight: ", self.weight)

        # Checking height
        if self.height > 6:
            print("Too tall")
        elif self.height < 5:
            print("Too short")
        else:
            print("Perfect")


adam = Person(5.5, 150)
adam.get_data()


