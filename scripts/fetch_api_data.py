import requests
import pandas as pd
import os
import json
import sys
from datetime import datetime
#from utils.logger import setup_logger
sys.path.append(os.path.abspath('scripts'))

def get_immmunization_metdata(data):
    
    immunisation_category = []
    for heads, dictionary in data.items():
        for head in dictionary:
            if head:
                for k, v in head.items():
                    if k == 'IndicatorCode':
                        immunisation_category.append(v)
            else:
                print("empty")
    return immunisation_category


def fetch_metadata():

    Vaccaine_name = "https://ghoapi.azureedge.net/api/Indicator?$filter=contains(IndicatorName,%20%27Immunization%27)"
    
    headers = {
    "Authorization": "ponmani"
    }
    response = requests.get(Vaccaine_name, headers=headers,)
    data = response.json()
    removed = list(data.keys())[0]
    data.pop(removed)
    list_of_immmunization_metdata= get_immmunization_metdata(data)
    return list_of_immmunization_metdata

def fetch_real_data():
    data_list=[]

    indicator_names = fetch_metadata()
    indicator_names = indicator_names

    headers = {
    "Authorization": "ponmani"
    }
    for indicator in indicator_names:
       
       url = f"https://ghoapi.azureedge.net/api/{indicator}"
       response = requests.get(url, headers=headers,)
       data_list.append(response.json())
 

    return data_list

def fetch_to_df():
    df_list = []
    data_list = fetch_real_data()
    #keys = data_list[-1].keys()
    for i in data_list:
        info = i.get("value",[])
        df = pd.DataFrame(info)
        df_list.append(df)        
    return df_list

def covert_data_to_csv():
    df_list = fetch_to_df()
    for i,df in enumerate(df_list):
        
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data_{i}.csv"
        df.to_csv(f"Vaccination-Analytics/data/raw/{filename}", index=False)
    




def main():
    print(covert_data_to_csv())


if __name__ == "__main__":
    main()


