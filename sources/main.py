
from function import find_recipes, suggest_alternatives, recipes_db

# 사용자로부터 재료를 입력받습니다. 입력은 쉼표로 구분된 문자열로 
input_ingredients = input("가지고 있는 재료를 쉼표로 구분하여 입력해주세요: ")
user_ingredients = [ingredient.strip() for ingredient in input_ingredients.split(',')]

# 입력받은 재료로 만들 수 있는 레시피를 찾기
recommended_recipes = find_recipes(user_ingredients)
print("추천 레시피:", recommended_recipes)

# 사용자에게 선택받은 레시피를 입력받거나 선택할 수 있게 
selected_recipe_name = input("만들고 싶은 레시피를 입력해주세요: ")
selected_recipe = next((recipe for recipe in recipes_db if recipe['name'] == selected_recipe_name), None)

# 선택한 레시피의 누락된 재료를 찾아 대체재를 제안
if selected_recipe:
    missing_ingredients = [ingredient for ingredient in selected_recipe['ingredients'] if ingredient not in user_ingredients]
    for ingredient in missing_ingredients:
        alternatives = suggest_alternatives(ingredient)
        print(f"{ingredient}의 대체재:", alternatives)
else:
    print("선택한 레시피를 찾을 수 없습니다.")
