#for undersøgelse af tekststrengen, eksempelvis er det en http:// adresse
import requests
from urllib.parse import urlparse
import pandas as pd
import asyncio


def is_valid_http_url(url):
    parsed_url = urlparse(url)
    # Check if the scheme is 'http' or 'https' and the netloc (domain) is not empty
    return parsed_url.scheme in ['http', 'https'] and bool(parsed_url.netloc)

async def klartilnaeste(aRequest: requests.head):
    #giver læseren lov til at gå igang med næste request, så længde der ikke er mere end maxAntal requests igang
    my=requests.get(aRequest.url,timeout=10)



    #men starter med at sætte en sleep igang
    await asyncio.sleep(1)


async def forCheck(df,navnepaasojle):
    
    counter=0
    testforsog=50
    for index, row in df.iterrows():
        if (isinstance(row.loc[navnepaasojle[0]],str)):
            if (is_valid_http_url(row[navnepaasojle[0]])):
                print(row[navnepaasojle[0]])
                try:
                    r=requests.head(row[navnepaasojle[0]],timeout=10)
                    if r.status_code==200:
                        row[navnepaasojle[0]]="JA"
                        task = asyncio.create_task(klartilnaeste(r))
                        await task
                        #wait for some achnolegement from another code before running next part
                        #but try to do this multithreat wise but with a pool
                except requests.exceptions.Timeout:
                    print("timed out")
                    r.close()
                
            else:
                "NVU"
        else:
            "NoSTR"
            
        counter+=1
        print(counter)
        if (counter>testforsog):
            break
    return("done")
        
