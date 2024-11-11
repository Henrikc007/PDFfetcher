#for undersøgelse af tekststrengen, eksempelvis er det en http:// adresse
import downloader
from urllib.parse import urlparse
import asyncio
import requests


def is_valid_http_url(url):
    parsed_url = urlparse(url)
    # Check if the scheme is 'http' or 'https' and the netloc (domain) is not empty
    return parsed_url.scheme in ['http', 'https'] and bool(parsed_url.netloc)



def getfilename(r: requests.head,Myurl):
    if 'Content-Disposition' in r.headers:
        content_disposition = r.headers['Content-Disposition']
        if 'filename=' in content_disposition:
            staten=True
            filename = content_disposition.split('filename=')[1].strip('/"')
            
            
        # If filename is not found in the header, extract it from the URL
            if filename is None:
                staten=False
                if isinstance(Myurl,str):
                    filename=Myurl.split("/").reverse()[0]
                    print(filename)
                   
        print("filnavn er "+ filename)
        return filename

async def forCheck(df,navnepaasojle):
    
    counter=0
    testforsog=100
    
    for index, row in df.iterrows():
        if index > 25:
            if (isinstance(row.loc[navnepaasojle[0]],str)):
                if (is_valid_http_url(row[navnepaasojle[0]])):
                    #print(row[navnepaasojle[0]])
                    try:
                        
                        r=requests.head(row[navnepaasojle[0]],timeout=1)
                        
                        if r.status_code==200:
                            pdffilename = row['BRnum']
                            
                            task = asyncio.create_task(downloader.klartilnaeste(row[navnepaasojle[0]],pdffilename))
                            await task
                            #wait for some achnolegement from another code before running next part
                            #but try to do this multithreat wise but with a pool
                    # except requests.exceptions.Timeout:
                    except requests.exceptions:
                        print("error with coode " + r.status_code)
                        
                    
                else:
                    print("NVU")
            else:
                print("NoSTR")
                
            counter+=1
            print(counter)
            if (counter>testforsog):
                break
    return("done")
        
