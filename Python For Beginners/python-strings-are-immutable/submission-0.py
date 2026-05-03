def remove_fourth_character(word: str) -> str:
    pass
    before4= word[:3]
    after4= word[4:len(word)]
    newword= before4+ after4
    
    return newword


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
