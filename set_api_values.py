# import json
import get_and_set_env

def setLanguage():
    # Select the language
    print()
    languageUserInput = input('Input the language: \n ar (arabic) \n de (german) \n en (english) \n es (spanish) \n fr (french) \n it (italian)\n nl (dutch) \n pt (portuguese) \n zh (chinese)\n \n').lower()

    while (languageUserInput not in language_dict):
        if languageUserInput in language_dict:
            break
        else:
            print('Please input a valid language')
            print()

            languageUserInput = input('Input the language: \n de (german) \n en (english) \n es (spanish) \n fr (french) \n it (italian)\n nl (dutch) \n pt (portuguese) \n zh (chinese)\n \n').lower()

    # print(len(languageUserInput))
    # print(f'Language selected: {languageUserInput} \n')
    languageUserInput = languageUserInput.replace(" ", "")
    get_and_set_env.updateLanguageKey(languageUserInput)
    return languageUserInput

def setTopic():
    # Select the topic
    topicUserInput = input('Input the topic: ')
    topicUserInput = topicUserInput.replace(" ", "")
    get_and_set_env.updateTopicKey(topicUserInput)
    # print(f'Topic selected: {topicUserInput} \n')
    # print(len(topicUserInput))
    return topicUserInput

def returnLongLanguage():
    languageUserInput = get_and_set_env.returnLanguageKey()
    return language_dict[languageUserInput]

language_dict = {
    'de': 'german',
    'en': 'english',
    'es': 'spanish',
    'fr': 'french',
    'it': 'italian',
    'nl': 'dutch',
    'pt': 'portuguese',
    'zh': 'chinese'
}
