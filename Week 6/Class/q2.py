# def get_unique_titles(list_of_tuples):
#     title_set = {}
#     for books in list_of_tuples:
#         title = books[0]
#         if title not in title_set:
#             title_set[title] = 1
#         else:
#             title_set[title] += 1
#     return list(title_set)

def get_unique_titles(list_of_tuples):
    title_set = set()
    for books in list_of_tuples:
        title = books[0]
        if title not in title_set:
            title_set.add(title)
    return list(title_set)

print(get_unique_titles([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1", "paperback", 5), ("Intro to Programming", "Ed-3", "hardcover", 4)]) )

def get_titles_and_counts(list_of_tuples):
    title_set = {}
    for books in list_of_tuples:
        title, ed, cover, quantity = books
        if title not in title_set:
            title_set[title] = quantity
        else:
            title_set[title] += quantity

    return list(title_set.items())


print(get_titles_and_counts([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1", "paperback", 5), ("Intro to Programming", "Ed-3", "hardcover", 4), ("Intro to Python", "Ed-3", "hardcover", 3)]) )