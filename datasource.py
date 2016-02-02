class DataSource:
    ''' The WebDB project database interface, handles query and returns results
        02/01/2016 method stubs implemented
    '''
    
    def __init__(self):
        pass

    def getYearRange(self):
        ''' return the maximum and minumum date (year) that the dataset has.
            can be used by webapp.py to initialize the dropdown list for start
            and end date selection and allows for a more robust database update
        '''
        return (0,0)

    def getDataHeader(self,electionType):
        '''return the header of the data entries
        '''
        return ['','']

    def getCountyData(self,electionType,county,state,startDate,endDate):
        ''' 
            Return the election data county in a given state in a given date range
            In the case of congressional election, county is actually congressional district
            Arguments:
                String electionType,state
                int startDate, endDate
                String list counties
            Return:
                {(county,state):[table]} 
                A dictionray, where the key is the (county,state) tuple and [table] the list
                of data entries like [year,repvote,demvote,...]
        '''
        return {(county,state):[]} 

    def getStateData(self,electionType,state,startDate,endDate):
        '''
            A  wraper for getCountyData, return the data for a given state in given date range
            Arguments:
                String electionType
                int startDate, endDate
                String list states 
            Returns:
                {state:[table]}
                A dictionary with state as the key and the data table as values.
        '''
        return {state:[]}

    def generateDownloadableData(self):
        ''' After a given query is done, generate an csv for download
        '''
        link=''
        return link

