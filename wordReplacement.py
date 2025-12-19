def word_replacement():
    str = "I build this program to let you replace word"
    replacement = input("Replace: ")
    replaced_to = input("To: ")

    print(str.replace(replacement,replaced_to))
word_replacement()