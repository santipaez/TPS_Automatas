def solve(operation: str) -> int:
    numbers = list(map(int, operation.replace('+', ' ').replace('*', ' ').split()))
    operators = [char for char in operation if char in ['+', '*']]
    
    # Resolver las multiplicaciones
    while '*' in operators:
        index = operators.index('*')
        numbers[index] *= numbers[index+1]
        del numbers[index+1]
        del operators[index]
    
    # Resolver las sumas
    result = numbers[0]
    for i in range(len(operators)):
        result += numbers[i+1] if operators[i] == '+' else 0
    
    return result


# Casos de prueba
print(solve("2 + 7 * 2 + 1")) # Debería imprimir 17
print(solve("2 * 2 * 2 + 32 * 2")) # Debería imprimir 72
