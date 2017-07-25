import csv
from flask import Flask
from flask import render_template # this function combines data w HTML to make webpage
app = Flask(__name__)

def get_csv():
	csv_path = "./static/la-riots-deaths.csv"
	csv_file = open(csv_path, "rb")
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return(csv_list)

@app.route("/") # flask decorator connecting index function below with root URL, /

def index(): # function returns the rendered index.html template
	template = "index.html"
	object_list = get_csv()
	return render_template(template, object_list = object_list)
	

if __name__ == '__main__':
	# launch flask test server
	app.run(debug=True, use_reloader=True)
	
