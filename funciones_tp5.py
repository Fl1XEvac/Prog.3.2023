import pytest
#Ejercicio 1
def num_dni(dni):
    if dni > 9999999:
        return True
    else:
        return False

#Ejercicio 2

def last_word(phrase):
    phrase_list=phrase.split()
    how_long= phrase_list[-1]
    return len(how_long)

#Ejercicio 3

def num_dni1(dni1):
    dni1 = int(dni1)
    if dni1 > 999999:
        return True
    else:
        return False

def partherid(first_name, second_name, last_name, dni1):
    int(dni1)
    letters_in_lastname= str(len(last_name))
    partherid= str(first_name.title() + letters_in_lastname + dni1[0:2])
    return partherid

#Ejercicio 4

def multiple(num,num1):
    if num % num1 == 0:
        return True
    elif num1 % num == 0:
        return True
    else:
        return False

#Ejercicio 5

def temperature(temperature_min, temperature_max):
    temperature_mid= ((temperature_max + temperature_min)/2)
    return temperature_mid

#Ejercicio 6

def add_space_after_letters(text):
    result = ""
    for letter in text:
        result += letter + " "
    return result

#Ejercicio 7

def find_max_and_min(numbers):
    if not numbers:
        return None, None
    maximum = minimum = numbers[0]
    for value in numbers:
        if value > maximum:
            maximum = value
        elif value < minimum:
            minimum = value
    return maximum, minimum

#Ejercicio 8

def calculate_circle_area_and_perimeter(radius):
    area = 3.14 * radius**2  
    
    perimeter = 2 * 3.14 * radius
    
    return area, perimeter

#Ejercicio 9

def login(user, password):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
            return False

#Ejercicio 10

def apply_discount(cart, discounts):
    total_price = 0
    
    for product, price in cart.items():
        if product in discounts:
            discount = discounts[product]
            discounted_price = price * (1 - discount / 100)
            total_price += discounted_price
        else:
            total_price += price
    
    return total_price

#Ejercicio 11

def apply_function(func, lst):
    result= []
    for item in lst:
        result.append(func(item))
    return result

def add_one(number):
    return number + 1

#Ejercicio 12

def count_word_lengths(phrase):
    words = phrase.split()
    word_lengths = {}
    
    for word in words:
        word_lengths[word] = len(word)
    
    return word_lengths

#Ejercicio 13

def calculate_vector_magnitude(x, y):
    magnitude = (x**2 + y**2)**0.5
    return magnitude

#Ejercicio 14

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

#Ejercicio 15

def factorial(number):
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

#Ejercicio 16

def calculate_frequency(number, digit):
    number_str = str(number)
    count = 0
    
    for d in number_str:
        if d == digit:
            count += 1
    
    return count

#Ejercicio 17

def factorial_range(number):
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

def is_prime1(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_digits(number):
    plus = 0
    while number > 0:
        digit = number % 10
        plus += digit
        number //= 10
    return plus





