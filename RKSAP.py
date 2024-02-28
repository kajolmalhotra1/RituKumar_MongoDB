#RituKumar_SAP(Orders)

import pymongo
import glob
import pandas as pd

client = pymongo.MongoClient('mongodb+srv://kajol_m:fsAs8da5EFWLjYGN@recononprod.gyx6g.mongodb.net/?retryWrites=true&w=majority')
orders_files = glob.glob(r'C:\Users\DeLL\PycharmProjects\mongodb-upload files\Myntra\Seller Files\SAP\Orders\Orders.xlsb')
db = client['Ritu_Kumar']
collection = db['Myntra_SAP_Orders']
for file in orders_files:
    print(file)
    df = pd.read_excel(file)

    # Convert large integers to strings in all columns
    df = df.astype(str)
    df.columns = df.columns.str.replace(' ', '_').str.lower()

    # Insert data into MongoDB
    try:
        db.Myntra_SAP_Orders.insert_many(df.to_dict(orient='records'))
    except OverflowError:
        # If an OverflowError occurs, handle it by converting large integers to strings
        df = df.astype(str)
        # df.columns = df.columns.str.replace(' ', '_').str.lower()
        db.Myntra_SAP_Orders.insert_many(df.to_dict(orient='records'))
        print("Inserted large integers as strings to avoid OverflowError")





