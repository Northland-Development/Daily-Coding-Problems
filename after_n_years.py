def after_n_years(people, years):
    newDic = {}
    for person, age in people.items():
        newDic[person] = age+years
    return newDic


print(after_n_years({
    "Joel": 32,
    "Fred": 44,
    "Reginald": 65,
    "Susan": 33,
    "Julian": 13
}, 1))

print(after_n_years({
    "Baby": 2,
    "Child": 8,
    "Teenager": 15,
    "Adult": 25,
    "Elderly": 71
}, 19))

print(after_n_years({
    "Genie": 1000,
    "Joe": 40
}, 5)
)
