## Regular way of creating a list


def create_list(words):
    codes = []
    for word in words:
        codes.append(ord(word))
    return codes


result = create_list("FjhjFUYKJNKl")
print(result)

## List Comprehension way (2 lines of code)

symbols = "FjhjFUYKJNKl"
print([ord(symbol) for symbol in symbols])  ## A very simple list comprehension example
