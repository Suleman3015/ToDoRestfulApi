import graphene
from graphene            import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database            import db_session, App as AppModel
from sqlalchemy          import and_

class App(SQLAlchemyObjectType):
	class Meta:
		model= AppModel
		interfaces = (relay.Node,)


class createApp(graphene.Mutation):
	class Input:
		#Id = graphene.String()
		title = graphene.String()
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
			return createApp(app=app, ok=ok)

#class changeTitle(graphene.Mutation):
#	class Input:
#		title = graphene.String()
#		description = graphene.String()
#
#	ok = graphene.Boolean()
#	todo = graphene.Field(Todo)
#
#	@classmethod
#	def mutate(cls, _, context, **kwargs):
######	ok = True
##		return changeTitle(todo=todo, ok=ok)

class Query(graphene.ObjectType):
	Node = relay.Node.Field()
	app = SQLAlchemyConnectionField(App)
	find_app = graphene.Field(lambda: App, title=graphene.String())
	all_app = SQLAlchemyConnectionField(App)

	def resolve_find_todo(cls, _, context, **kwargs):
		query = App.get_query(context)
		title = kwargs.get("title")
		return query.filter(AppModel.title == title).first()

class MyMutations(graphene.ObjectType):
	create_app = createApp.Field()
#	change_title = changeTitle.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations, types=[App])