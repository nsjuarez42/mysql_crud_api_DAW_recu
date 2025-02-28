from flask import Flask,jsonify,request
from config import Development,Build
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config.from_object(Development)
mysql = MySQL(app)

def tuple_to_dict(tup):
    return {"title":tup[0],"description":tup[1],"category":tup[2],"status":tup[3],"id":tup[4]}

@app.route("/todos",methods=["GET","POST"])
def todos():
    if request.method == "GET":
        cursor = mysql.get_db().cursor()

        cursor.execute("SELECT * FROM todos")
        todos = [tuple_to_dict(t) for t in cursor.fetchall()]

        return jsonify({"todos":todos})

    elif request.method == "POST":
        cursor = mysql.get_db().cursor()


        title=request.json["title"]
        description=request.json["description"]
        status=request.json["status"]
        category=request.json["category"]
        print("Title {} description {} status {} category {}".format(title,description,status,category))

        cursor.execute("INSERT INTO todos(title,description,category,status,id) VALUES(%s,%s,%s,%s,NULL)",(title,description,category,status))
        mysql.get_db().commit()

        id = cursor.lastrowid
        print("Inserted id {}".format(id))

        cursor.execute("SELECT * FROM todos WHERE id=%s",(id))

        todo = cursor.fetchone()

        return jsonify({"msg":"Inserted successfully","todo":tuple_to_dict(todo)})

        


@app.route("/todo/<id>",methods=["PUT","DELETE","GET"])
def todo(id):

    if request.method == "PUT":
        cursor = mysql.get_db().cursor()

        title=request.json["title"]
        description=request.json["description"]
        status=request.json["status"]
        category=request.json["category"]

        cursor.execute("UPDATE todos SET title=%s,description=%s,status=%s,category=%s WHERE id=%s",(title,description,status,category,id))

        mysql.get_db().commit()
        
        cursor.execute("SELECT * FROM todos WHERE id=%s",(id))
        todo = cursor.fetchone()

        return jsonify({"msg":"Updated successfully","todo":tuple_to_dict(todo)})


        

    elif request.method == "DELETE":
        cursor = mysql.get_db().cursor()

        cursor.execute("SELECT * FROM todos WHERE id=%s",(id))

        todo = tuple_to_dict(cursor.fetchone())

        cursor.execute("DELETE FROM todos WHERE id=%s",(id))

        mysql.get_db().commit()
       
        return jsonify({"msg":"Deleted successfully","todo":todo})
        

    elif request.method == "GET":
        cursor = mysql.get_db().cursor()

        cursor.execute("SELECT * FROM todos WHERE id=%s",(id))

        return jsonify({"todo":tuple_to_dict(cursor.fetchone())})



if __name__ == "__main__":
    app.run(debug=True)
