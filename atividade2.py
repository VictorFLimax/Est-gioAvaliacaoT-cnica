texto = input("Digite: ")

contador = 0

for letra in texto:
    if letra == 'a' or letra == 'A':
        contador += 1

if contador > 0:
    print(f"A letra 'a' aparece {contador} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")