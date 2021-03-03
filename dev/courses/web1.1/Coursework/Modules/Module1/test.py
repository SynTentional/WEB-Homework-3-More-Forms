# Named parameters

def divide(numerator, denominator):
    return numerator / denominator

answer = divide(denominator = 6, numerator = 12)
print(answer)

def really_long_function(
        num_times,
        greeting,
        outro,age,
        show_greeting,
        show_outro):
    # do something with parameters
    pass

really_long_function(
    num_times = 10,
    greeting = 'hello',
    outro = 'goodbye',
    age = 25,
    show_greeting = True,
    show_outro = False
)