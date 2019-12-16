from flask import Flask , render_template , jsonify
from flask_pymongo import PyMongo 
from flask import redirect
from bson.objectid import ObjectId
from flask import request

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://sulemanahmed:sulemanahmed@cluster0-v2lke.mongodb.net/test?retryWrites=true&w=majority'
app.config['MONGO_DBNAME'] = 'cluster0'
mongo = PyMongo(app)

#Task_id = ObjectId()
#print(task_id)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/todo/api/v1.0/tasks",methods = ["GET"])
def get_all_task():
	rezult = []
	task_db = mongo.db.tasks
	if task_db.count_documents({}) > 0:
		for task in task_db.find():
			rezult.append({"id":str(task["_id"]),"title":task["title"],"description":task["description"],"done":task["done"]})

	return jsonify({"tasks":rezult})

@app.route("/todo/api/v1.0/tasks/[task_id]",methods = ["GET"])
def get_task(task_id):
	rezult = []
	tasks = mongo.db.tasks.find_one_or_404({"_id" : ObjectId("5decb8d5c088e69dd604c7df")})
	rezult.append({"id":str(task["_id"]),"title":task["title"],"description":task["description"],"done":task["done"]})
	return jsonify({"tasks":rezult})


	
@app.route("/todo/app/v1.0/tasks/[task_id]" , methods = ["POST"])
def create_task():
	title = request.json.get('title',"")
	description = request.json.get("description","")
	task_db = mongo.db.tasks
	new_task_id = db_task.insert({"title":title,"description":descripttion,"done":False})
	return jsonify({"id":str(new_task_id)})

@app.route("/todo/api/v1.0/tasks/<ObjectId:task_id>", methods = ['PUT'])
def update_task(task_id):
    db_task = mongo.db.tasks
    task = db_task.find_one_or_404({"_id": task_id})

    title = request.json.get("title", task["title"])
    description = request.json.get('description', task["description"])
    done = bool(request.json.get("done", task["done"]))

    task[0]["title"] = title
    task[0]["description"] = description
    task[0]["done"] = done
    db_task.save(task)
    response = {'status': 'success', 'status_code': '200',
                 'message': 'Task Updated'}

    return jsonify({'response': response})

@app.route("/todo/api/v1.0/tasks/<ObjectId:task_id>",methods=['DELETE'])
def delete_task(task_id):
	mongo.db.task.find_one_or_404({"_id":task_id})
	mongo.db.task.delete_one({"_id":task_id})
	response = {'status':'success','status_code':'200','message':'Task Deleted'}
	return jsonify({'response':response})

@app.errorhandler(404)
def not_found(error):
	response = {"status": "error", "status_code": "404", "message": "Not Found"}
	return jsonify({"response": response})


if __name__ == "__main__":
	app.run(debug = True)

