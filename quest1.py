


palavra = input()

for i in palavra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        palavra = palavra.replace(i, i.upper())   
print(palavra)
