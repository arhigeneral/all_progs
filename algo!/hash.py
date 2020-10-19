book = dict()

book["milk"] = 1.49
book["avocado"] = 0.45
book["pechenki"] = 1.01

print(book["milk"])
def new_product():
    print("Нужно ли вам еще один продукт в списке?")
    proverka = input()
    if (proverka == "y"):
        print("Введите новый продукт ")
        product = input()
        print("Введите цену продукта")
        cost = float(input())
        book[product] = cost
        new_product()
    else:
        return 0

new_product()

print(book)
