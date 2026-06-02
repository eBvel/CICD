def max_number(a: float, b: float) -> float:

    if a > b:
        return a

    else:
        return b


def multiply(a: float, b: float) -> float:

    return a * b


class FixMe:
    def __init__(self, name: str):

        self.name = name

    def zero_function(self, x: float) -> None:

        if x > 0:
            print("positive")

        elif x < 0:
            print("negative")

        else:
            print("zero")
