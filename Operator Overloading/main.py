# Reference: https://www.geeksforgeeks.org/operator-overloading-in-python/

# Overloading + operator for classes

class SpecialClass:
    def __init__(self, params: str):
        self.params = params
    def __add__(self, obj: object):
        "Overloading +"
        return self.params + " separtor-in-between " + obj.params
    def __mul__(self, obj: object):
        "Overloading * (multiplication)"
        return "Combined: " + self.params + obj.params if not self.params in obj.params else "Single: " + self.params

if __name__ == '__main__':
    obj_1 = SpecialClass("Sachin")
    obj_2 = SpecialClass("Acharya")
    print(obj_1 + obj_2) # Adding Two Object - printing out

    # Checking Condition one
    print(obj_1 * obj_2) # Not

    obj_1 = SpecialClass("Sachin")
    obj_2 = SpecialClass("Sachin")
    
    # Equal
    print(obj_1 * obj_2)