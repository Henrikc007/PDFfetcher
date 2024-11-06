#for undersøgelse af tekststrengen, eksempelvis er det en http:// adresse
import requests
from urllib.parse import urlparse
import pandas as pd


def is_valid_http_url(url):
    parsed_url = urlparse(url)
    # Check if the scheme is 'http' or 'https' and the netloc (domain) is not empty
    return parsed_url.scheme in ['http', 'https'] and bool(parsed_url.netloc)


def forCheck(df,navnepaasojle):
    counter=0
    testforsog=10
    for index, row in df.iterrows():
        if (isinstance(row.loc[navnepaasojle[0]],str)):
            if (is_valid_http_url(row[navnepaasojle[0]])):
                print(row[navnepaasojle[0]])
                r=requests.head(row[navnepaasojle[0]])
                if r.status_code==200:
                    row[navnepaasojle[0]]
            else:
                "NVU"
        else:
            "NoSTR"
            
        counter+=1
        print(counter)
        if (counter>testforsog):
            break
    return("done")
        
