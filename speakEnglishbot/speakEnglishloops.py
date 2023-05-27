import requests
import json

app_id = "8e445cdd"
app_key = "6ad98cfbeb1db383a5ff2a25ace6501c"
language = "en-gb"

def speakenglish(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    responce = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    responce = responce.json()
    if 'error' in responce.keys():
        return False
    output = {}
    senses = responce['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if responce['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']:
        output['auido'] = responce['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output

if __name__ == '__main__':
    answer_msg = speakenglish('word')
    print(answer_msg['definitions'])
    print(answer_msg['auido'])

