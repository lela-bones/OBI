import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#best file= mac_dude_BlinkTest_1.json
#second best = a88ac021f60d23d32aec7764199fcfcf64c3784548eedc852c90f6a4baa24f48.json
filename = open('../data/mac_dude_BlinkTest_1.json', 'r')

#loads json file
data = json.load(filename)

#stores only the eeg data
eeg = np.array(data['patterns'])

#maps the node number to the data
inputs = map(lambda p: p['input'], eeg[2:])
#puts data into a list
inputs = list(inputs)
#puts data into an array
inputs = np.array(inputs)
#turns into dataframe
#df = pd.DataFrame(data=inputs)

#normalizes the data
inputs = np.subtract(inputs, inputs.min())
inputs = np.divide(inputs, inputs.max())
