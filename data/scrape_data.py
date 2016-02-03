from bs4 import BeautifulSoup
import requests

def scrapeElectionData(office):
    areatype = 3 if office == 3 else 2

    election_data = list()
    url = "http://library.cqpress.com/elections/download-data%s.php"    
    params = {  'filetype':'1', 'office':office, 'areatype':areatype, 
            'format':'3', 'emailto':'', 'emailfrom':'', 'license':'on'}

    session   = requests.Session()
    data_html = session.get(url%(""), params = params)
    data_soup = BeautifulSoup(data_html.content, "html5lib")

    years  = data_soup.find(id = "year")
    for y in years.find_all('option'):
        params['year'] = y['value']

        data_html = session.get(url%(""), params = params)
        data_soup = BeautifulSoup(data_html.content, "html5lib")

        states = data_soup.find(id = 'states')
        for s in states.find_all('option'):
            print("Scraping %s - %s"%(y['value'], s['value']))
            params['states[]'] = s['value']
            
            data = session.get(url%("-results"), params = params).content
            election_data.append(data)
            
    return election_data

def write(data, path):

    s = open(path+'_data.csv', 'w')
    f = open(path+'_failed_data.csv', 'wb')
    for entry in data:
        try:
            entry = entry.decode('utf-8')
            for line in entry.split('\n'):
                if len(line.split(',')) > 3:
                    s.write(line+'\n')
        except:
            f.write(entry) 
             

def main():
    #p_data = scrapeElectionData(1)
    #write(p_data, 'data/presidential')

    #h_data = scrapeElectionData(2)
    #write(h_data, 'data/house')

    #s_data = scrapeElectionData(3)
    #write(s_data, 'data/senate')

    g_data = scrapeElectionData(4)
    write(g_data, 'data/governor')



if __name__=='__main__':
   main() 
