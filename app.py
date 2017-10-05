from flask import Flask,render_template, request, session

app = Flask (__name__)

app.secret_key = 'secret'

userCode = "sasha"
passCode = "manahal"



@app.route('/', methods = ['POST', 'GET'])

def root():
    if session.has_key('user'):
        return render_template('welcome.html', name= session['user'])
    else:
        return render_template('form.html')


@app.route('/welcome', methods = ['POST', 'GET'])

def welcome():
    
    currentUser = request.form['username']
    currentPass = request.form['password']
                               
    if currentUser  == userCode and currentPass == passCode:
        session['user'] = currentUser
        return render_template('welcome.html', name = currentUser)

    
    elif currentUser != userCode:  
        return render_template('error.html', errorMsg = "Username is wrong!")

    
    else:
        return render_template('error.html' , errorMsg = "Password is wrong!")

@app.route('/logOut' , methods = ['POST', 'GET'])

def logOut():
    #print "SFDFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
    #session.clear()
    session.pop('user')
    return render_template('logOut.html')
    

if __name__ == '__main__':
    app.run(debug= True)
    
