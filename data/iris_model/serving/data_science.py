import pandas as pd
from sklearn.externals import joblib


model_dir_path = "../../data/model"


def predict(model_dir_path: str, data_frame: pd):
    model_path = "{model_dir_path}/model.pkl".format(model_dir_path=model_dir_path)
    print(data_frame)
    with open(model_path, 'rb') as pickle_file:
        loaded_model = joblib.load(pickle_file)
        result = loaded_model.predict_proba(data_frame)
        return result


predict(model_dir_path, 500)
