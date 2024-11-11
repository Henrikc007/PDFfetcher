#thiss is a modification and improvement of original downloader to make the further development easyer
#my dl path is set to subfolder called dl_pdf
pth="C:/Users\HenrikChristensen/OneDrive - Specialisterne/Skrivebord/ProjektUge5/PDFfetcher/dl_pdf"

#the module for handling the list of files to be downloadet is called downloadList

#the module to handle the downloading is callede dlSupervisor

import pandas as pd
import dlSupervisor
import asyncio

MAX_CONCURRENT_TASKS = 10

semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)
filMedListen = 'GRI_2017_2020.xlsx'
sheetNavn = '0'


print("læser excel fil ind som dataframe")
dataframeListen = pd.read_excel(filMedListen,sheetNavn)

#her er angivet mine prioriterede og sekundeærer søjler i dataframe hvor adresserne burde ligge
prioliste='Pdf_URL'
sekundaer_liste='Report Html Address'
toSojler = [prioliste,sekundaer_liste]


#downloadklasse = downloadList.filtreretDataframe(dataframeListen,toSojler)

print("vi søger listerne igennem for at få tjekket alle tekst filer igennem")
muligepdfer=asyncio.run(dlSupervisor.forCheck(dataframeListen,toSojler))
print("Vi har gennemløbet de mulige adresser ")

#download 5 stks som test
print("færdig")
