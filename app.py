from flask import Flask
from flask import render_template # this function combines data w HTML to make webpage
app = Flask(__name__)

@app.route("/") # flask decorator connecting index function below with root URL, /

def index(): # function returns the rendered index.html template
	template = "index.html"
	return render_template(template)

if __name__ == '__main__':
	# launch flask test server
	app.run(debug=True, use_reloader=True)
	
