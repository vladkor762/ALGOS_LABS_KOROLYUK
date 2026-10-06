import base64
import datetime

#запись об одной странице
class Page:
    def __init__(self, url, vremya, zakladka=False):
        self.url = url
        self.vremya = vremya
        self.zakladka = zakladka


class IstoriyaBrauzera:
    def __init__(self):
        self.history = []
        self.pos = -1  #-1 значит пусто

    def pereiti(self, url):
        #если откатывались назад, всё что впереди удаляем
        self.history = self.history[:self.pos + 1]
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.history.append(Page(url, now))
        self.pos = len(self.history) - 1
        print("Перешли на", url)

    def nazad(self):
        if self.pos > 0:
            self.pos -= 1
            print("Назад:", self.history[self.pos].url)
        else:
            print("Нельзя назад, это начало")

    def vpered(self):
        if self.pos < len(self.history) - 1:
            self.pos += 1
            print("Вперёд:", self.history[self.pos].url)
        else:
            print("Нельзя вперёд, дальше ничего нет")

    def pokazat(self):
        if self.pos >= 0:
            print("Сейчас открыто:", self.history[self.pos].url)
        else:
            print("История пуста")

    def ochistit(self):
        self.history = []
        self.pos = -1
        print("История очищена")

    # ищем записи где встречается подстрока
    def poisk_po_domenu(self, domen):
        found = []
        for p in self.history:
            if domen in p.url:
                found.append(p)
        if len(found) == 0:
            print("Ничего не нашли по", domen)
        else:
            print("Найдено", len(found), "записей:")
            for p in found:
                print(" ", p.url, "|", p.vremya, "| закладка:", p.zakladka)

    def toggle_zakladka(self):
        if self.pos >= 0:
            self.history[self.pos].zakladka = not self.history[self.pos].zakladka
            print("Закладка:", self.history[self.pos].zakladka)
        else:
            print("Нечего помечать")

    #сохраняем в base64. одна строка=одна запись
    def sohranit(self, filename):
        f = open(filename, "w")
        for p in self.history:
            line = p.url + "|" + p.vremya + "|" + str(p.zakladka)
            enc = base64.b64encode(line.encode())
            f.write(enc.decode() + "\n")
        f.close()
        print("Сохранили в", filename)

    # читаем обратно
    def zagruzit(self, filename):
        self.history = []
        self.pos = -1
        try:
            f = open(filename, "r")
            for raw in f:
                raw = raw.strip()
                if raw == "":
                    continue
                dec = base64.b64decode(raw).decode()
                parts = dec.split("|")
                url = parts[0]
                vremya = parts[1]
                zakl = parts[2] == "True"
                self.history.append(Page(url, vremya, zakl))
            f.close()
            if len(self.history) > 0:
                self.pos = len(self.history) - 1
            print("Загружено:", len(self.history))
        except FileNotFoundError:
            print("Файл не найден:", filename)


if __name__ == '__main__':
    h = IstoriyaBrauzera()
    h.pereiti("https://google.com")
    h.pereiti("https://github.com")
    h.pereiti("https://github.com/python")
    h.pereiti("https://youtube.com")
    h.pereiti("https://stackoverflow.com")

    print()
    h.nazad()
    h.nazad()
    h.pokazat()

    print()
    h.vpered()
    h.pokazat()

    print()
    h.toggle_zakladka()
    h.pereiti("https://python.org")

    print()
    h.poisk_po_domenu("github")

    print()
    h.sohranit("history.txt")
    h.ochistit()

    print()
    h.zagruzit("history.txt")
    h.pokazat()

    # print("готово")