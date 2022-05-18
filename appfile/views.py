from django.shortcuts import render

# function for translation
def translate(word):
    import requests
    API_KEY = '52309d6aa90c200fbe5f8b99465f2c93'
    API_ID = '14831ecd'

    headers = {
        "Accept": "application/json",
        "app_id": API_ID,
        "app_key": API_KEY
    }

    url = f"https://od-api.oxforddictionaries.com/api/v2/translations/en/hi/{word.lower()}?strictMatch=false&fields=translations"
    r = requests.get(url, headers=headers)
    hindi = r.json()["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['translations'][0]['text']

    url2 = f"https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/{word}?fields=definitions&strictMatch=false"
    r2 = requests.get(url2, headers=headers)
    define = r2.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]

    return hindi,define


# Create your views here.
def index(request):
    dict={}
    try:
        if request.method=="POST":
            word=request.POST.get('word')
            data=list(translate(word))
            dict={
                'word':word.title(),
                'hindi':data[0],
                'definition':data[1]
            }
    except KeyError:
        dict={
            'word': 'Enter correct',
            'hindi': 'not reachable',
            'definition':'not reachable'
        }
    return render(request,"index.html",context=dict)
