import math
import random

num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é {raiz:.2f}")

graus = 45
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(f"{seno:.2f}")

num_random_int = random.randint(a=1, b=10)
print(num_random_int)

def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")
    
print_lyrics()
print(type(print_lyrics))