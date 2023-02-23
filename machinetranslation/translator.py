""" Module defines a class to translate text
    Currenttly the translations are from:
    - french to english 
    - english to french """
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



class WatsonTranslator():
    def __init__(self):
        authenticator = IAMAuthenticator('1fMUSo7m19tAXb9uXJ011nAHeawx3OslXXna0CQC7cVc')
        self.language_translator = LanguageTranslatorV3(
            version='2021-05-01',
            authenticator=authenticator
        )

        self.language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/add117af-6f59-437c-9ad9-da04c9c35edc')


    def english_to_french(self, english_text):
        """Function translates am english text to french """
        translation = self.language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

        return translation['translations'][0]['translation']

        # return frenchText


    def french_to_english(self, french_text):
        """Function translated a french text to english """
        translation = self.language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

        return translation['translations'][0]['translation']