import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://ever:3v3r@localhost/municipios')
nombre_tabla = 'avaluos_rusticos'

if not engine.dialect.has_table(engine, nombre_tabla, schema='xichu'):
	df = pd.read_csv('avaluos_rusticos.csv')
	df.to_sql(nombre_tabla, con=engine, schema='xichu')
	print(f'tabla creada: {nombre_tabla}')
else:
	print(f'Ya existe tabla {nombre_tabla}')
