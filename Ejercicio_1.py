def sumar(a,b):
    if isinstance(a,(int, float)) and  isinstance(b, (int,float)):
        return a+b
    elif isinstance(a,list) and isinstance(b,list):
        return a+b
    elif isinstance(a, str) and isinstance(b, str):
        return a+b
    else:
        return (f"No es posible sumar {type(a)} con {type(b)}")

#Ejemplos
print(sumar(5,3))
print(sumar([1,2,3],[4,5,6]))
print(sumar ("Buenos","dias"))
print(sumar(5,[1,2]))
print(sumar(3,"hola"))
