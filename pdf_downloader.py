#thiss is a modification and improvement of original downloader to make the further development easyer

#the module for handling the list of files to be downloadet is called downloadList

#the module to handle the downloading is callede dlSupervisor

import pandas as pd
import dlSupervisor
import downloadList

filMedListen = 'GRI_2017_2020.xlsx'
sheetNavn = '0'
#dataframeListen = downloadList.returnDatafile(filMedListen,sheetNavn)

print("læser excel fil ind som dataframe")
dataframeListen = pd.read_excel(filMedListen,sheetNavn)

#her er angivet mine prioriterede og sekundeærer søjler i dataframe hvor adresserne burde ligge
prioliste='Pdf_URL'
sekundaerListe='Report Html Address'
toSojler = [prioliste,sekundaerListe]


#downloadklasse = downloadList.filtreretDataframe(dataframeListen,toSojler)

print("vi søger listerne igennem for at få tjekket alle tekst filer igennem")
muligepdfer=dlSupervisor.forCheck(dataframeListen,toSojler)
print("vi har gennemsøgt alle linjer, i søjlerne prioliste og sekundaerliste og tjekket om det er htmlsider")


#download 5 stks som test
print("færdig")

