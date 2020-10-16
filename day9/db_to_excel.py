from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import MetaData

import xlsxwriter


engine = create_engine('sqlite:///:memory:')
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()
meta = MetaData()

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('records.xlsx')
worksheet = workbook.add_worksheet()

records_table = Table(
    'records', meta,
    Column("id", Integer, primary_key=True),
    Column("qty", String),
    Column("desc", String)
)

meta.create_all(engine)
conn = engine.connect()
# Some data we want to write to the worksheet.
records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)

for qty, id, desc in records:
    record = records_table.insert().values(id=id, qty=qty, desc=desc)
    conn.execute(record)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0
r = records_table.select()
res = conn.execute(r)

worksheet.write(row, col,     "id")
worksheet.write(row, col + 1, "Desc")
worksheet.write(row, col + 2, "qty")
row = 1
# Iterate over the data and write it out row by row.
for id, qty, desc in (res):
    worksheet.write(row, col,     id)
    worksheet.write(row, col + 1, desc)
    worksheet.write(row, col + 2, qty)
    row += 1

workbook.close()
