# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace('!', '') 

#print(remove_exclamation_marks("Oh, no!!!"))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == '!':
        return s[:-1]
    else:
        return s
print(remove_last_em("!Hi"))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    word_spisok = s.split(' ')
    word_spisok_new = []
    #print(word_spisok)
    for i in range(len(word_spisok)) :
        if word_spisok[i].count('!') != 1 :
            word_spisok_new.append(word_spisok[i])
            return (" ".join(word_spisok_new))

#print(remove_word_with_one_em("Hi! !Hi! Hi!"))
