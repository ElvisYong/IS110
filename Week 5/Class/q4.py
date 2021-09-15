def get_avg_len(item: list) -> float:
    """
    Get average length of item
    :param item: list
    :return: int
    """
    if item:
        return sum(len(i) for i in item) / len(item)
    return 0


print(get_avg_len(["C", "Java", "Python", "PHP"]))
print(get_avg_len([]))


def get_longest_str(item: list) -> str:
    """
    Get longest string in item
    :param item: list
    :return: string
    """
    if item:
        return max(item, key=len)
    return ""


print(get_longest_str(["C", "Java", "Python", "PHP"]))
print(get_longest_str([]))
print(get_longest_str(["C", "Java", "HTML", "PHP"]))


def concatenate_emails(item: list) -> str:
    """
    Concatenate emails
    :param item: list
    :return: string
    """
    if item:
        concat_string = ''
        for s in item:
            if ' ' not in s and s.count('@') == 1:
                concat_string += s + ';'
        return concat_string
    return ""


my_list1 = ["tommy.goh@sis.smu.edu.sg", "alan_wong@gmail.com"]
print(concatenate_emails(my_list1))
my_list2 = []
print(concatenate_emails(my_list2))
my_list3 = ["IS111", "a @ b", "jerry.lee@sis.smu.edu.sg", "@@@",
            "alan_wong@gmail.com", "Python", "george_tan@yahoo.com"]
print(concatenate_emails(my_list3))


def check_hashtags(item: list) -> bool:
    if all('#'in s and ' ' not in s for s in item) and item != []:
        return True
    return False

print(check_hashtags(["#singapore", "#music", "#travel"]))
print(check_hashtags([]))
print(check_hashtags(["#singapore", "#music album", "#travel"]))
print(check_hashtags(["singapore", "#music", "#travel"]))
