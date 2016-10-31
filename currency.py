class Currency():
    def __init__(self, currency_code, value):
        self.currency_code = currency_code
        self.value = value
        pass

    def __eq__(self, other):
        if self.currency_code == other.currency_code and self.value == other.value:
            return True
        else:
            return False

    def __add__(self, other):
         if self.value == other.value:
            return Currency

    # def __add__():
    #     if self.value == other.value:
    #         return Currency(self.currency_code, self.value + other.value)

    #     else:
    #         raise DifferentCurrencyCodeError()
    #         pass


#if __name__ == "__main__":
#     main()
