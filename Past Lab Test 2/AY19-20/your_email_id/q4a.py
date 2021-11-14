# Name:
# Email ID:

def store_family_relations(family_file):
    # Modify the code below.
    with open(family_file, 'r') as family:
        family_dict = {}
        for line in family:
            split_line = line.strip().split(':')
            parents, children = split_line[0], split_line[1]
            parents = parents.replace('(', '').replace(')', '').split(',')
            father, mother = parents[0], parents[1]
            children = children.split(';')

            # get child and gender and add them into fam dict
            for child in children:
                child = child.strip().replace('(', '').replace(')', '').split(',')
                name, gender = child[0], child[1]

                # Populate the parents into fam_dict first
                family_dict[(father, name)] = 'father'
                family_dict[(mother, name)] = 'mother'

                # Populate the fam dict with parent child
                if gender == 'M':
                    family_dict[(name, father)] = 'son'
                    family_dict[(name, mother)] = 'son'
                elif gender == 'F':
                    family_dict[(name, father)] = 'daughter'
                    family_dict[(name, mother)] = 'daughter'
                
    return family_dict
    