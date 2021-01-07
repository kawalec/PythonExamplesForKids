def takeCapital():
    dictionary = {}
    dictionary['Albania'] = 'Tirana'
    dictionary['Andora'] = 'Andora'
    dictionary['Austria'] = 'Wiedeń'
    dictionary['Belgia'] = 'Bruksela'
    dictionary['Białoruś'] = 'Mińsk'
    dictionary['Bośnia i Hercegowina'] = 'Sarajewo'
    dictionary['Bułgaria'] = 'Sofia'
    dictionary['Chorwacja'] = 'Zagrzeb'
    dictionary['Czarnogóra'] = 'Podgorica'
    dictionary['Czechy'] = 'Praga'
    dictionary['Dania'] = 'Kopenhaga'
    dictionary['Estonia'] = 'Tallin'
    dictionary['Finlandia'] = 'Helsinki'
    dictionary['Francja'] = 'Paryż'
    dictionary['Grecja'] = 'Ateny'
    dictionary['Hiszpania'] = 'Madryt'
    dictionary['Holandia'] = 'Amsterdam'
    dictionary['Irlandia'] = 'Dublin'
    dictionary['Islandia'] = 'Rejkiawik'
    dictionary['Liechtenstein'] = 'Vaduz'
    dictionary['Litwa'] = 'Wilno'
    dictionary['Luksemburg'] = 'Luksemburg'
    dictionary['Łotwa'] = 'Ryga'
    dictionary['Macedonia'] = 'Skopie'
    dictionary['Malta'] = 'Vallletta'
    dictionary['Mołdawia'] = 'Kiszyniów'
    dictionary['Monako'] = 'Monako'
    dictionary['Niemcy'] = 'Berlin'
    dictionary['Norwegia'] = 'Oslo'
    dictionary['Polska'] = 'Warszawa'
    dictionary['Portugalia'] = 'Lizbona'
    dictionary['Rosja'] = 'Moskwa'
    dictionary['Rumunia'] = 'Bukareszt'
    dictionary['San Marino'] = 'San Marino'
    dictionary['Serbia'] = 'Belgrad'
    dictionary['Słowacja'] = 'Bratysława'
    dictionary['Słowenia'] = 'Lublana'
    dictionary['Szwajcaria'] = 'Berno'
    dictionary['Szwecja'] = 'Sztokholm'
    dictionary['Ukraina'] = 'Kijów'
    dictionary['Watykan'] = 'Watykan'
    dictionary['Węgry'] = 'Budapeszt'
    dictionary['Wielka Brytania'] = 'Londyn'
    dictionary['Włochy'] = 'Rzym'
    return dictionary

def question(dictionary): 
    youTry = 0
    for i in range(len(dictionary)):
        key, value = dictionary.popitem()
        print('What is the capital of the country ' + key + '?')
        capital = input('You answer: ')
        if capital == value:
            youTry += 1
            print('Congratulations! Good answer.')
        else:
            print('You failed. Correct answer is ' + value + ".")
    print('The number of correct answers: ' + str(youTry) + '.')

def main():
    capital = takeCapital()
    question(capital)

main()