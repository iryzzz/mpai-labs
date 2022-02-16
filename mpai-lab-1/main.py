import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import data, img_as_float, exposure



import json
settings = {
    'path_in': 'galaxy.jpg',
    'path_out': 'out.jpg',
    'parameter': 0.5
}
with open('settings.json', 'w') as fp:
    json.dump(settings, fp)

def get_user_parameters():
    with open('settings.json') as json_file:
        json_data = json.load(json_file)
    parameters = {entry: json_data[entry] for entry in json_data.keys()}
    return parameters


print (get_user_parameters())