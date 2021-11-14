# Name:
# Email ID:

def get_relation_through_link(family_dict, link):
    # Modify the code below.

    # Check direct relation
    if (link[0], link[len(link) - 1]) in family_dict:
        return family_dict[(link[0], link[len(link) - 1])]

    rs_list = []
    # Check for indirect relation
    while len(link) > 1:
        rs_list.append(family_dict[(link[0], link[1])])
        link.pop(0)

    # populate relation_mapping into dict for easy search
    rm = {}
    with open('relation_mapping.txt', 'r') as f:
        for line in f:
            line_split = line.strip().split(':')
            comp, rs = line_split[0], line_split[1]
            a, b = comp.replace('(', '').replace(')', '').split(',')
            rm[(a, b)] = rs

    # Check the relation
    prev_rs = ''
    while len(rs_list) > 1:
        if prev_rs == '':
            prev_rs = rm[(rs_list[0], rs_list[1])]
            rs_list.pop(0)
        else:
            cur_rs = rm[(rs_list[0], rs_list[1])]
            if prev_rs == 'wife':
                prev_rs = rm[(prev_rs, 'son')]
                rs_list.pop(0)
            else:
                prev_rs = rm[(prev_rs, 'cur_rs')]
                rs_list.pop(0)

    return prev_rs
