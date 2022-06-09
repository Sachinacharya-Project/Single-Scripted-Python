# Reference: https://www.geeksforgeeks.org/operator-overloading-in-python/

# Overloading + operator for classes

class SpecialClass:
    def __init__(self, params: str):
        self.params = params
    def __add__(self, obj: object):
        "Overloading +"
        return self.params + " separtor-in-between " + obj.params

if __name__ == '__main__':
    obj_1 = SpecialClass("Sachin")
    obj_2 = SpecialClass("Acharya")
    print(obj_1 + obj_2) # Adding Two Object - printing out