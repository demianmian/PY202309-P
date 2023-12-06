# 레시피 데이터베이스의 모의 데이터
recipes_db = [
    {
        'name': '토마토 파스타',
        'ingredients': ['토마토', '파스타', '소금', '올리브 오일', '마늘'],
        'instructions': [
            "파스타를 끓는 물에 소금을 약간 넣고 삶아주세요.",
            "토마토와 마늘을 잘게 다진 후 올리브 오일로 볶아 토마토 소스를 만듭니다.",
            "삶은 파스타를 토마토 소스와 잘 섞어주세요."
        ]
    },
    {
        'name': '갈릭 브레드',
        'ingredients': ['빵', '마늘', '버터'],
        'instructions': [
            "마늘을 잘게 다져 버터와 섞습니다.",
            "빵에 마늘 버터를 바르고 오븐에서 바삭하게 구워냅니다."
        ]
    },
    {
        'name': '브루스케타',
        'ingredients': ['빵', '토마토', '마늘', '올리브 오일', '소금', '바질', '페퍼'],
        'instructions': [
            "토마토는 주사위 모양으로 잘게 썰고, 마늘은 다져 준비합니다.",
            "빵을 오븐에서 바삭하게 구운 후 마늘을 문지릅니다.",
            "구운 빵 위에 토마토를 올리고 올리브 오일, 소금, 바질, 후추로 양념합니다."
        ]
    },
    {
        'name': '간장계란밥',
        'ingredients': ['밥', '계란', '간장', '참기름', '통깨'],
        'instructions': [
             "계란을 기호대로 후라이해주세요(반숙 추천)",
             "밥위에 후라이를 얹습니다",
             "간장과 참기름을 적당히 뿌립니다"
         ]

    },
    {
        'name': '크림 파스타',
        'ingredients': ['파스타', '크림', '버터', '마늘', '파마산 치즈', '소금', '후추'],
        'instructions': [
            "파스타를 기호대로 삶습니다(평균8분).",
            "팬에 버터를 녹이고 다진 마늘을 향이 날 때까지 볶습니다.",
            "크림과 파마산 치즈를 추가하여 소스가 두꺼워질 때까지 저어줍니다.",
            "삶은 파스타를 크림 소스와 잘 섞습니다.",
            "소금과 후추로 간을 맞춥니다."
        ]
    },
    {
        'name': '김치찌개',
        'ingredients': ['김치', '돼지고기', '두부', '양파', '대파', '마늘', '고추장', '간장', '참기름'],
        'instructions': [
            "돼지고기를 볶다가 잘게 썬 김치를 넣고 볶습니다.",
            "물을 부어 끓이고, 김치가 익을 때까지 중불에서 끓입니다.",
            "두부, 양파, 대파를 넣고 조금 더 끓인 후 마늘, 고추장, 간장으로 간을 맞춥니다."
        ]
    },
    {
        'name': '오이냉국',
        'ingredients': ['오이', '양파', '고추', '참기름', '식초', '설탕', '소금', '얼음'],
        'instructions': [
            "오이와 양파, 고추를 얇게 채 썰어줍니다.",
            "참기름, 식초, 설탕, 소금으로 양념장을 만듭니다.",
            "양념장에 채 썬 채소를 넣고 잘 섞은 후, 냉장고에서 차게 식혀줍니다.",
            "식사 직전에 얼음을 넣고 서빙합니다."
        ]
    },
    {
        'name': '불고기',
        'ingredients': ['소고기', '양파', '마늘', '대파', '간장', '설탕', '참기름', '후추'],
        'instructions': [
            "소고기는 얇게 썰어 양념장(간장, 설탕, 참기름, 후추, 다진 마늘, 다진 대파)에 재웁니다.",
            "양념한 고기를 중불에서 볶습니다.",
            "고기가 거의 익으면 채 썬 양파를 넣고 볶아줍니다."
        ]
    },
    {
        'name': '콩나물국',
        'ingredients': ['콩나물', '다시마', '멸치', '마늘', '대파', '소금', '참기름'],
        'instructions': [
            "다시마와 멸치로 육수를 끓입니다.",
            "육수가 끓으면 콩나물과 다진 마늘을 넣고 끓입니다.",
            "콩나물이 익으면 대파를 넣고 소금으로 간을 합니다."
        ]
    },
    {
        'name': '잡채',
        'ingredients': ['당면', '소고기', '당근', '양파', '시금치', '피망', '간장', '설탕', '참기름', '통깨'],
        'instructions': [
            "당면을 물에 불린 후 삶아줍니다.",
            "소고기, 당근, 양파, 피망을 얇게 채썰어 볶습니다.",
            "시금치는 데쳐서 준비합니다.",
            "모든 재료를 큰 볼에 넣고 간장, 설탕, 참기름으로 양념한 후 통깨를 뿌려줍니다."
        ]
    },
    # ... 더 많은 레시피들
]


# 대체 재료 데이터베이스의 모의 데이터
alternatives_db = {
     '토마토': ['캔 토마토', '토마토 페이스트'],
    '파스타': ['스파게티', '페투치니'],
    '올리브 오일': ['카놀라 오일', '해바라기 오일'],
    '마늘': ['마늘 분말', '마늘 페이스트'],
    '빵': ['크루통', '바게트'],
    '버터': ['마가린', '식물성 버터'],
    '계란': ['두부'],
    '간장': ['타마리', '코코넛 아미노스', '우스터 소스', '소야 소스'], 
    '참기름': ['들기름', '호두 오일'],
    '김': ['노리', '해초 샐러드'],
    '통깨': ['깨소금', '참깨'],
    '크림': ['코코넛 밀크', '캐시넛 크림'],
    '파마산 치즈': ['베지테리언 파마산'],
    '후추': ['흰 후추', '카옌 페퍼'],
    '돼지고기': ['닭고기', '쇠고기'],
    '두부': ['치즈', '유부'],
    '양파': ['샬롯', '대파'],
    '대파': ['쪽파', '양파'],
    '고추장': ['고춧가루', '미소 페이스트'],
    '오이': ['피클', '호박'],
    '식초': ['레몬 주스', '라임 주스'],
    '설탕': ['꿀', '메이플 시럽'],
    '소고기': ['돼지고기', '양고기'],
    '다시마': ['멸치 가루', '해초 가루'],
    '멸치': ['새우 가루', '다시다'],
    '콩나물': ['무', '숙주'],
    '당면': ['우동 면', '라이스 누들'],
    '당근': ['파프리카', '호박'],
    '시금치': ['케일', '청경채'],
    '피망': ['파프리카', '애호박']
}


'''# 사용자가 가진 재료를 기반으로 레시피를 찾는 함수
def find_recipes(user_ingredients, recipes_db):
    # 사용자가 가진 재료를 기반으로 레시피를 찾아 리스트로 반환합니다.
    recommended_recipes = []
    for recipe in recipes_db:
        if any(ingredient in user_ingredients for ingredient in recipe['ingredients']):
            recommended_recipes.append(recipe['name'])
    return recommended_recipes'''
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
    return alternatives_db.get(ingredient, [])


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