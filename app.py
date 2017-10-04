from flask import Flask,render_template, request, session

app = Flask (__name__)

userCode = "sasha"
passCode = "manahal"

@app.route('/', methods = ['POST', 'GET'])

def root():
    return render_template('form.html')


@app.route('/welcome', methods = ['POST', 'GET'])

def welcome():
    if request.form[username] == userCode and request.form[passCode] == passCode:    
        return render_template(


if __name__ == '__main__':
    app.run(debug= True)
    
