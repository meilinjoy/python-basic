#!/usr/bin/python3
from gettext import translation
from urllib import response
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from matplotlib.pyplot import text
url_s2t = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/2402681c-9103-4699-8189-93d915a16e7b'
iam_apikey_s2t = 'z5D-4oDKO4tyCbeL1xNfyVxoRc8vAYlU07_dUZqSmhY8'

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
#print(s2t)
filename='PolynomialRegressionandPipelines.mp3'



with open(filename,mode='rb') as wav:
    #print(wav,'))))))))))))))')
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    #print(response.result,"-----")

from pandas import json_normalize
json_normalize(response.result['results'],"alternatives")

recognized_text = response.result['results'][0]['alternatives'][0]["transcript"]
print(recognized_text)

from ibm_watson import LanguageTranslatorV3
#url_lt = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/927b56b0-7fa1-4b2d-bbf3-49053bf3e6f8'
url_lt = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/2402681c-9103-4699-8189-93d915a16e7b'
apikey_lt = 'z5D-4oDKO4tyCbeL1xNfyVxoRc8vAYlU07_dUZqSmhY8'
#apikey_lt = '00ElBaRxalZWZ6c4yZE6ysl5jQUpCw0btphl5b2R6qQu'
version_lt = '2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
Language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
Language_translator.set_service_url(url_lt)
#print(Language_translator,'----')

from pandas import json_normalize
json_normalize(Language_translator.list_identifiable_languages().get_result,'languages')

translation_response = Language_translator.translate(text=recognized_text,model_id='en-es')
translation=translation_response.get_result()
spanish_translation =translation['translations'][0]['translation']
 
translation_new = Language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
translation_eng=translation_new['translations'][0]['translation']

print(translation_eng,'====')


