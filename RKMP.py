# #RituKumar(Orders,Returns,Payments)
# import pymongo
# import glob
# import pandas as pd
# #
# client = pymongo.MongoClient('mongodb+srv://kajol_m:fsAs8da5EFWLjYGN@recononprod.gyx6g.mongodb.net/?retryWrites=true&w=majority')
# payments_files = glob.glob(r'C:\Users\DeLL\PycharmProjects\mongodb-upload files\Myntra\MarketPlace Files\Payments\*.csv')
# db = client['Ritu_Kumar']
# for file in payments_files:
#     print(file)
#     df = pd.read_csv(file)
#     df.columns = df.columns.str.replace(' ', '_').str.lower()
#     db.Myntra_MP_Payments.insert_many(df.to_dict(orient='records'))
# orders_files = glob.glob(r'C:\Users\DeLL\PycharmProjects\mongodb-upload files\Myntra\MarketPlace Files\Orders\*.csv')
# db = client['Ritu_Kumar']
# for file in orders_files:
#     print(file)
#     df = pd.read_csv(file)
#     df.columns = df.columns.str.replace(' ', '_').str.lower()
#     db.Myntra_MP_Orders.insert_many(df.to_dict(orient='records'))
# returns_files =glob.glob(r'C:\Users\DeLL\PycharmProjects\mongodb-upload files\Myntra\MarketPlace Files\Returns\*.csv')
# db = client['Ritu_Kumar']
# for file in returns_files:
#     print(file)
#     df = pd.read_csv(file)
#     df.columns = df.columns.str.replace(' ', '_').str.lower()
#     db.Myntra_MP_Returns.insert_many(df.to_dict(orient='records'))
#
#
#
