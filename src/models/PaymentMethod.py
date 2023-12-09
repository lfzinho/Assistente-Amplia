from abc import ABC, abstractmethod


# class PaymentMethod:
#     def __init__(self):
#         pass

#     def view_information(self):
#         pass


class PaymentMethod(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def view_information(self) -> None:
        pass
