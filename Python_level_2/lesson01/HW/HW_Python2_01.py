# Урок 1. Работа с сетью, сокеты. Тестирование кода
# 1. Функционал
# Первая часть домашнего задания будет заключаться в реализации простого клиент-серверного взаимодействия по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата.
# Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
# Функции клиента:
# - сформировать presence-сообщение; 1
# - отправить сообщение серверу; 1
# - получить ответ сервера;
# - разобрать сообщение сервера;
# - параметры командной строки скрипта client.py <addr> [<port>]:
# addr - ip-адрес сервера
# port - tcp-порт на сервере, по умолчанию 7777
# Функции сервера:
# - принимает сообщение клиента; 1
# - формирует ответ клиенту;
# - отправляет ответ клиенту;
# - имеет параметры командной строки:
# -p <port> - TCP-порт для работы (по умолчанию использует порт 7777)
# -a <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)
#
# 2. Тесты.
# Для всех функций необходимо написать тесты с использованием doctest (небольшие тесты в документации функций), unittest или py.test (в дальнейшем упор будет делаться на библиотеку py.test). Тесты должны быть оформлены в отдельных скриптах с префиксом test_ в имени файла (например, test_client.py).
#
# 3. Дополнительно
# В качестве практики написания тестов напишите тесты для домашних работ курса Python-1.