import pizza
from pizza import make_pizza1
from pizza import make_pizza as mp
import pizza as p


pizza.make_pizza2(12, 'pepperoni')
pizza.make_pizza2(16, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza1('pepperoni')
make_pizza1('mushrooms', 'green peppers', 'extra cheese')
mp('pepperoni')
mp('mushrooms', 'green peppers', 'extra cheese')
p.make_pizza2(12, 'pepperoni')
p.make_pizza2(16, 'mushrooms', 'green peppers', 'extra cheese')
