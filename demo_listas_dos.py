import random

def selecciona_frase(frases):
    return random.choice(frases)

frases = ["Frase 1","Frase 2","Frase 3","Frase 4",
          "Frase 5","Frase 6","Frase 7","Frase 8",
          "Frase 9","Frase 10","Frase 11","Frase 12",
          "Frase 13","Frase 14","Frase 15","Frase 16"]

print(f"Tengo {len(frases)} frases celebres...")

'''
for frase in frases:
    print(f"{frase}")
'''

print("_____________________________________________________________________________")
#selecciona una frase aleatoria

print(selecciona_frase(frases))
