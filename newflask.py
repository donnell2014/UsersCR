from flask import Flask, render_template, request, redirect
from mysqlconnect import connectToMySQL
app = Flask(__name__)


@app.route("/users")
def index():
    mysql = connectToMySQL('users_schema')   # call the function, passing in the name of our db
    users = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    print(users)
    return render_template("readall.html", all_users=users)

@app.route("/users/new", methods=["POST"])
def add_friend_to_db():
    mysql = connectToMySQL('users_schema')
    print(request.form)
    # mysql.query_db("INSERT INTO users_schema(first_name, last_name, email,created_at, updated_at) VALUES (fname from form, lname from form, email from form, NOW(), NOW())")
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
    data = {
        "fname":request.form['fname'],
        "lname":request.form['lname'],
        "email":request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/users')



@app.route("/users/new")
def addfriendhtml():
    return render_template('create.html')



if __name__ == "__main__":
    app.run(debug=True)

