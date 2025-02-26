from bprinter import BPrinter

# Создаем экземпляр BPrinter с показом времени
bp = BPrinter(show_time=True)

# Использование стандартных принтеров
bp.success("Операция выполнена успешно!")
bp.error("Произошла ошибка при выполнении операции")
bp.warning("Внимание! Возможны проблемы")
bp.info("Информационное сообщение")
bp.debug("Отладочная информация")
bp.critical("Критическая ошибка!")
bp.system("Системное сообщение")
bp.done("Задача завершена")

# Создание пользовательского принтера
custom = bp.custom(
    "TEST",
    color="cyan",
    background="white",
    bold=True
)
custom("Сообщение от пользовательского принтера")

# Использование BPrinter с разными стилями
bp_solid = BPrinter(style="solid")
bp_solid.info("Информация в сплошном стиле")
bp_solid.warning("Предупреждение в сплошном стиле")

bp_minimal = BPrinter(style="minimal")
bp_minimal.info("Информация в минималистичном стиле")
bp_minimal.warning("Предупреждение в минималистичном стиле") 