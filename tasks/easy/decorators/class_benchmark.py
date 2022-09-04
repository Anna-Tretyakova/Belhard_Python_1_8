"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time

# start_time = time.time()
# end_time = time.time()
# difference = e - s


def class_benchmark(cls):
    call_attr = {k: v for k, v in cls.attr.items() if callable(v)}
    for name, value in call_attr.items():
        decorated = class_benchmark(value)
        setattr(cls, name, decorated)
    return cls


def def_benchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}\nВремя начала: {start_time}")
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"Выполнено {func.__name__}\nВремя окончания: {end_time}\nВсего затрачено времени на выполнение: {end_time - start_time}")
        return res
    return wrapper


