import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import db_session
from database import App as AppModel
from sqlalchemy import and_

class App(SQLAlchemyObjectType):
	class Meta:
		model= AppModel
		interfaces = (relay.node,)

class createApp(graphene.Mutation):
	class Input:
		#Id = graphene.Int()
		title= graphene.String()
		description = graphene.String()
		done = graphene.String()
	ok = graphene.Boolean()
	app = graphene.Field(App)

	@classmethod
	def mutate(cls, _, context, **kwargs):
		app = AppModel(title=kwargs.get("title"), description=kwargs.get("description"), done=kwargs.get("done"))
		db_session.add(app)
		db_session.commit()
		ok = True
		return createTodo(app=App, ok=ok)


#class Query(graphene.ObjectType):
#	node = relay.Node.Field()
#	all_Id = SQLAlchemyConnectionField(Id)
#	all_title = SQLALchemyConnectionField(title)
#	all_description = SQLALchemyConnectionField(description)
#	all_done = SQLALchemyConnectionField(done)

#schema = graphene.Schema(query=Query,types=[Title,Description,Done,Id])	



class Query(graphene.ObjectType):
	node = relay.Node.Field()
	app = SQLAlchemyConnectionField(App)
	find_app = graphene.Field(lambda: app, title= graphene.String())
	all_app = SQLAlchemyConnectionField(App)

	def resolve_find_user(self,args,context,info):
		query = app.get_query(context)
		title = args.get('title')
		# you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
		return query.filter(UserModel.title == title).first()
class MyMutations(graphene.ObjectType):
	create_app = CreateApp.Field()

schema = graphene.Schema(query=Query,types=[App])			

