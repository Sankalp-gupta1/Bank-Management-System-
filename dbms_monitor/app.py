from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# ✅ MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishikesh@astha",
    database="mysql_monitor"
)

# ✅ Monitor Route
@app.route("/monitor")
def monitor():
    cursor = db.cursor()

    cursor.execute("SHOW GLOBAL STATUS")
    status = cursor.fetchall()

    cursor.execute("SHOW VARIABLES")
    variables = cursor.fetchall()

    cursor.execute("SHOW FULL PROCESSLIST")
    processlist = cursor.fetchall()

    return render_template("monitor.html", status=status, variables=variables, processlist=processlist)

# ✅ Flask Run
if __name__ == "__main__":
    app.run(debug=True)
