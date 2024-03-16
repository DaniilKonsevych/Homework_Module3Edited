import random

def get_numbers_ticket(min : int, max : int, quantity : int):
    try:
        if max>1000 or min<1 or max<=quantity or min>=quantity:
            return ""
        else:
            Sorting = sorted(random.sample(range(min, max), quantity))
            return Sorting
    except:
        return ""
    
#Тестування
print(get_numbers_ticket(1, 50, 5))
print(get_numbers_ticket(0, 50, 5))
print(get_numbers_ticket(1, 1001, 5))
print(get_numbers_ticket(2, 50, -1))
print(get_numbers_ticket("ф", "50", ";"))
print(get_numbers_ticket(50, 1, 5))
print(get_numbers_ticket(1, 50, 51))
print(get_numbers_ticket(1, 6, 5))
print(get_numbers_ticket(1, 3, 2))