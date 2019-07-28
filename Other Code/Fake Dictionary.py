# A novice attempts to create a simple language dictionary

# The database is English language centered, the key is in English and the values are in order as follow: French, Bulgarian, Italien, Russian.

import sys

database = {'cat': {'french': 'le chat', 'bulgarian': 'Боца!', 'italian': 'il gatto', 'russian': 'кошка', 'german': 'katze'},
         'dog': {'french': 'le chien', 'bulgarian': 'куче', 'italian': 'il cane', 'russian': 'собака', 'german': 'der hund'},
         'mouse': {'french': 'la souris', 'bulgarian': 'мишка', 'italian': 'il mouse', 'russian': 'мышь' , 'german': 'die maus'},
         'bear': {'french': 'l\'ourse', 'bulgarian': 'Ники', 'italian': 'il orso' , 'russian': 'медведь' , 'german': 'der bär'},
         'kitten': {'french': 'le chaton', 'bulgarian': 'котенце', 'italian': 'il gattino' , 'russian': 'котенок' , 'german': 'das kätzchen'},
         'puppy': {'french': 'le chiot', 'bulgarian': 'кученце', 'italian': 'il cucciolo' , 'russian': 'щенок' , 'german': 'der welpe'},
         'chicken': {'french': 'le poulet', 'bulgarian': 'кокошка', 'italian': 'il pollo' , 'russian': 'курица' , 'german': 'das hähnchen'},
         'lion': {'french': 'le lion', 'bulgarian': 'лъв', 'italian': 'il leone' , 'russian': 'лев' , 'german': 'der löwe'},
         'lynx': {'french': 'le lynx', 'bulgarian': 'рис', 'italian': 'la lince' , 'russian': 'рысь' , 'german': 'der luchs'},
         'puma': {'french': 'le puma', 'bulgarian': 'пума', 'italian': 'il puma' , 'russian': 'пума' , 'german': 'der puma'},
         'tiger': {'french': 'le tigre', 'bulgarian': 'тигър', 'italian': 'la tigre' , 'russian': 'тигр' , 'german': 'der tiger'},
         'zebra': {'french': 'le zèbre', 'bulgarian': 'зебра', 'italian': 'la zebra' , 'russian': 'зебра' , 'german': 'das zebra'},
         'ladybird': {'french': 'la coccinelle', 'bulgarian': 'Баба Калинка' , 'italian': 'la coccinella' , 'russian': 'божья коровка' , 'german': 'der marienkäfer'},
         'pig': {'french': 'le cochon', 'bulgarian': 'прасе', 'italian': 'il maiale' , 'russian': 'свинья' , 'german': 'das schwein'},
         'wolf': {'french': 'le loup', 'bulgarian': 'вълк', 'italian': 'il lupo' , 'russian': 'волк' , 'german': 'der wolf'},
         'whale': {'french': 'une baleine', 'bulgarian': 'кит', 'italian': 'la balena' , 'russian': 'кит' , 'german': 'der wal'},
         'fish': {'french': 'le poisson', 'bulgarian': 'риба', 'italian': 'il pesce' , 'russian': 'рыба' , 'german': 'der fisch'},
         'panda': {'french': 'le panda', 'bulgarian': 'панда', 'italian': 'il panda' , 'russian': 'панда', 'german': 'der panda'},
         'skunk': {'french': 'la moufette', 'bulgarian': 'скункс', 'italian': 'la puzzola' , 'russian': 'скунс' , 'german': 'das stinktier'},
         'pussy': {'french': 'la chatte', 'bulgarian': 'путка', 'italian': 'la figa' , 'russian': 'киска', 'german': 'die muschi'}}

print('Welcome to the best "English to ..." dictionary ever!')
print('Please select to which language you would like to translate.')
print()
print('You have the following options:\n\n[1] English to French\n[2] English to Bulgarian\n[3] English to Italian\n[4] English to Russian\n[5] English to German')
print()

while True:
    print('Please make your choise by typing in the language name.')
    language = input()
    language2 = language.lower()
    if language2 not in ('french', 'bulgarian', 'italien', 'russian', 'german'):
        print('Please type in a valid language selention (French, Bulgarian, Italian, Russian or German)')
        print()
        continue
    else:
        print('Thank you for you selection')
        print()
    print('Please type in the word you want to translate into ' + language2 + ' or type in EXIT to quit the program.')
    word = input()
    print()
    if word.lower() in database.keys():
        print(word + ' translates to "' + database[word][language2] + '" in ' + language2 + '.')
        print()
    elif word == 'EXIT':
        print('Thank you for using the best dictionary ever. Have a great day!')
        sys.exit()
    else:
        print('Unfortunately, "' + word + '" is not a word that the dictionary can recognize.')
        continue
    while True:
        print('If you want to translate another word please type it in.\nIf you want to quit the program type EXIT.\nIf you want to translate to another language please type in LANGUAGE:')
        decision = input()
        if decision == 'EXIT':
            print('Thank you for using the best dictionary ever. Have a great day!')
            sys.exit()
        elif decision.lower() in database.keys():
            print(decision + ' translates to "' + database[decision][language2] + '" in ' + language2 + '.')
            print()
            continue
        elif decision == 'LANGUAGE':
            break
        break
