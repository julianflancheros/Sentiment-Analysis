import os
import json
import get_and_set_env

def calljson():
    language = get_and_set_env.returnLanguageKey()
    # print('language:', language)

    # Directory containing the JSON files with test phrases
    test_phrases_dir = 'test_phrases'

    # List to hold all test phrases
    test_phrases = []

    # Iterate over all JSON files in the directory
    for filename in os.listdir(test_phrases_dir):
        if filename.endswith(f'{language}.json'):  # Match files with the language key
            filepath = os.path.join(test_phrases_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Assuming each JSON file contains a dictionary with a key 'test_phrases' that holds a list of phrases
                test_phrases.extend(data['test_phrases'])
    print("test_phrases", test_phrases)
    return test_phrases
