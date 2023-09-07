import enum

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 4
    
color = Color.RED
print(color)
print(color.name)
print(color.value)
