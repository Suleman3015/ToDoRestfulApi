from datetime import datetime
from mongoengine import Document
from mongoengine.fields import DateTimeField , ReferenceField, StringField

class Id(Document):
	meta = {"task":"id"}
	name = StringField()

class Title(Document):
	meta = {"task":"title"}
	name = StringField()


class Description(Document):
	meta = {"task":"description"}
	name =  StringField()

class Done(Document):
	meta = {"Task":"document"}
	name = StringField()
	date = DateTimeField(default=datetime.now)	




