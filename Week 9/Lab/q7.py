def get_lineup(info):
    current_person = ""
    res = []
    while len(res) != len(info):
        for people in info:
            front, back = people
            if back == current_person:
                res.insert(0, front)
                current_person = front
    return res


info = [("Mary", "Jason"), ("John", "Alan"), ("Jason", "George"), ("Alan", "Christie"), ("Christie", "Mary"), ("George", "")]

print(get_lineup(info))
