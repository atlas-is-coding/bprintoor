from bprinter import ASCIIArtGenerator, init

# Инициализация с настройками по умолчанию
init()

# Простой ASCII арт
print("Простой ASCII арт:")
print(ASCIIArtGenerator.render("Hello!"))

# ASCII арт с цветом
print("\nЦветной ASCII арт:")
print(ASCIIArtGenerator.render("Colors!", color="red"))

# Отключаем цветной вывод
print("\nОтключаем цветной вывод:")
init(strip=True)
print(ASCIIArtGenerator.render("No Colors!", color="red"))

# Включаем цветной вывод обратно
init(strip=False)

# ASCII арт с фоном
print("\nASCII арт с фоном:")
print(ASCIIArtGenerator.render("Background", background="blue"))

# ASCII арт с другим шрифтом
print("\nASCII арт с шрифтом 'banner':")
print(ASCIIArtGenerator.render("Big Text", font="banner"))

# ASCII арт с ограниченной шириной
print("\nASCII арт с шириной 40 символов:")
print(ASCIIArtGenerator.render("Narrow Text", width=40))

# Предпросмотр разных шрифтов
print("\nПредпросмотр разных шрифтов:")
print(ASCIIArtGenerator.preview_fonts("ABC", fonts=["standard", "banner", "big"]))

# Получение списка всех доступных шрифтов
print("\nДоступные шрифты:")
fonts = ASCIIArtGenerator.get_available_fonts()
print(", ".join(fonts[:10]) + "...") 