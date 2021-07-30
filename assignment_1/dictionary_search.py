import requests

try:
    word = input("Word: ")
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/' + word
    res = requests.get(url)

    result = word.title() + ". Noun. "

    data = res.json()[0]['meanings']

    for meaning in data:
        if meaning['partOfSpeech'] == 'noun':
            ans = meaning['definitions'][0]['definition']
            result = result + ans
            break

    print(result)

except Exception as e:
    print(e)