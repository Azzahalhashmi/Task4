#authenticate
url='https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/cfebd5f9-f842-46d4-b2db-a6fdf4f468d1'
apikey='6JAnhPhd0pLzNcP1qXUt8MYB5D8__X6JpjZ7Ge3BEiKC'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
tts=TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

#convert a string
with open('./TextToSpeechResult.mp3','wb')as audio_file:
    res=tts.synthesize('Hello Smart Method World',accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
