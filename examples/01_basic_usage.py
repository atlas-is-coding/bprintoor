from bprinter import Color, Background, Style

# Простое использование цветов
print(Color.RED + "Это красный текст" + Style.RESET)
print(Color.BLUE + "Это синий текст" + Style.RESET)
print(Color.GREEN + "Это зеленый текст" + Style.RESET)

# Использование фона
print(Background.WHITE + Color.BLACK + "Черный текст на белом фоне" + Style.RESET)
print(Background.BLUE + Color.WHITE + "Белый текст на синем фоне" + Style.RESET)

# Использование стилей
print(Style.BOLD + "Жирный текст" + Style.RESET)
print(Style.ITALIC + "Курсивный текст" + Style.RESET)
print(Style.UNDERLINE + "Подчеркнутый текст" + Style.RESET)
print(Style.STRIKE + "Зачеркнутый текст" + Style.RESET)

# Комбинирование стилей
print(Color.RED + Style.BOLD + Style.UNDERLINE + "Жирный подчеркнутый красный текст" + Style.RESET) 