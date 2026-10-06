class OcheredDvaSteka:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def dobavit(self, x):
        self.stack_in.append(x)
        print("Добавили", x)

    # перекидываем из in в out когда out пустой
    def _transfer(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())

    def dostat(self):
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            print("Очередь пуста")
            return None
        self._transfer()
        val = self.stack_out.pop()
        print("Достали", val)
        return val

    def front(self):
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            print("Очередь пуста")
            return None
        self._transfer()
        return self.stack_out[-1]

    # вариативная часть - проверка есть ли элемент
    def soderzhit(self, x):
        for v in self.stack_in:
            if v == x:
                return True
        for v in self.stack_out:
            if v == x:
                return True
        return False

    def pokazat(self):
        # сначала out в обратном порядке (начало очереди), потом in
        first = []
        for i in range(len(self.stack_out) - 1, -1, -1):
            first.append(self.stack_out[i])
        for v in self.stack_in:
            first.append(v)
        print("Очередь:", first)


if __name__ == '__main__':
    q = OcheredDvaSteka()

    q.dobavit(10)
    q.dobavit(20)
    q.dobavit(30)
    q.pokazat()

    print()
    print("front =", q.front())
    print("soderzhit(20) =", q.soderzhit(20))
    print("soderzhit(99) =", q.soderzhit(99))

    print()
    q.dostat()
    q.dostat()
    q.pokazat()

    print()
    q.dostat()
    q.pokazat()

    print()
    q.dostat()