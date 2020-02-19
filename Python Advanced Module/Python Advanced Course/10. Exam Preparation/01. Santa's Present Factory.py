from collections import deque

PRESENTS_REQUIREMENTS = {"Doll": 150,
                         "Wooden train": 250,
                         "Teddy bear": 300,
                         "Bicycle": 400, }


def inputs_func() -> tuple:
    material_boxes = deque([int(x) for x in input().split(" ")])
    magic_values = deque([int(x) for x in input().split(" ")])
    return material_boxes, magic_values


def check_for_match(materials: deque, magic_levels: deque):
    produced_presents = {}
    while materials and magic_levels:
        match = False
        material = materials.pop()
        magic = magic_levels.popleft()
        magic_score = material * magic
        for k, v in PRESENTS_REQUIREMENTS.items():
            if v == magic_score:
                if not k in produced_presents.keys():
                    produced_presents[k] = 0
                produced_presents[k] += 1
                match = True
                break
        if not match:
            if magic_score < 0:
                materials.append(material + magic)
            elif magic_score > 0:
                materials.append(material + 15)
            elif magic_score == 0:
                if material != 0:
                    materials.append(material)
                if magic != 0:
                    magic_levels.appendleft(magic)
    return produced_presents, materials, magic_levels


def print_result(result_dict: dict, materials: deque, magic_levels: deque):
    if "Doll" in result_dict.keys() and "Wooden train" in result_dict.keys():
        print("The presents are crafted! Merry Christmas!")
    elif "Teddy bear" in result_dict.keys() and "Bicycle" in result_dict.keys():
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")
    if materials:
        print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
    if magic_levels:
        print(f"Magic left: {', '.join(map(str, magic_levels))}")
    if result_dict:
        for item in sorted(result_dict.items(), key=lambda kv: (kv[0], kv[1])):
            print(f"{item[0]}: {item[1]}")


def main():
    material_boxes, magic_levels = inputs_func()
    result = check_for_match(material_boxes, magic_levels)
    print_result(*result)


if __name__ == "__main__":
    main()
