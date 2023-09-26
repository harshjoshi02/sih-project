import pandas as pd

phone_data=pd.read_csv('ndtv_data_final.csv',encoding='latin-1')
laptop_data=pd.read_csv('laptop_price (1).csv',encoding='latin-1')
watch_data=pd.read_csv('Smart watch prices.csv',encoding='latin-1')

phone_brands = phone_data['Brand'].unique()
laptop_brands = laptop_data['Company'].unique()
watch_brands = watch_data['ï»¿Brand'].unique()

def device_spec(brand,model,ch,*arg):
  if ch == 1:
    for bar in phone_brands:
      if bar == brand:
        device_specs = phone_data.loc[phone_data['Model'] == model]
      else:
         print('Not Found')
         pass
  if ch == 2:
    for bar in laptop_brands:
      if bar == brand:
        device_specs = laptop_data.loc[laptop_data['Product'] == model]
        min = device_specs['laptop_ID'].min()
        device_specs = device_specs.loc[device_specs['laptop_ID'] == min]
      else:
         pass
  if ch == 3:
    for bar in watch_brands:
      if bar == brand:
        device_specs = watch_data.loc[watch_data['Model'] == model]
        min = device_specs.index.min()
        device_specs = device_specs.loc[device_specs.index == min]
      else:
         pass
  return device_specs

