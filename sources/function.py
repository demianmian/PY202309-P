import recipes_module

# 사용자가 가진 재료를 기반으로 레시피를 찾는 함수
def find_recipes(user_ingredients, recipes_db):
    # 사용자가 가진 재료를 기반으로 레시피를 찾아 리스트로 반환합니다.
    recommended_recipes = []
    for recipe in recipes_db:
        if any(ingredient in user_ingredients for ingredient in recipe['ingredients']):
            recommended_recipes.append(recipe)  # 레시피 전체를 추가
    return recommended_recipes


# 대체 재료를 제안하는 함수
def suggest_alternatives(ingredient):
    return recipes_module.alternatives_db.get(ingredient, [])


# 쇼핑 리스트 만드는 함수 
def create_shopping_list(selected_recipe, user_ingredients):
    shopping_list = [ingredient for ingredient in selected_recipe['ingredients']
                     if ingredient not in user_ingredients]
    return shopping_list

# 레시피 지침을 출력하는 함수
def print_recipe_instructions(recipe_name, recipes_db):
    recipe = next((r for r in recipes_db if r['name'] == recipe_name), None)
    if not recipe:
        print("레시피를 찾을 수 없습니다.")
        return
    
    print(f"\n{recipe['name']} 레시피 지침:")
    for instruction in recipe.get('instructions', []):
        print(instruction)