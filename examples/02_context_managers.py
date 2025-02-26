from bprinter import Style, Color, Background

# Использование контекстного менеджера для цвета
with Style.color("red"):
    print("Этот текст красный")
    print("И этот тоже красный")

# Использование контекстного менеджера для нескольких стилей
with Style.styled(Style.BOLD, Color.BLUE, Background.WHITE):
    print("Этот текст жирный, синий на белом фоне")
    print("И этот тоже")

# Вложенные контекстные менеджеры
with Style.color("blue"):
    print("Синий текст")
    with Style.styled(Style.BOLD):
        print("Жирный синий текст")
    print("Снова просто синий текст")

# Использование RGB цветов
with Style.color((255, 128, 0)):  # Оранжевый цвет
    print("Текст оранжевого цвета")

# Комбинирование разных контекстных менеджеров
with Style.color("green"):
    print("Зеленый текст")
    with Style.styled(Style.BOLD, Style.UNDERLINE):
        print("Жирный подчеркнутый зеленый текст") 