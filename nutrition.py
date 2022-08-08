# list of dictionaries, containing fruit and their calories from
# https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish

fruits = [
    {"name": "Apple", "calories": 130}, {"name": "Avocado", "calories":  50}, {"name": "Banana", "calories":  110},
    {"name": "Cantaloupe", "calories":  50}, {"name": "Grapefruit", "calories":  60}, {"name": "Grapes", "calories":  90},
    {"name": "Honeydew Melon", "calories":  50}, {"name": "Kiwifruit", "calories":  90}, {"name": "Lemon", "calories":  15},
    {"name": "Lime", "calories":  20}, {"name": "Nectarine", "calories":  60}, {"name": "Orange", "calories":  80},
    {"name": "Peach", "calories":  60}, {"name": "Pear", "calories":  100}, {"name": "Pineapple", "calories":  50},
    {"name": "Plums", "calories":  70}, {"name": "Strawberries", "calories":  50}, {"name": "Sweet Cherries", "calories":  100},
    {"name": "Tangerine", "calories":  50}
]


def main():
    '''main application, calling for input and checking it'''
    i = input('Please choose a fruit:  ').capitalize().strip().title()
    is_valid(i)


def is_valid(i):
    '''Check if the input is within the list'''
    i = i.strip()
    for each in fruits:
        if each["name"] == i:
            cal = each["calories"]
            print(f'Calories: {cal}')


main()