class MyItems:

    def __init__(self, *values) -> None:
        self._value = list(values)

    def __len__(self):
        return len(self._value)

    def __getitem__(self, item):
        return self._value.__getitem__(item)
