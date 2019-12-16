from app import app
import json
import unittest

class AppTestCase(unittest.TestCase):

	def AppSetup(self):
		print("settingUpApp")
		app.config["TESTING"] = True
		self.app = app.test_client()

	def tearDown(self):
		print('TEARING DOWN')

	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code,200)

	def test_load_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type="html/text")
		self.assertIn(b'/',response.data)

	def create_task(self, desc):
		tester = app.test_client(self)
		response = tester.post("/todo/app/v1.0/task", content_type="application/json",
			                  data=json.dumps({"title": "Unit Testing",
		                      "description": "Test Description form:" +desc}))
		return json.loads(response.get_data(as_text=True))

	def delete_task(self, task_id):
		tester = app.test_client(self)
		response = tester.delete("/todo/app/v1.0/task", content_type="application/json")
		json_response = json.loads(response.get_data(as_text=True))
		return json_response["response"]

	def test_create_task(self):
		tester = app.test_client(self)
		json_response = self.create_task("create")
		task_id = json_response['response']
		self.assertIsNotNone(task_id)

	def test_delete_task(self):
		tester = app.test_client(self)
		json_response = self.create_task("delete")
		task_id = json_response["response"]
		self.assertIsNotNone(task_id)

	def get_all_task(self):
		tester = app.test_client(self)
		response = tester.get('/todo/api/v1.0/tasks', content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"Testing App", response.data)
    
    # Ensure that getiing all task is working correclty
	def test_get_all_task(self):
		# creating a task
		tester = app.test_client(self)
		json_response = self.create_task("get all")
		task_id = json_response["response"]
		self.assertIsNotNone(task_id)
        
        # Ensure that deleting all tasks correctly
		json_response = self.delete_task(task_id)
		self.assertIsNotNone(json_response["status"], "success")

	def get_task(self):
		tester = app.test_client(self)
		response = tester.get('/todo/api/v1.0/tasks/'+task_id, content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b" Testing App", response.data)
		json_response = json.loads(response.get_data(as_text=True))
		self.assertEqual(json_response["tasks"][0]["done"], False)
    
    # Ensure that task is adding correctly
	def test_get_task(self):
		# creating a task
		tester = app.test_client(self)
		json_response = self.create_task("get")
		task_id = json_response["response"]
		self.assertIsNotNone(task_id)

		# Ensure that deleting created task is working correctly
		json_response = self.delete_task(task_id)
		self.assertIsNotNone(json_response["status"], "success")

	def update_task(self):
		tester = app.test_client(self)
		response = tester.put("/todo/api/v1.0/tasks"+task_id, content_type="application/json")
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"Testing App", reponse.data)
		json_response = json.loads(response.get_data(as_text=True))
		self.assertEqual(json_response["response"]["status"], "success")
    
    # Ensure that task is updating correctly
	def test_update_task(self):
		# creating a task
		tester = app.test_client(self)
		json_response = self.create_task("updated")
		task_id = json_response["response"]
		self.assertIsNotNone(task_id)

		# Ensure that deleting updating task is working correctly
		json_response = self.delete_task(task_id)
		self.assertIsNotNone(json_response["status"], "success")		

if __name__ == '__main__':
	unittest.main()		
		
