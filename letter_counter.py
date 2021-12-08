

def letter_counter(text:str) -> dict:
    text = text.casefold()
    return {x: text.count(x) for x in set(text)}

print(letter_counter("Hello! Welcome to Python World!"))