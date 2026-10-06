#считаем сколько раз встречается каждое слово
def poschitat_slova(text):
    words = text.split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq


# вывод по алфавиту (вариативная часть)
def vyvesti_po_alphabetu(freq):
    keys = sorted(freq.keys())
    for w in keys:
        print(w, "->", freq[w])


text = input("Введите текст: ")
print()

freq = poschitat_slova(text)

print("Обычный вывод:")
for w in freq:
    print(w, "->", freq[w])

print()
print("По алфавиту:")
vyvesti_po_alphabetu(freq)