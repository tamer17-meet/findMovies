from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def mainpage():
	return render_template('movies.html')

@app.route('/8')
def The_Transporter():	
    return render_template('TheTransporter.html')


@app.route('/7')
def Crank():	
    return render_template('crank.html')



@app.route('/Movies/')
def TheWolfOfWallStreet():
	return render_template('TheWolfOfWallStreet.html')


@app.route('/6')
def salt():
	return render_template('salt.html')


@app.route('/5')
def wanted():
	return render_template('wanted.html')


@app.route('/4')
def TheDeparted():
	return render_template('TheDeparted.html')


@app.route('/3')
def WelcomeToThePunch():
	return render_template('WelcomeToThePunch.html')


@app.route('/2')
def Movies():
	return render_template('minorityreport.html')


@app.route('/1')
def XXX():
	return render_template('XXX.html')





if __name__ == '__main__':
    app.run(debug=True)