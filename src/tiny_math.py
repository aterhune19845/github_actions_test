def add(left: int, right: int) -> int:
    return left + right


def describe_number(value: int) -> str:
    if value < 0:
        return "negative"
    if value == 0:
        return "zero"
    if value % 2 == 0:
        return "positive even"
    return "positive odd"
