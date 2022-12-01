import pandas as pd
import numpy as np
import pickle
import os


def my_scaler():
	scaler = pickle.load(open('eda_preprocessing_models/scaler.pkl','rb'))
	return scaler


def model_depth():
	model = pickle.load(open('eda_preprocessing_models/forest_depth.pkl','rb'))
	return model


def model_width():
	model = pickle.load(open('eda_preprocessing_models/forest_width.pkl','rb'))
	return model


def models_predict(data):
	model_for_depth = model_depth()
	model_for_width = model_width()
	depth = model_for_depth.predict(data)
	width = model_for_width.predict(data)
	if len(data) == 1:
		return [round(depth[0], 2), round(width[0], 2)]
	li = [[round(depth[i], 2), round(width[i], 2)] for i in range(len(data))]
	return li


def preporations(data):
	scaler = my_scaler()
	try:
		scaler_data = scaler.transform(data)
		return models_predict(scaler_data)
	except:
		pass


def predict_big_data(name):
	try:
	    df = pd.read_csv(name)
	    scaler = my_scaler()
	    scaler_data = scaler.transform(df)
	    data = models_predict(scaler_data)
	    pred_df = pd.DataFrame(data, columns=['Depth', 'Width'])
	    new_path = '/'.join(name.split('/')[:-1]) + '/pred_data.csv'
	    path_for_user = '/'.join(name.split('/')[-2:-1]) + '/pred_data.csv'
	    pred_df.to_csv(new_path, index=False)
	    return path_for_user
	except:
		pass