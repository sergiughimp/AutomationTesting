class Invoice:

    __seria = "XYZ" # attributes with __ are private
    number = 1

    def __init__(self, product_name, quantity, price_unit):
        self.number_invoice = Invoice.number
        self.product_name = product_name
        self.quantity = quantity
        self.price_unit = price_unit
        Invoice.number += 1

    def change_seria(self, new_seria):
        # can make the changes only from inside
        self.__seria = new_seria
    def describe(self):
        print(f"{self.__seria} {self.number_invoice}")
        print(f"Product | Quantity | Unit price")
        print(f"{self.product_name} | {self.quantity} | {self.price_unit}")


invoice1 = Invoice("Phone", 10, 120)
# print(invoice1.seria, invoice1.number_invoice)

invoice2 = Invoice("TV", 5, 200)
# Invoice.seria = "ABC"

# print(invoice2.seria, invoice2.number_invoice)
# print(invoice2.seria, invoice1.number_invoice)


invoice1.describe()
invoice1.change_seria("RTY")
invoice1.describe()
