from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return machinetranslation.translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return machinetranslation.translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.hml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
