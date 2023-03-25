import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))

def englishToFrench(englishText):
    try:
        frenchText = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        
        # print(json.dumps(frenchText, indent=2, ensure_ascii=False))
        frenchText = frenchText['translations'][0]['translation']
    except:
        frenchText = ''
    return frenchText


def frenchToEnglish(frenchText):
    try:
        englishText = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        
        # print(json.dumps(frenchText, indent=2, ensure_ascii=False))
        englishText = englishText['translations'][0]['translation']
    except:
        englishText = ''
    return englishText

# print(englishToFrench('How are you?'))
# print(frenchToEnglish('Comment es-tu?'))

# print(englishToFrench(''))