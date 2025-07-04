from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection Setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishikesh@astha"
)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        action = request.form.get("action")
        username = request.form.get("username")
        password = request.form.get("password")
        privilege = request.form.get("privilege")

        try:
            if action == "create":
                cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")
                db.commit()
                message = f"Success: User '{username}' has been created successfully."
                print(f"[INFO] User Creation: {message}")

            elif action == "grant":
                cursor.execute(f"GRANT {privilege} ON *.* TO '{username}'@'localhost';")
                cursor.execute("FLUSH PRIVILEGES;")
                db.commit()
                message = f"Success: Privilege '{privilege}' has been granted to user '{username}'."
                print(f"[INFO] Grant Privilege: {message}")

            elif action == "revoke":
                cursor.execute(f"REVOKE {privilege} ON *.* FROM '{username}'@'localhost';")
                cursor.execute("FLUSH PRIVILEGES;")
                db.commit()
                message = f"Success: Privilege '{privilege}' has been revoked from user '{username}'."
                print(f"[INFO] Revoke Privilege: {message}")

        except Exception as e:
            message = f"Error: {str(e)}"
            print(f"[ERROR] Exception occurred: {message}")

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
