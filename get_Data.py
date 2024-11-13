import get_Date as getDate
import get_and_set_env
import set_api_values
import requests
import download_kaggle_dataset
import pandas as pd
import os

def call_Api():
    API_KEY = get_and_set_env.returnAPiKey()
    date_string_dash = getDate.get_Date()
    languageUserInput = set_api_values.setLanguage()
    topicUserInput = set_api_values.setTopic()
    # # test
    # languageUserInput = 'en'
    # topicUserInput = 'cars'

    # Call APi
    url = f'https://newsapi.org/v2/everything?q={topicUserInput}&from={date_string_dash}&sortBy=publishedAt&apiKey={API_KEY}&language={languageUserInput}'
    response = requests.get(url)
    # print(f'The url consulted is: {url}')

    if response.status_code == 200:
        news = response.json()
        if not news.get('articles'):
            print('No articles found for the given query.')
            return None
        print('All good')

    # print(response)
    if response.status_code == 200:
        news = response.json()
        print('All good')
    else:
        print('Something terrible happened')
    print(' ')
    print(languageUserInput)

    # Call the function to get data from kaggle
    get_DataCSV()

    return news

# def get_DataCSV():
def get_DataCSV():
    languageUserInput = get_and_set_env.returnLanguageKey()
    match languageUserInput:
        case "en":
            item = 'clovisdalmolinvieira/news-sentiment-analysis'

        case "pt":
            item = 'mateuspicanco/financial-phrase-bank-portuguese-translation'

        case "de":
            item = 'matthiasse/german-news-headlines-politics-and-economics'

        case "es":
            item = 'chizhikchi/andalusian-hotels-reviews-unbalanced'

        case "it":
            item = 'mcantoni81/fake-news-the-gubbio-raw-fish-incident'

        case "zh":
            item = 'hkjianhui/baba-news-data'

        case "fr":
            item = 'hbaflast/french-twitter-sentiment-analysis'

        case "nl":
            item = 'maxscheijen/dutch-news-articles'

        case _:
            item = ''

    if not item:
        print('No dataset found for the given language.')
        return None

    namefile = download_kaggle_dataset.set_kaggle_file(item)

    if not namefile:
        print('No dataset found for the given language.')
        return None

    def get_latest_file(directory):
        files = os.listdir(directory)
        paths = [os.path.join(directory, basename) for basename in files]
        latest_file = max(paths, key=os.path.getmtime)
        return os.path.basename(latest_file)

    latest_file = get_latest_file('data')
    print(f'Latest modified file: {latest_file}')
    print('')

    # Reading the CSV file
    data = pd.read_csv(f'data/{latest_file}')

    return data
