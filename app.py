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
	
@app.route("/<row_id>/")	# see how that works, contrast w one before index function.
def detail(row_id):
		template = "detail.html"
		object_list = get_csv()
		for row in object_list:
			if row["id"] == row_id:
				return render_template(template, object = row)
# above note both url route and function take an argument, row_id.
# goal is for number passed to URL to go into the function where it will be used to 
# pull the corresponding ID from the csv. then we'll pass that to the template to render the unique page.


if __name__ == '__main__':
	# launch flask test server
	app.run(debug=True, use_reloader=True)
	
