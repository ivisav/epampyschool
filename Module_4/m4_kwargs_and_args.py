# *args
def student_score(name, *scores):
    print(f"The student: {name}\nScore:")
    for score in scores:
        print(score)


student_score('Mike', 5, 3, 5, 4)


#   **kwargs
def describe_pets(owner, **pets):
    print(f"Name of the owner:  {owner}")
    for breed, name in pets.items():
        print(f"{breed} : {name}")


describe_pets('Igor', Aussie="Meonia", Shepherd="Grace")
