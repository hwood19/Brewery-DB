from flask import Flask, render_template, request
import csv
app=Flask(__name__,static_folder='static', static_url_path='css/static.css'))
@app.route('/greet', methods=['POST'])
def greet():
    inputBrewery = request.form['beersearch']
    inputBrewery = inputBrewery.upper()
	with open("Brewerylist.csv") as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',')
		line_count = 0
		found_result = False
		for row in csv_reader:
			if inputBrewery == row[0]:
				found_result = True
				print(row[0] + " in " + row[1] + " has a " + row[2] + " rating.")
		
	if found_result == False:
		print("Specified brewery was not found.");

@app.route('/')
def home():
    
    return render_template("home.html",beersearch="")

if __name__=="__main__":
    app.run(debug=True)
