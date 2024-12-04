import random

def roll_die_simulation():
    frequency1 = 0  # contagem de 1s lançados
    frequency2 = 0  # contagem de 2s lançados
    frequency3 = 0  # contagem de 3s lançados
    frequency4 = 0  # contagem de 4s lançados
    frequency5 = 0  # contagem de 5s lançados
    frequency6 = 0  # contagem de 6s lançados

    # soma 6.000.000 lançamentos de um dado
    for roll in range(1, 6000001):
        face = random.randint(1, 6)  # número entre 1 e 6
        # usa o valor 1–6 para as faces a fim de determinar qual contador incrementar
        if face == 1:
            frequency1 += 1
        elif face == 2:
            frequency2 += 1
        elif face == 3:
            frequency3 += 1
        elif face == 4:
            frequency4 += 1
        elif face == 5:
            frequency5 += 1
        elif face == 6:
            frequency6 += 1

    print("Face\tFrequency")  # cabeçalhos de saída
    print(f"1\t{frequency1}")
    print(f"2\t{frequency2}")
    print(f"3\t{frequency3}")
    print(f"4\t{frequency4}")
    print(f"5\t{frequency5}")
    print(f"6\t{frequency6}")

    print("")

    input()

if __name__ == "__main__":
    roll_die_simulation()
