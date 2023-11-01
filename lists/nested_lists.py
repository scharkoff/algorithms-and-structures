nested_list = [[1, 2, 1], [5, 2, [1, 2, [199, 29]], 3], [67, 10, 2, [1, 100, 20]]]

def nested_list_recursive(nested_list):
    result = []

    for item in nested_list:
        if (type(item) == list):
            result.extend(nested_list_recursive(item))
        else:
            result.append(item)
             
    return result

print(max(nested_list_recursive(nested_list)))