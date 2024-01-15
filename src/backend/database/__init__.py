from .tables import meta, engine

#meta.drop_all(engine)
meta.create_all(engine)