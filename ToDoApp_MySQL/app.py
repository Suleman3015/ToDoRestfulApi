from flask            import Flask, render_template
from flask_pymongo    import PyMongo 
from flask            import jsonify, redirect, json 
from flask_sqlalchemy import SQLAlchemy
from bson.objectid    import ObjectId
from flaskext.mysql import MySQL



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://suleman:Sulemanahmed3015@localhost/todo-py'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True
db = SQLAlchemy(app)

class Task(db.Model):
	__tablename__ = "tasks"
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(100))
	description = db.Column(db.Text)
	done = db.Column(db.Boolean , default=False)

	def __init__(self,title,description,done=False):
		self.title = title
		self.description = description 
		self.done = done

	def __repr__(self):
		return '<id{}>'.format(self.id)	

@app.route("/")
def index():
	return "<h1> TODO APP </h1>"

@app.route("/todo/api/v1.0/tasks",methods=['GET'])
def get_all_task():
	result = []
	tasks = Task.query.all()
	if tasks:
		for task in task_db:
			result.append({"id": str(task.id), 
				"title":task.title, 
				"description": task.description, 
				"done": task.done
				})

	return jsonify({"tasks": result})	



@app.route("/todo/api/v1.0/tasks/[task_id]",methods=["GET"])
def get_Task():
	rezult = []
	task = Task.query.filter_by().first()
	task_db = Task.query.all()
	if task_db:
		for task in task_db:
			rezult.append({
				"id": str(task.id),
			    "description": task.description,
			    "done": task.done
			    })
	return jsonify({"tasks": rezult} )
#	if task_db:
#		for task in task_db:
#			rezult.append({
#				"id": str(task.id),
#			    "description": task.description,
#			    "done": task.done
#			    })
#	return jsonify({"tasks": rezult} )
 #Read a specific task
#@app.route('/task/<id>', methods=['GET'])
#ef getTask(id):
#	return id		
		
@app.route("/todo/api/v1.0/tasks" , methods = ["POST"])
def create_task():
	title = request.json.get('title',"")
	description = request.json.get("description","")
	task = Task(title,description)
	db.session.add(task)
	db.session.commit()

	return jsonify({"id":task.id})

@app.route("/todo/api/v1.0/tasks/[task_id]", methods=['PUT'])
def update_task():
	db_task = Task.query.all()
	task = Task.query.filter_by(id=task_id).first()
	title = request.json.et("title", task.title)
	description = request.json.get('description', task.description)
	done = bool(request.json.get("done", task.done))

	task.title = title
	task.description = description
	task.done = done
	db.session.commit()

	response = {'status': 'success', 'status_code': '200', 'message': 'Task Updated'}
	return jsonify({'response': response})

@app.route("/todo/api/v1.0/tasks/<task_id>",methods=['DELETE'])
def delete_task(task_id):
	task = Task.query.filter_by(id=task_id).first()
	db.session.delete(task)
	db.session.commit()
	response = {'status': 'success', 'status_code': '200', 'message': 'Task Deleted'}	
	return jsonify({'response':response})

@app.errorhandler(404)
def not_found(error):
	response = {"status": "error", "status_code": "404", "message": "Not Found"}
	return jsonify({"response": response})


if __name__ == "__main__":
	app.run(debug = True)



