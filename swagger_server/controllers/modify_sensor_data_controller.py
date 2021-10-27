import connexion
import six
from flask import jsonify

from swagger_server import util
import json
import pandas as pd
def delete_sensor_data(deviceId):  # noqa: E501
    """Delete sensor data

    This can only be done by the logged in user. # noqa: E501

    :param deviceId: Sensor Id that need to be updated
    :type deviceId: int

    :rtype: None
    """
    try:
        df = pd.read_csv("/tmp/iot.csv")
        if deviceId in df['dev_id'].values :
            indexNames = df[ df['dev_id'] == deviceId].index
            df.drop(indexNames , inplace=True)
            df.to_csv("/tmp/iot.csv")
            status = 200
            data = {"Success message": "Device deleted from the csv"}
        else:
            status = 400
            data = {"Error message": "Invalid device"}
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return jsonify(data),status

def update_sensor_data(body):  # noqa: E501
    """Updated Sensor name

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """

          # noqa: E501
    try:
        body = connexion.request.get_json()

        dev_id = body['dev_id']
        device_name = body['device_name']

        df = pd.read_csv("/tmp/iot.csv")
        if dev_id in df['dev_id'].values :
            df.loc[df['dev_id'] == dev_id, 'device_name'] = device_name
            df.to_csv("/tmp/iot_updated_modifed.csv")
            status = 200
            data = {"Success message": "CSV updated and saved as iot_updated_modifed.csv in /tmp"}
        else:
            status = 400
            data = {"Error message": "Invalid device"}
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return data, status