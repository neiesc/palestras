#!/bin/python3

def multiplicacao(a: int, b: int) -> int:
    """Multiplicação de 2 numeros
    
    Arguments:
        a {int} -- Primeiro numero
        b {int} -- Segundo numero
    
    Returns:
        int -- Returno da multiplicação
    """
    return a * b

print(__name__)
if __name__ == "__main__":
    import sys
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(multiplicacao(a, b))