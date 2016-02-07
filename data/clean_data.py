import pandas as pd 
path = ['governor%s_data.csv',
        'senate%s_data.csv',
        'house%s_data.csv',
        'presidential%s_data.csv' ]
def main():

    for p in path:
        a = open(p%(""), 'a') 
        f = open(p%('_failed'), 'rb') 
        for entry in f:
            string_entry = entry.decode('utf-8', errors = 'replace').split('\r')
            for line in string_entry:
                a.write(line)

def remove_redundancy():
    ''' Remove repetitive headers and the aggregate statistics in the combined data files.
        Also removed CensusPop and RaceNotes
    '''
    for p in path:
        data = pd.read_csv(p%(""))
        # get rid of the columns we don't want
        data.drop(["CensusPop","RaceNotes"],axis=1,inplace=True)
        try:
            data.drop(["TitleNotes","OtherNotes"],axis=1,inplace=True)
        except ValueError:
            pass
        # get rid of the aggregate statistics and duplicate headers resulting from merging the csv's
        data = data[data["Office"] != "CensusPopAll"]
        data = data[data["Office"] != "Office"]
        data = data[data["Office"] != "N/A"]
        data = data[data["Office"].notnull()]
        # for the dates, only keep the year part
        # rename the race date column to RaceYear
        data.rename(columns={'raceYear':'RaceYear','RaceDate':'RaceYear'},inplace=True)
        print data.columns.values
        data['RaceYear'] = data['RaceYear'].map(lambda x : str(x)[:4])
        data = data[data["RaceYear"]!='nan']
        data.to_csv(p%("_cleaned"),index=False)

if __name__=="__main__":
    main()
