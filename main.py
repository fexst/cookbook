with open('recipes.txt', encoding='UTF-8') as f:
    cook_book = {}
    lines = f.readlines()
    count = 0
    count_dish = 0
    for idx, line in enumerate(lines):
        if (line.strip().isalpha() or (" " in line.strip() or "-" in line.strip())) and not "|" in line:
            dish = line.strip()
            cook_book[dish] = []
        elif line.strip().isdigit():
            for i in range(idx + 1, idx + int(line.strip()) + 1):
                if len(line) > 1:
                    ingredients = {}
                    for j in range(len(lines[i])):
                        ingredient_name = lines[i][:lines[i].find(" |")]
                        quantity = lines[i][lines[i].find('| ') + 2:lines[i][lines[i].find('| ') + 2:].find(" |") + lines[i].find('| ') + 2]
                        measure = lines[i][lines[i].rfind(' '):]
                        ingredients['ingredient_name'] = ingredient_name.strip()
                        ingredients['quantity'] = quantity.strip()
                        ingredients['measure'] = measure.strip()
                    cook_book[dish].append(ingredients)
                    
def get_shop_list_by_dishes(dishes, person_count):
    result = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                if name not in result:
                    result[name] = {'measure': measure, 'quantity': quantity}
                else:
                    result[name]['quantity'] += quantity

    return print(result)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)