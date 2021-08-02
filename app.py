# from translate import Translator
from googletrans import Translator
from flask import Flask, render_template, request

translator = Translator()

app = Flask(__name__)


@app.route('/')
def home_page():
    example_embed = 'This string is from python'
    return render_template('index.html', embed=example_embed)


@app.route('/<string:translang>', methods=['POST', 'GET'])
def submit_form(translang):
    if request.method == 'POST':
        data = request.form.to_dict()
        if data["text"] is "":
            return render_template('index.html', embed1=data["text"], embed2="Please enter a valid text")
        trans_text = translator.translate(data["text"], dest=translang).text
        return render_template('index.html', embed1=data["text"], embed2=trans_text)

# translator = Translator()
# print(translator.translate("Hello! How are you?").text)
