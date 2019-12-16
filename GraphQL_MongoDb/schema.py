import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField,MongoengineObjectType
from models import  Id as IdModel
from models import Title as titleModel
from models import Description as descriptionModel 
from models import Done as doneModel

class Id(MongoengineObjectType):
	class Meta:
		model = IdModel
		interfaces = (Node,)

class Title(MongoengineObjectType):
	class Meta:
		model = titleModel
		interfaces = (Node,)

class Description(MongoengineObjectType):
	class Meta:
		model = descriptionModel
		interfaces = (Node,)

class Done(MongoengineObjectType):
	class Meta:
		model = doneModel
		interfaces = (Node,)

class Query(graphene.ObjectType):
	node = Node.Field()
	all_id = MongoengineConnectionField(Id)
	all_title = MongoengineConnectionField(Title)
	all_description = MongoengineConnectionField(Description)
	all_done = MongoengineConnectionField(Done)

schema = graphene.Schema(query=Query,types=[Title,Description,Done,Id])	

