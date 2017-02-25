import json
import counting
from shape_base import shape_filtred_base
from shape_base import shape_main_base
from graph import plt_histogram

if __name__ == '__main__':
    url = 'https://api.superjob.ru/2.0/oauth2/password/'
    print('Input your secret key:')
    client_secret = input()
    vacancy_url = 'https://api.superjob.ru/2.0/vacancies/'

    shape_main_base(url, vacancy_url, client_secret)
    print ('You can find full base in file \"vacancy_base\".json')

    shape_filtred_base()
    print ('You can find filtred base in file \"filtred_base_of_vacancy\".json')

    base = json.load(open('filtred_base_of_vacancy.json', encoding = 'utf8'))
    languages_dict = {'C++': [0, 0, 0], 'JavaScript': [0, 0, 0], 'Python': [0, 0, 0], 'PHP': [0, 0, 0],
            ' C ': [0, 0, 0],  'C#': [0, 0, 0], ' Java ': [0, 0, 0],  '1С': [0, 0, 0], 'Delphi': [0, 0, 0]}

    languages = ['C++', 'JavaScript', 'Python', 'PHP', ' C ', 'C#', ' Java ', '1С', 'Delphi']

    for object in base:
        payment = counting.calc_payment(object)
        candidate = str(object['candidat']).lower()
        for language in languages:
            counting.calc_vacancies(candidate, languages_dict, language, payment)

    sorted_base = sorted(languages_dict.items(), key=lambda a: a[1], reverse=True)
    x, y = [], []
    for i in range(len(sorted_base)):
        print('Language :', sorted_base[i][0])
        print('Number of vacancies :', sorted_base[i][1][0])
        if sorted_base[i][1][2] !=0:
            print('<Salary> :', round(sorted_base[i][1][1]/sorted_base[i][1][2]))
            y.append(round(sorted_base[i][1][1]/sorted_base[i][1][2]))
            x.append(i + 1)

    plt_histogram(sorted_base, x, y)
