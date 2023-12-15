from function import find_recipes, suggest_alternatives, create_shopping_list, print_recipe_instructions
from shopping_list_manager import save_shopping_list
import recipes_module

while True:
    # 사용자로부터 재료를 입력받기
    input_ingredients = input("가지고 있는 재료를 쉼표로 구분하여 입력해주세요: ")
    user_ingredients = [ingredient.strip() for ingredient in input_ingredients.split(',')]

    # 가진 재료로 만들 수 있는 레시피 추천
    available_recipes = find_recipes(user_ingredients, recipes_module.recipes_db)
    if available_recipes:
        print("\n가지고 있는 재료로 만들 수 있는 레시피:")
        for idx, recipe in enumerate(available_recipes, 1):
            print(f" - {idx}. {recipe['name']}")
    else:
        print("\n가진 재료로 만들 수 있는 레시피가 없습니다.")

    # 사용자가 만들고 싶은 레시피를 선택할 수 있도록 안내
    selected_recipe_idx = input("\n만들고 싶은 레시피 번호를 입력해주세요: ")
    if selected_recipe_idx.isdigit():
        selected_recipe = available_recipes[int(selected_recipe_idx) - 1]

        # 선택한 레시피가 있다면, 필요한 재료를 체크
        if selected_recipe:
            print(f"\n{selected_recipe['name']} 레시피에 필요한 재료:")
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
            print_recipe_instructions(selected_recipe['name'], recipes_module.recipes_db)
            break
        else:
            print("선택한 레시피를 찾을 수 없습니다.")
    else:
        # 숫자가 아닌 값을 입력한 경우, 다시 레시피 선택 단계로 돌아감
        continue
