def validate(pin):
    return len(pin) in (4,6) and pin.isdigit()


pin=input("lalalal:")


validate(pin)

#with regex solution!

import re

def validate_pin(pin):
    return bool(re.fullmatch("\d{4}|\d{6}",pin))

#maybe with

def validate_pin(pin):
    return len(pin in (4,6) and all(p in '0123456789' for p in pin)

validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()
