from function import find_recipes, suggest_alternatives, recipes_db, create_shopping_list, print_recipe_instructions
from shopping_list_manager import save_shopping_list

while True:
    # 사용자로부터 재료를 입력받기
    input_ingredients = input("가지고 있는 재료를 쉼표로 구분하여 입력해주세요: ")
    user_ingredients = [ingredient.strip() for ingredient in input_ingredients.split(',')]

    # 가진 재료로 만들 수 있는 레시피 추천
    available_recipes = find_recipes(user_ingredients, recipes_db)
    if available_recipes:
        print("\n가지고 있는 재료로 만들 수 있는 레시피:")
        for recipe in available_recipes:
            print(f" - {recipe}")
    else:
        print("\n가진 재료로 만들 수 있는 레시피가 없습니다.")

    # 사용자가 만들고 싶은 레시피를 선택할 수 있도록 안내
    selected_recipe_name = input("\n만들고 싶은 레시피 이름을 입력하시거나, 없으면 엔터를 눌러주세요: ")
    if selected_recipe_name:
        selected_recipe = next((recipe for recipe in recipes_db if recipe['name'] == selected_recipe_name), None)

        # 선택한 레시피가 있다면, 필요한 재료를 체크
        if selected_recipe:
            print(f"\n{selected_recipe_name} 레시피에 필요한 재료:")
            missing_ingredients = []
            for ingredient in selected_recipe['ingredients']:
                # 재료가 사용자가 가지고 있는 재료인지 확인
                if ingredient in user_ingredients:
                    print(f" - {ingredient} (가지고 있음)")
                else:
                    missing_ingredients.append(ingredient)
                    alternatives = suggest_alternatives(ingredient)
                    alternative_text = f" (대체재료: {', '.join(alternatives)})" if alternatives else ""
                    print(f" - {ingredient} (필요함){alternative_text}")
            

            # 쇼핑 리스트를 생성
            shopping_list = create_shopping_list(selected_recipe, user_ingredients)
            if shopping_list:
                print("\n쇼핑 리스트:")
                for item in shopping_list:
                    print(f" - {item}")
            else:
                print("\n추가로 구매할 재료가 없습니다.")

            # 사용자에게 쇼핑 리스트를 저장할지 질문
            if shopping_list:
                save_option = input("쇼핑 리스트를 저장하시겠습니까? (yes/no): ")
                if save_option.lower() == 'yes':
                    filename = save_shopping_list(shopping_list)
                    print(f"쇼핑 리스트가 {filename}에 저장되었습니다.")
                # 레시피 지침을 출력하는 코드를 추가
                print_recipe_instructions(selected_recipe_name, recipes_db)
            break
        else:
            print("선택한 레시피를 찾을 수 없습니다.")
    else:
        # 엔터를 눌렀을 경우, 다시 재료 입력 단계로 돌아감
        continue
