#RituKumar_fnyd(Orders,Returns)
import pymongo
import glob
import pandas as pd

client = pymongo.MongoClient('mongodb+srv://kajol_m:fsAs8da5EFWLjYGN@recononprod.gyx6g.mongodb.net/?retryWrites=true&w=majority')
orders_files = glob.glob(r'C:\Users\DeLL\PycharmProjects\mongodb-upload files\Myntra\Seller Files\fynd\Orders\Orders.xlsb')
db = client['Ritu_Kumar']
for file in orders_files:
    print(file)
    df = pd.read_excel(file)
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    db.Myntra_fynd_Orders.insert_many(df.to_dict(orient='records'))
# returns_files = glob.glob(r'C:\Users\DeLL\PycharmProjects\mongodb-upload files\Myntra\Seller Files\fynd\Returns\Returns.xlsb')
# db = client['Ritu_Kumar']
# for file in returns_files:
#     print(file)
#     df = pd.read_excel(file)
#     df.columns = df.columns.str.replace(' ', '_').str.lower()
#     db.Myntra_fynd_Returns.insert_many(df.to_dict(orient='records'))

