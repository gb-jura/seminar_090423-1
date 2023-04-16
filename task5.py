"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

websites = ['yandex.ru', 'youtube.com']

for website in websites:
    ping_result = subprocess.check_output(['ping', website])
    encoding = chardet.detect(ping_result)['encoding']
    ping_result_str = ping_result.decode(encoding)
    print(ping_result_str)