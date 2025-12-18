def is_europe_standard(number: str):
    comma_index = number.rfind(",")
    dot_index = number.rfind(".")

    comma_is_exist = comma_index >= 0
    dot_is_exist = dot_index >= 0

    # запятая и точка существуют
    if comma_is_exist and dot_is_exist:
        # если индекс запятой больше, чем индекс точки,
        # тогда Европеский стандарт, иначе Американский
        if comma_index > dot_index:
            return True
        else:
            return False

    # запятая существует и отделяет дробную часть,
    # значит Европейский
    if comma_is_exist and \
        comma_index >= (len(number) - 3 - 1):
        return True

    # запятая существует, но не отделяет дробную часть,
    # значит Американсикий
    if comma_is_exist:
        return False
    
    # точка существет и отделяет дробную часть,
    # значит Американский
    if dot_is_exist and \
        dot_index >= (len(number) - 3 - 1):
        return False
    
    # точка существует, но не отделяет дробную часть,
    # значит Европейский
    if dot_is_exist:
        return True
    
    return True

def solve(numbers: list[str]):
    sum_numbers = 0

    for number in numbers:
        if is_europe_standard(number):
            print(float(number))
        
solve(["1,234.56", "10.000,50", "999,999.99", "99,999", "0.005"])