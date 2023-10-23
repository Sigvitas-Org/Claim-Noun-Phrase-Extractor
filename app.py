from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        input_text = request.form['input_text']
        doc = nlp(input_text)
        noun_phrases = [chunk.text for chunk in doc.noun_chunks]

        return render_template('index.html', input_text=input_text, noun_phrases=noun_phrases)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
