# rules for finding a closure

    # we must have a nested function
    # the nested function should reference a value of a higher scope
    # the function that wraps the nested must return it too
    
    # when we have a class that has only one method  when we work with decorators


def make_multiplaier(x):

    def multiplaier(n):
        return x * n

    return multiplaier

times10 = make_multiplaier(10)
times4 = make_multiplaier(4)

# print(times10(3))
# print(times4(5))
# print(times10(times4(2)))


def repeater_word(n):
    def repeater(string):
        assert type(string) == str, "solo puedes usar strings"
        return string * n

    return repeater

def make_division_by(n):
    def division(x):
        assert type(x) == int
        return x // n
    return division


def run():
    # repeat = repeater_word(10)
    # print(repeat("Hi!"))
    div_by_3 = make_division_by(3)
    print(div_by_3(18))
    div_by_5 = make_division_by(5)
    print(div_by_5(100))



if __name__ == "__main__":
    run()
