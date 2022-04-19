from flask import Flask, redirect, render_template,request, url_for
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer

model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/summarizer", methods = ['GET','POST'])
def summarizerPage():
    if request.method == 'POST':
        return redirect(url_for('index'))

    print("Hello")
    return render_template('summary.html')

@app.route("/summarize",methods=['POST','GET'])
def getSummary():
    print("hello")
    body=request.form['data']
    print(body)
    result = model(body, num_sentences=2)
    print("hello")
    print(result)
    return render_template('summarizer.html',result=result)
    # return render_template('summary.html',result=result)
if __name__ =="__main__":
    app.run(debug=True,port=8000)