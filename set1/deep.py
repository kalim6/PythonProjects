deep = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
deep = deep.lower().strip()

valid_responses = ["42", "forty-two", "forty two"]

if deep in valid_responses:
    print("Yes")
else:
    print("No")
