import pandas as pd

#her hentes downloadfilen ind...der læses hele downloadfilen ind
def returnDatafile(filen,sheetname):
    with open(filen) as file:
        df = pd.read_excel(file,sheet_name=sheetname)
        return df

class filtreretDataframe():
    def __init__(self,datafyld,rakker):
        self.data = datafyld.sliced_df[rakker]
        


