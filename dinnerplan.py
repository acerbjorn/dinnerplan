import numpy as np
import pandas as pd
import datetime

weeks = 40
start_date = datetime.date(2023, 8, 30)
weekmask = "Wed Sun"



cooks = np.array(pd.read_csv("cooks.csv").columns)
assigned_cooking_spots = np.random.permutation(cooks)
while (np.size(assigned_cooking_spots) <= (weeks*4)) or (np.size(assigned_cooking_spots) % 2 != 0):
    random_order_cooks = np.random.permutation(cooks)
    assigned_cooking_spots = np.concatenate((assigned_cooking_spots, random_order_cooks))


assigned_cooking_spots = np.reshape(assigned_cooking_spots, [-1, 2])
[cooking_days, _] = assigned_cooking_spots.shape
cooking_dates = pd.bdate_range(start_date, periods=cooking_days, freq="C", weekmask=weekmask)


schedule = pd.DataFrame(assigned_cooking_spots, columns=['Kok 1', 'Kok 2'], index=cooking_dates)

schedule.to_excel('schedule.xlsx')
