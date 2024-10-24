#acredito q segue um padrao de mais 2
a = [1, 3, 5, 7]
a.append(a[-1] + 2)
print("a) Próximo número:", a[-1])



#acredito q multiplique por 2
b = [2, 4, 8, 16, 32, 64]
b.append(b[-1] * 2)
print("b) Próximo número:", b[-1])

#raiz quadrados perfeitos
c = [0, 1, 4, 9, 16, 25, 36]
c.append((len(c))**2)
print("c) Próximo número:", c[-1])

#quadrados de números pares.
d = [4, 16, 36, 64]
d.append((len(d)*2)**2)
print("d) Próximo número:", d[-1])


#segue a sequência de Fibonacci.
e = [1, 1, 2, 3, 5, 8]
e.append(e[-1] + e[-2])
print("e) Próximo número:", e[-1])
#alterna entre 8 e 1 soma
f = [2, 10, 12, 16, 17, 18, 19]
f.append(f[-1] + 1)
print("f) Próximo número:", f[-1])