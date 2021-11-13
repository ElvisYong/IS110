def convert_to_list(num_list_str):
    comma_splited = num_list_str.split(',')
    layer_count = 0
    outer_layer = []
    middle_layer = []
    deep_layer = []

    for line in comma_splited:
        if line[0] == '[':
            layer_count += 1
        
        if layer_count == 1:
            outer_layer.append(int(line.replace('[', '').replace(']', '')))
            continue
        
        if layer_count == 2:
            middle_layer.append(int(line.replace('[', '').replace(']', '')))
            
            if ']' in line:
                layer_count -= 1
                outer_layer.append(middle_layer)
                middle_layer = []
            continue
        
        if layer_count == 3:
            deep_layer.append(int(line.replace('[', '').replace(']', '')))
            
            if ']' in line:
                layer_count -= 2
                middle_layer.append(deep_layer)
                outer_layer.append(middle_layer)
                deep_layer = []
            continue
    return outer_layer


my_list = convert_to_list('[4,5,[6,7],[8,[9,10]],11]')
print(my_list)