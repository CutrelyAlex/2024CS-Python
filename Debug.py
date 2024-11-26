from Modles.dish import *

dish_path = "dishes.json"

# 测试用入口
def test_main():
    dishes = convert_to_dishes(load_dishes_from_json(dish_path))
    print(dishes[0].display_info())

    
if __name__ == "__main__":
    test_main()