from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__) # Flask is a class

base_path = pathlib.Path().cwd()
db_name = "employee_details.db"
file_path = base_path / db_name


@app.route("/")
def index():
    return render_template( "index_fillin.html")

@app.route("/about")
def about():
    return render_template( "about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    employees = cursor.execute("SELECT * FROM employees").fetchall()
    con.close()
    return render_template( "data_table_fillin.html", employees = employees)


if __name__=="__main__":
    app.run(debug=True)