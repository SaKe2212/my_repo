def juravls(S):
    x = S / 6
    katya = 4 * x
    petya = x
    sereja = x
    return petya, katya, sereja
S = int(input("Введите общее количество журавликов S: "))
petya, katya, sereja = juravls(S)
print(f"Петя сделал {petya} журавликов")
print(f"Сережа сделал {sereja} журавликов")
print(f"Катя сделала {katya} журавликов")