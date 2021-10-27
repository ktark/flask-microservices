import connexion
import six
from flask import jsonify

from swagger_server import util
import json
import pandas as pd


def get_sensor_by_id(deviceId):  # noqa: E501

    try:
        df = pd.read_csv("/tmp/iot.csv")
        if deviceId in df['dev_id'].values :
            df_deviceId = df.loc[df['dev_id'] == deviceId]
            df_resp = df_deviceId[['dev_id','device_name','snr']]
         #   df_resp = df_resp.head(1)
            data = df_resp.to_json()

            status = 200
            #data = {"Success message": "Device deleted from the csv"}
        else:
            status = 400
            data = {"Error message": "Invalid device"}
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return json.loads(data),status

def getmaximum(sensor):  # noqa: E501

    try:
        df = pd.read_csv("/tmp/iot.csv")
        df_sensor = df[[sensor,'dev_id','datetime','device_name']].max()
        data = df_sensor.to_json()
        status = 200
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return json.loads(data),status


def getminimum(sensor):  # noqa: E501

    try:
        df = pd.read_csv("/tmp/iot.csv")
        df_sensor = df[[sensor,'dev_id','datetime','device_name']].min()
        data = df_sensor.to_json(orient="records")
        status = 200
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return json.loads(data),status