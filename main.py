from pyscript import display 

#string 
name = "Cianna Del Prado"
display(f"Name: {name}")

#integer
age = 15
display(f"Age: {age}")

#float
height = 160.0
display(f"height: {height} cm")

# List
countries_visited = ["China", "South Korea", "Switzerland"]
countries = ", ".join(countries_visited)
display(f"Countries I want to visit: {countries}")


# Boolean
student_type = False
display(f"New student: {student_type}")


# Dictionary
student_info = {
    "color": "Pink",
    "car_brand": "Mercedes",
    "shoe_size": 7,
    "best_friend": "Mandy Cajanding"
}

display(f"Color: {student_info['color']}")
display(f"Car Brand: {student_info['car_brand']}")
display(f"Shoe Size: {student_info['shoe_size']}")
display(f"Best Friend: {student_info['Mandy Cajanding']}")


# Set
favorite_fruits = {"Mango", "Grapes", "Banana", "Strawberry", "Watermelon"}
fruits = ", ".join(favorite_fruits)
display(f"Favorite fruits: {fruits}")


# Tuple
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

week = ", ".join(days)
display(f"Days of the week: {week}")


def calculate(event):

    number1 = document.querySelector("#number1").value
    number2 = document.querySelector("#number2").value

    number1 = float(number1)
    number2 = float(number2)

    # Addition
    addition = number1 + number2

    # Subtraction
    subtraction = number1 - number2

    # Multiplication
    multiplication = number1 * number2

    # Division
    division = number1 / number2

    display(f"First Number: {number1}")
    display(f"Second Number: {number2}")
    display(f"Addition: {addition}")
    display(f"Subtraction: {subtraction}")
    display(f"Multiplication: {multiplication}")
    display(f"Division: {division}")




