import json

from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
from circular_singly_linked_list import CircularSinglyLinkedList
from subscribers import Subscriber

DATA_PATH = './data/data.json'
RESULT_PATH = './data/result.txt'
TARGET_DURATION = 10  # переменная для продолжительности разговора (по заданию должна быть равна 10)


# метод для извлечения исходных данных из файла json
def get_data():
    with (open(DATA_PATH, 'r', encoding='utf-8') as f):
        result = json.load(f)
    return result


# метод для записи полученных результатов в файл txt
def write_data(data):
    with open(RESULT_PATH, 'a', encoding='utf-8') as f:
        for el in data:
            result = json.dumps(el,
                                default=subscriber_to_json,
                                ensure_ascii=False,
                                indent=4)
            f.write(result + '\n')


# метод для сериализации экземпляров класса Subscriber
def subscriber_to_json(obj):
    if isinstance(obj, Subscriber):
        return {'ФИО': obj.fio, 'номер телефона': obj.phone,
                'дата разговора': obj.conversation_date, 'время разговора': obj.conversation_duration}
    raise TypeError(f'Объект типа {obj.__class__.__name__} нельзя сериализовать в JSON')


# метод для наполнения связного списка экземплярами класса Subscriber
def fill_linked_list(linked_list: CircularSinglyLinkedList, data):
    for item in data:
        subscriber = Subscriber(item.get('ФИО'), item.get('номер телефона'), item.get('дата разговора'),
                                item.get('время разговора'))
        linked_list.push_back(subscriber)
    return linked_list


# метод для подсчёта количества абонентов, время разговора у которых более 10 мин.
def count_subscribers_by_duration(linked_list: CircularSinglyLinkedList):
    counter = 0
    arr = linked_list.convert_to_array()
    for node in arr:
        duration = node.conversation_duration.split(':')
        if int(duration[0]) > TARGET_DURATION:
            counter += 1
        elif int(duration[0]) == TARGET_DURATION and int(duration[1]) > 0:
            counter += 1
    return counter


if __name__ == '__main__':
    # создание экземпляра класса CircularSinglyLinkedList - Однонаправленный кольцевой список
    circular_singly_list = CircularSinglyLinkedList()

    # извлечение данных абонентов
    data = get_data()

    # заполнение кольцевого списка абонентами
    fill_linked_list(circular_singly_list, data)

    # сортировка абонентов в кольцевом списке по алфавиту
    circular_singly_list.sort()
    circular_singly_list.output()

    # запись результата сортировки в файл
    write_data(circular_singly_list.convert_to_array())

    # подсчёт количества абонентов, которые разговаривали более 10 минут и запись в файл
    amount = count_subscribers_by_duration(circular_singly_list)
    with open(RESULT_PATH, 'a', encoding='utf-8') as f:
        f.write(f'Количество абонентов, которые разговаривали более {TARGET_DURATION} минут: {amount}\n')

    # arr = [9, 5, 7, 10, 4, 5, 1, 1, 5, 8]
    # test = CircularSinglyLinkedList()
    # for el in arr:
    #     test.push_back(el)
    # test.output()
    # test.sort(True)
    # test.output()
