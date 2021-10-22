def extract_data(python_filename, output_filename):
    function_dict = {}
    function_name = ''
    start_doc = False

    with open(python_filename, 'r') as rf:
        for line in rf:
            if line.startswith('def'):
                function_name = line.replace('def', '')
                function_name = function_name.replace(':', '')
                function_dict[function_name] = [function_name]

            elif line.strip().startswith('"""') and line.strip().endswith('"""') and line.lower().islower() == True:
                function_dict[function_name].append(line)
                continue

            elif '"""' in line and start_doc == False:
                function_dict[function_name].append(line)
                start_doc = True

            elif line.rstrip().endswith('"""') and start_doc == True:
                function_dict[function_name].append(line)
                start_doc = False
                continue
            
            elif start_doc:
                function_dict[function_name].append(line)
    
    with open(output_filename, 'w') as wf:
        for count, item in enumerate(function_dict.items()):
            if count == 0:
                wf.write(str(count + 1) + '. ' + item[1][0].strip() + '\n')
            else:
                wf.write('\n' + str(count + 1) + '. ' + item[1][0].strip() + '\n')

            for line in item[1][1:]:
                if line.strip() == '"""':
                    continue
                else:
                    if '"""' in line:
                        line = line.replace('"""', '')
                    wf.write('    ' + line.strip() + '\n')

        
extract_data('python_script.py', 'q6_output.txt')