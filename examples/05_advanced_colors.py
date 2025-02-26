from bprinter import Color, Background, Style, Printer

# RGB цвета для текста
print(Color.rgb(255, 0, 0) + "Красный (RGB)" + Style.RESET)
print(Color.rgb(0, 255, 0) + "Зеленый (RGB)" + Style.RESET)
print(Color.rgb(0, 0, 255) + "Синий (RGB)" + Style.RESET)

# RGB цвета для фона
print(Background.rgb(255, 255, 0) + "Текст на желтом фоне (RGB)" + Style.RESET)
print(Background.rgb(255, 0, 255) + "Текст на пурпурном фоне (RGB)" + Style.RESET)

# Использование 256-цветной палитры
for i in range(0, 256, 16):
    print(Color.code(i) + f"Цвет {i}" + Style.RESET, end=" ")
print("\n")

# Градиент с использованием RGB
for i in range(0, 256, 32):
    r, g, b = i, 255 - i, 128
    print(Color.rgb(r, g, b) + f"Градиент {i}" + Style.RESET, end=" ")
print("\n")

# Создание принтера с RGB цветами
rainbow_printer = Printer(
    color=(255, 128, 0),  # Оранжевый
    background=(0, 0, 128)  # Темно-синий
)
rainbow_printer("Текст с RGB цветами")

# Яркие цвета
print(Color.BRIGHT_RED + "Яркий красный" + Style.RESET)
print(Color.BRIGHT_GREEN + "Яркий зеленый" + Style.RESET)
print(Color.BRIGHT_BLUE + "Яркий синий" + Style.RESET)

# Яркие цвета фона
print(Background.BRIGHT_RED + "Текст на ярком красном фоне" + Style.RESET)
print(Background.BRIGHT_GREEN + "Текст на ярком зеленом фоне" + Style.RESET)
print(Background.BRIGHT_BLUE + "Текст на ярком синем фоне" + Style.RESET)

# Комбинирование RGB цветов
print(Color.rgb(255, 128, 0) + Background.rgb(0, 0, 128) + 
      "Оранжевый текст на темно-синем фоне" + Style.RESET) 