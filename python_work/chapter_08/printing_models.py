unprinted_designs = ['phone case', 'robot pendant', 'dodeca hedron']
completed_models = []
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
# print(f"\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


def print_models(unprinted_designs1, completed_models1):
    while unprinted_designs1:
        current_design1 = unprinted_designs1.pop()
        print(f"Printing model: {current_design1}")
        completed_models1.append(current_design1)


def show_completed_models(completed_models1):
    print(f"\nThe following models have been printed:")
    for completed_model1 in completed_models1:
        print(completed_model1)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
