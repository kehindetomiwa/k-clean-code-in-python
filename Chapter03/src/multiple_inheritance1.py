

class BaseModule:
    module_name = "top"

    def __init__(self, p_module_name) -> None:
        self.name = p_module_name

    def __str__(self) -> str:
        return f"{self.module_name}:{self.name}"


class BaseModule1(BaseModule):
    module_name = "module-1"


class BaseModule2(BaseModule):
    module_name = "module-2"


class BaseModule3(BaseModule):
    module_name = "module-3"


class ConcreteModuleA12(BaseModule1, BaseModule2):
    """"
    """


class ConcreteModuleB23(BaseModule2, BaseModule3):
    """
    """


for cls in ConcreteModuleA12.mro():
    print(cls.__name__)
