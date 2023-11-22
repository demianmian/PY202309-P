# 레시피 데이터베이스의 모의 데이터
recipes_db = [
    {
        'name': '토마토 파스타',
        'ingredients': ['토마토', '파스타', '소금', '올리브 오일', '마늘']
    },
    {
        'name': '갈릭 브레드',
        'ingredients': ['빵', '마늘', '버터']
    },
    # ... 더 많은 레시피들
]

# 대체 재료 데이터베이스의 모의 데이터
alternatives_db = {
    '토마토': ['캔 토마토', '토마토 페이스트'],
    '파스타': ['스파게티', '페투치니'],
    # ... 더 많은 대체 재료들
}

# 사용자가 가진 재료를 기반으로 레시피를 찾는 함수
def find_recipes(user_ingredients):
    possible_recipes = []
    for recipe in recipes_db:
        if set(recipe['ingredients']).issubset(set(user_ingredients)):
            possible_recipes.append(recipe['name'])
    return possible_recipes

# 대체 재료를 제안하는 함수
def suggest_alternatives(ingredient):
    return alternatives_db.get(ingredient, [])

