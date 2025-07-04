from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection config
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishikesh@astha",  
    database="bank_system"
)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        sender = int(request.form["sender"])
        receiver = int(request.form["receiver"])
        amount = float(request.form["amount"])
        
        try:
            cursor.callproc("transfer_money", (sender, receiver, amount))
            db.commit()
            # Redirect karenge yahan, taaki refresh pe dobara POST na ho
            return redirect(url_for('index', message="Transaction completed."))
        except Exception as e:
            db.rollback()
            return redirect(url_for('index', message="Transaction failed: " + str(e)))

    # GET request ke case me ya redirect ke baad
    # message query string se lene ke liye:
    message = request.args.get('message', '')

    # Show accounts
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()

    # Show transaction logs
    cursor.execute("SELECT * FROM transaction_log ORDER BY log_time DESC")
    logs = cursor.fetchall()

    return render_template("index.html", message=message, accounts=accounts, logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
