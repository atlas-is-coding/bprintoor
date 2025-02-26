from bprinter import Printer

# Создаем принтер с включенным форматированием
printer = Printer(enable_formatting=True)

# Базовое форматирование
printer("Это **жирный** текст")
printer("Это _курсивный_ текст")
printer("Это __подчеркнутый__ текст")
printer("Это ~~зачеркнутый~~ текст")

# Ссылки
printer("Посетите [наш сайт](https://example.com)")

# Inline код
printer("Используйте команду `pip install bprinter`")

# Цветной текст
printer("Это {red|красный} и {blue|синий} текст")

# Комбинированное форматирование
printer("**Жирный текст с _курсивом_ и {green|зеленым} цветом**")

# Создаем принтер с цветом и форматированием
colored_printer = Printer(
    color="blue",
    background="white",
    bold=True,
    enable_formatting=True
)

colored_printer("Синий жирный текст на белом фоне с **дополнительным выделением**")

# Создаем принтер с префиксом и форматированием
log_printer = Printer(
    prefix="[LOG]",
    show_time=True,
    enable_formatting=True
)

log_printer("Произошло {red|критическое} событие в `main.py`") 