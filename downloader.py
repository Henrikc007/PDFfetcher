#henter og gemmer filen


import requests
from urllib.parse import urlparse
import asyncio
import os

async def klartilnaeste(aRequest,filnavn):
    pth="C:/Users\HenrikChristensen/OneDrive - Specialisterne/Skrivebord/ProjektUge5/PDFfetcher/dl_pdf/"
    #Her er indført en stop statement, som sikrer at dpfFil er en ikke tom værdi, og kun i tilfælde af at det lykkedes at finde enpassende pdffil hentes den
   
    
    
    doDL = True
    pdfFil=pth+filnavn
    print(pdfFil)


    #giver læseren lov til at gå igang med næste request, så længde der ikke er mere end maxAntal requests igang
    if doDL:
        print("connecter til")
        
        try:
            my=requests.get(aRequest,timeout=1)
            if my.status_code==200:
                pdf = open(pdfFil,'wb')
                pdf.write(my.content)
                pdf.close()
                my.close()
            else:
                print("cant connect")
                
        except asyncio.exceptions:
            print("no connection")

    #     with open(pdfFil,'wb') as f:
    #         f.write(my.content)
    #         print(f"PDF downloaded as {pdfFil}!")
    # else:
    #     print(f"Failed to download PDF. Status code: {my.status_code}")



    #men starter med at sætte en sleep igang
    await asyncio.sleep(1)