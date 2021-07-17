from pprint import pprint


def get_data():

    result = dict()
    val_name = ['ingredient_name', 'quantity', 'measure']
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            cook_name = line.strip()
            number_of_ingredients = int(f.readline().strip())

            ingredients_list=[]
            for ingredients in range(number_of_ingredients):
                data = f.readline().strip().split(' | ')
                ingredients_dict = dict(zip(val_name, data))
                ingredients_list.append(ingredients_dict)

            f.readline()
            result[cook_name] = ingredients_list
    return result

def get_shop_list_by_dishes(dishes: list, person_count: int):
    cook_book = get_data()
    shopping_dict = {}
    for dish in dishes:
        ingredients_list = cook_book[dish]
        for ingredients_dict in ingredients_list:
            ingredient = ingredients_dict['ingredient_name']
            if ingredient in shopping_dict.keys():
                shopping_dict[ingredient]['quantity'] += int(ingredients_dict['quantity']) * person_count
            else:
                shopping_dict[ingredient] = {'measure': ingredients_dict['measure'], 'quantity': int(ingredients_dict['quantity']) * person_count}

    return shopping_dict




pprint(get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 2))
    

#pprint(cook_book(), width=100, sort_dicts=False)




