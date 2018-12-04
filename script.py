from flask import Flask, render_template, request
import csv

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/greet', methods=['POST'])
def greet():
    input_brewery = request.form['beersearch']
    input_brewery = input_brewery.upper()
    with open("Brewerylist.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if input_brewery == row[0].upper():
                result_string = "{name} in {row} has a {rating} Google rating. Their best seller is their {beer} which is a {type}. Try it out"
                result_string = result_string.format(name=row[0], row=row[1], rating=row[2], beer=row[3], type=row[4])                        
                return render_template('home.html', data=result_string)
				
    return render_template('home.html', data="Specified brewery was not found.")


@app.route('/')
def home():
    return render_template("home.html", beersearch="")


if __name__ == "__main__":
    app.run(debug=True)
