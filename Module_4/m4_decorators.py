def this_is_decorator(some_text):
    def text(speech):
        return [some_text(phrase[0], phrase[1]) for phrase in speech]
    return text


@this_is_decorator
def print_the_speech(name, some_text):
    saying = f"{name} says: '{some_text}'"
    return saying


print(print_the_speech([('Masha', 'bla bla?'), ('Misha', 'bla bla!')]))