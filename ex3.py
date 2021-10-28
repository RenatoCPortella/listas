nota = []

for i in range(4):
    nota1 = float(input('Digite a nota: '))
    nota.append(nota1)
media = sum(nota)/4
print(f'As notas foram: {nota}\nA média foi: {media}')
