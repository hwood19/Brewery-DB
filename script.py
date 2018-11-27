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
        found_result = False
        for row in csv_reader:
            if input_brewery.upper() == row[0].upper():
                found_result = True
                return ("{name} in {row} has a {rating} Google rating."
                        .format(name=row[0], row=row[1], rating=row[2]))

    if not found_result:
        return "Specified brewery was not found."


@app.route('/')
def home():
    return render_template("home.html", beersearch="")


if __name__ == "__main__":
    app.run(debug=True)
