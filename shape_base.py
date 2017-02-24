import json
import requests

def shape_main_base( url, vacancy_url,  client_secret ):
    headers = {'X-Api-App-Id': client_secret}
    parameters_of_vacancy = {
        'town': 4,
        'catalogues': 48,
        'count': 100,
        'keyword': 'Программист'
    }
    dictionary_of_vacancy = json.loads(requests.get(vacancy_url, params=parameters_of_vacancy, headers=headers).text)
    with open('vacancy_base.json', 'w', encoding='utf-8') as search_file:
        json.dump(dictionary_of_vacancy, search_file, ensure_ascii=False)
    #return dictionary_of_vacancy


def shape_filtred_base():
    base = json.load(open('vacancy_base.json', encoding='utf8'))
    necessary_information = []
    for i in base['objects']:
        k = {
            'profession': i['profession'],
            'payment_from': i['payment_from'],
            'payment_to': i['payment_to'],
            'candidat': i['candidat']
        }
        necessary_information.append(k)
    new_base = open('filtred_base_of_vacancy.json', 'w', encoding='utf8')
    json.dump(necessary_information, new_base, ensure_ascii=False)
