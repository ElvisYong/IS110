def get_average_duration(items):
    duration = 0
    if items:
        for i in items:
            duration += i[2] 
        return duration/len(items)
    return 0.0

def get_num_movies_of_genre(items, genre):
    count = 0
    if items:
        for i in items:
            if i[1] == genre:
                count += 1
        return count
    return 0

def get_title_of_longest_movie(items):
    if items:
        longest_length = 0
        longest_title = ''
        for i in items:
            if len(i[0]) > longest_length:
                longest_length = len(i[0])
                longest_title = i[0]
        return longest_title
    return ''

def get_movies_with_keyword(items, keyword):
    if items:
        for i in items:
            if keyword in i[0]:
                print(i[0], i[1], i[2])