# 예시 레시피 데이터베이스
recipes = {
    '토마토 파스타': {'토마토', '파스타', '올리브 오일', '마늘'},
    '감자 샐러드': {'감자', '마요네즈', '양파', '사과'},
    '닭가슴살 구이': {'닭가슴살', '소금', '후추', '올리브 오일'},
}

# 대체 재료 목록
substitutes = {
    '토마토': ['파프리카'],
    '파스타': ['스파게티', '우동'],
    '올리브 오일': ['식용유', '버터'],
}

def find_recipe(ingredients):
    possible_recipes = []
    for recipe, required_ingredients in recipes.items():
        if ingredients.issuperset(required_ingredients):
            possible_recipes.append(recipe)
    return possible_recipes

def suggest_substitutes(ingredients):
    suggested_substitutes = {}
    for ingredient in ingredients:
        if ingredient in substitutes:
            suggested_substitutes[ingredient] = substitutes[ingredient]
    return suggested_substitutes

# 사용자의 재료 입력
user_ingredients = {'토마토', '파스타', '마늘', '식용유'}

# 레시피 추천
recommended_recipes = find_recipe(user_ingredients)
print("추천 레시피:", recommended_recipes)

# 대체 재료 제안
ingredient_substitutes = suggest_substitutes(user_ingredients)
print("가능한 대체 재료:", ingredient_substitutes)
