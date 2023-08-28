import numpy as np
import pandas as pd

weeks = 20

cooks = np.array(pd.read_csv("cooks.csv").columns)
assigned_cooking_spots = np.random.permutation(cooks)
while (np.size(assigned_cooking_spots) <= weeks*4) and (np.size(assigned_cooking_spots) % 2 != 0):
    random_order_cooks = np.random.permutation(cooks)
    
    assigned_cooking_spots = np.concatenate((assigned_cooking_spots, random_order_cooks))

assigned_cooking_spots = np.reshape(assigned_cooking_spots, [-1, 2])

schedule = pd.DataFrame(assigned_cooking_spots, columns=['Kok 1', 'Kok 2'])

schedule.to_excel('schedule.xlsx')