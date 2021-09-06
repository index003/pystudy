
def make_pizza(*toppings):
    print(toppings)


def make_pizza1(*toppings):
    print("\nMake a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def make_pizza2(size, *toppings):
    print(f"\nMake a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
make_pizza1('pepperoni')
make_pizza1('mushrooms', 'green peppers', 'extra cheese')
make_pizza2(12, 'pepperoni')
make_pizza2(16, 'mushrooms', 'green peppers', 'extra cheese')
