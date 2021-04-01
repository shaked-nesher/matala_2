def revword(word: str) -> str:
    new_string = ""
    for char in word:
        new_string = char.lower() + new_string
    return new_string


def countword() -> int:
    file = open('text.txt', 'r+')
    lines=file.readlines()
    word = lines[0].split("\n")[0]
    counter = 1
    for line in lines[1:]:
        for wordinline in line.split(" "):
            if "\n" in wordinline:
                wordinline=wordinline.split("\n")[0]
            if revword(wordinline) == word:
                counter = counter + 1
    return counter


