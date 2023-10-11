import pytest
from funciones_tp5 import *
#Ejercicio 1
@pytest.mark.parametrize("dni, res", [
    (45532464, True),
    (4553245, False),
    (12345678, True)
])
def test_num_dni(dni, res):
    assert num_dni(dni) == res

#Ejercicio 2

@pytest.mark.parametrize("phrase, res", [
    ("A barata eu josuke higashikata", 11)
])
def test_last_word(phrase, res):
    assert last_word(phrase) == res

#Ejercicio 3

@pytest.mark.parametrize("dni, res", [
    ("45532464", True),
    ("45532456", True),
    ("12345678", True)
])
def test_num_dni1(dni,res):
    assert num_dni1(dni) == res

@pytest.mark.parametrize("first_name, second_name, last_name, dni1, res", [
    ("Ulises", "Nicolas", "Jimenez", "45532464", "Ulises745")
])
def test_partherid(first_name, second_name, last_name, dni1, res):
    assert partherid(first_name, second_name, last_name, dni1) == res

#Ejercicio 4

@pytest.mark.parametrize("num, num1, res",[
    (4, 2, True),
    (7, 8, False),
    (5, 10, True)
])
def test_multiple(num, num1, res):
    assert multiple(num,num1) == res

#Ejercicio 5

@pytest.mark.parametrize("temperature_max, temperature_min, res",[
    (25, 10, 17.5),
])
def test_temperature(temperature_max, temperature_min, res):
    assert temperature(temperature_max, temperature_min) == res

#Ejercicio 6

@pytest.mark.parametrize("text, res",[
    ("hola", "h o l a ")
])
def test_add_space_after_letters(text, res):
    assert add_space_after_letters(text) == res

#Ejercicio 7

def test_find_max_and_min():
    result = find_max_and_min([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    assert result == (9, 1)

#Ejercicio 8

def test_calculate_circle_area_and_perimeter():
    result = calculate_circle_area_and_perimeter(7)
    res_area = 153.86  
    res_perimeter = 43.96  
    assert result == (res_area, res_perimeter)

#Ejercicio 9

@pytest.mark.parametrize("user, password, res",[
    ("usuario1", "asdasd", True)
])
def test_login(user, password, res):
    assert login(user, password) == res

#Ejercicio 10

def test_apply_discount():
    cart = {}
    discounts = {}
    result = apply_discount(cart, discounts)
    assert result == 0  

    cart = {'producto1': 10, 'producto2': 20, 'producto3': 30}
    discounts = {}
    result = apply_discount(cart, discounts)
    assert result == 60  

    cart = {'producto1': 10, 'producto2': 20, 'producto3': 30}
    discounts = {'producto1': 10, 'producto3': 20}
    result = apply_discount(cart, discounts)
    assert result == 53.0  

#Ejercicio 11

def test_apply_function():
    lst = [1, 2, 3, 4, 5]
    result = apply_function(add_one, lst)
    expected_result = [2, 3, 4, 5, 6]
    assert result == expected_result

    lst = []
    result = apply_function(add_one, lst)
    expected_result = []
    assert result == expected_result

    def double_value(number):
        return number * 2
    lst = [2, 4, 6, 8, 10]
    result = apply_function(double_value, lst)
    expected_result = [4, 8, 12, 16, 20]
    assert result == expected_result

#Ejercicio 12

def test_count_word_lengths():
    phrase = "Esto es una prueba"
    result = count_word_lengths(phrase)
    expected_result = {'Esto': 4, 'es': 2, 'una': 3, 'prueba': 6}
    assert result == expected_result

    phrase = ""
    result = count_word_lengths(phrase)
    expected_result = {}
    assert result == expected_result

    phrase = "Python es genial y Python es poderoso"
    result = count_word_lengths(phrase)
    expected_result = {'Python': 6, 'es': 2, 'genial': 6, 'y': 1, 'poderoso': 8}
    assert result == expected_result

#Ejercicio 13

def test_calculate_vector_magnitude():
    x = 3
    y = 4
    result = calculate_vector_magnitude(x, y)
    expected_result = 5.0
    assert result == expected_result

    x = -2
    y = 5
    result = calculate_vector_magnitude(x, y)
    expected_result = 5.385164807134504
    assert result == expected_result

    x = -6
    y = -8
    result = calculate_vector_magnitude(x, y)
    expected_result = 10.0
    assert result == expected_result

#Ejercicio 14

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False

#Ejercicio 15

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720