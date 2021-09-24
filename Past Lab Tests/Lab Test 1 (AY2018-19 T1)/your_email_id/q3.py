#
# Name: 
# Email ID: 
#
def mask_out(sentence, banned, substitutes):
    # write your answer between #start and #end
    #start
    for i, b  in enumerate(banned):
        if i > len(substitutes) - 1:
            sentence = sentence.replace(b, substitutes[0])
        else:
            sentence = sentence.replace(b, substitutes[i])
    return sentence
    #end


print('Test 1')
print('Expected:abcd#')
print('Actual  :' + mask_out('abcde', 'e', '#'))
print()

print('Test 2')
print('Expected:#$solute')
print('Actual  :' + mask_out('absolute', 'ab', '#$'))
print()

print('Test 3')
print('Expected:121hon')
print('Actual  :' + mask_out('python', 'pyt', '12'))
print()





