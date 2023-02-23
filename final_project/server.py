from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")
translator = WatsonTranslator()

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_to_french = translator.englishToFrench(textToTranslate)
    return translated_to_french
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_to_english = translator.englishToFrench(textToTranslate)
    return translated_to_english

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
