def mask_card_number(number: str) -> str:
    """Функция принимает номер карты в виде строки
    и возвращает замаскированны номер карты в виде строки"""
    return number[:4] + " " + number[4:6] + "** **** " + number[-4:]


def mask_account_number(number: str) -> str:
    """Функция принимает на входе номер счета
    и возвращает его в замаскированном виде в типе - строка"""
    return "**" + number[-4:]


if __name__ == "__main__":
    print(mask_card_number("7000792289606361"))
    print(mask_account_number("73654108430135874305"))
