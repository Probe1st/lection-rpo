def is_europe_standard(number: str):
    comma_index = number.rfind(",")
    dot_index = number.rfind(".")

    # запятая и точка существуют
    if comma_index >= 0 and dot_index >= 0:
        # если индекс запятой больше, чем индекс точки,
        # тогда Европеский стандарт, иначе Американский
        if comma_index > dot_index:
            return True
        else:
            return False

    # запятая существует и отделяет дробную часть,
    # значит Европейский
    if comma_index >= 0 and \
        comma_index >= (len(number) - 3 - 1):
        return True

    # запятая существует, но не отделяет дробную часть,
    # значит Американсикий
    if comma_index >= 0:
        return False
    
    # точка существет и отделяет дробную часть,
    # значит Американский
    if dot_index >= 0 and \
        dot_index >= (len(number) - 3 - 1):
        return False
    
    # точка существует, но не отделяет дробную часть,
    # значит Европейский
    if dot_index >= 0:
        return True
    
    return True

def solve(numbers: list[str]):
    sum_numbers = 0

    for number in numbers:
        if is_europe_standard(number):
            sum_numbers += float()
    