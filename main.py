from flask import Flask, request
from sklearn.externals import joblib
import pandas as pd
import happybase as hb
import json


app = Flask(__name__)

# Path to model.
model_dir_path = "/root/PycharmProjects/pract20a/model"


# Processing data with model. Get model path, data(json). Return results list.
def predict(model_dir_path: str, data_frame: pd):
    model_path = "{model_dir_path}/model.pkl".format(model_dir_path=model_dir_path)

    with open(model_path, 'rb') as pickle_file:
        loaded_model = joblib.load(pickle_file)
        result = loaded_model.predict_proba(data_frame)
        return result
# End processing.


# Solving problem with converting exponential values in result sets to float.
def exp_to_float(value):
    return "{:.2f}".format(float(value))


# Method that store results into HBase. Using HappyBase Api.
def put_to_hbase(inp_data):

    d = json.loads(inp_data)

    connection = hb.Connection(HB_HOST, HB_PORT)

    tables = connection.tables()
    print("HBase has tables {0}".format(tables))

    if HB_TABLE_NAME not in tables:
        print("Creating table {0}".format(HB_TABLE_NAME))
        connection.create_table(HB_TABLE_NAME, {'cf:': dict()})

    table = connection.table(HB_TABLE_NAME)

    b = table.batch()

    for key, value in d.items():
        print(key, value)
        try:
            b.put(key, value)
            print("Storing values with row key '{0}'".format(key))
        except ValueError:
            pass
        else:
            b.send()


@app.route("/predict", methods=["POST"])
def post():

    data = pd.read_json(request.data)
    resp = predict(model_dir_path, data)

    new_resp = list(map(lambda lst: tuple(map(lambda x: exp_to_float(x), lst)), resp))

    ndf = pd.DataFrame.from_records(new_resp, columns=["cf:Iris-setosa", "cf:Iris-versicolor", "cf:Iris-virginica"])

    result = ndf.to_json(orient='index')

    put_to_hbase(result)

    return result


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = "9999"

    HB_HOST = 'localhost'
    HB_PORT = 9090
    HB_TABLE_NAME = 'ir_test6'

    app.run(host=HOST, port=PORT)
