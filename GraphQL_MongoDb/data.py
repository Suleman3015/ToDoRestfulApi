from mongoengine import connect
from models import Id,Title,Description,Done

connect(host='mongodb+srv://sulemanahmed:sulemanahmed@cluster0-v2lke.mongodb.net/test?retryWrites=true&w=majority')

def init_db():
	identity = Id(name="5decb8d5c088e69dd604c7df")
	identity.save()

	title= Title(name="todays assignment")
	title.save()

	description = Description(name="do assignment")
	description.save()

	store = Done(name='completed')
	store.save()