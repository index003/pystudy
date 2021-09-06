def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}. ")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


# 位置实参
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 默认值
def describe_pet2(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}. ")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


describe_pet2('willie')
describe_pet2(pet_name='harry', animal_type='hamster')


