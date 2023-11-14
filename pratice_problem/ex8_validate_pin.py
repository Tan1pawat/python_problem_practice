# my_solution

# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         return all(x.isdigit() for x in pin)
#     else:
#         return False

# better solution

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin("090909"))
