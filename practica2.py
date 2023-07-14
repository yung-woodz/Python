alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list = list(range(26))
list1 = int()

print(alpha)
print(list)

print("INGRESE SU PALABRA A TRAVES DE NUMEROS")
print("Ingrese espacio por si quiere terminar (max. 26)")


for x in list:
    num = int(input())
    if num > 0 or num < 27:
        list(list1(range(num)))
    elif num == ' ':
        break

print(alpha(list1))