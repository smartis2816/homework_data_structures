from functools import total_ordering


@total_ordering
class Subscriber:
    # конструктор для инициализации экземпляра класса
    def __init__(self, fio, phone, conversation_date, conversation_duration):
        self.fio = fio
        self.phone = phone
        self.conversation_date = conversation_date
        self.conversation_duration = conversation_duration

    # переопределение __str__ для наглядного вывода в консоль
    def __str__(self):
        return f"ФИО: {self.fio}\nномер телефона: {self.phone}\n" \
               f"дата разговора: {self.conversation_date}\n" \
               f"время разговора: {self.conversation_duration}"

    # ниже методы для сравнения экземпляров класса - пригодится при сортировке по алфавиту
    def __eq__(self, other):
        if isinstance(other, Subscriber):
            return self.fio == other.fio
        return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.fio[0] == other.fio[0]:
            i = 1
            while self.fio[i] == other.fio[i]:
                i += 1
            return self.fio[i] > other.fio[i]
        else:
            return self.fio[0] > other.fio[0]
