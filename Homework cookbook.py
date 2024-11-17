#Задание1
with open('recipes.txt', encoding='UTF-8') as file:
    cook_book = {}
    for n in file:
        recepie_name = n.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for p in range(ingredients_count):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'ingredient_name': product,
                                'quantity': int(quantity),
                                'measure': word})
        file.readline()
        cook_book[recepie_name] = ingredients

print(cook_book)


#Задание2
def get_shop_list_by_dishes(dishes: list, person_count: int):
    new_cook = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                new_cook.setdefault(ingredient_name, {'quantity': 0, 'measure': ingredient['measure']})
                new_cook[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
        else:
            print('Такого блюда нет в книге')

        print(new_cook)

get_shop_list_by_dishes(['Запеченный картофель'],2 )