#for undersøgelse af tekststrengen, eksempelvis er det en http:// adresse
import requests
from urllib.parse import urlparse
import pandas as pd


def is_valid_http_url(url):
    parsed_url = urlparse(url)
    # Check if the scheme is 'http' or 'https' and the netloc (domain) is not empty
    return parsed_url.scheme in ['http', 'https'] and bool(parsed_url.netloc)


def forCheck(dataframelist: pd,navnepaasojle):
   
    appended=[]
    for streng in dataframelist.iterrows():
        if (isinstance(streng[navnepaasojle[0]],str)):
            if (is_valid_http_url(streng[navnepaasojle[0]])):
                r=requests.head(streng[navnepaasojle[0]])
                if r.status_code==200:
                    appended.append(streng[navnepaasojle[0]])
            else:
                appended.append("NVU")
        else:
            appended.append("NoSTR")
    return(appended)
        
