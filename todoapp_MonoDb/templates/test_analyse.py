from app import app
import unittest
import json 

class AppTest(unittest.TestCase):

	def app(self):
		print("setting app")
		app.config["TESTING"] = True
		self.app = app.Test_Client()

	def teardown(self):

        print("tearing down")


