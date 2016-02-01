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
        return []

    def getCountiesData(self,electionType,counties,state,startDate,endDate):
        ''' 
            Return the election data of a list of counties in a given state in a given date range
            @String electionType,state
            @int startDate, endDate
            @String list counties
            @returns a list of tuples (years,data1,data2,....) where data1, data2 currently would
                be percentage of votes the dems and republicans get.
                TODO: NEED DICTIONARIES
        '''
        return [(0,0)]

    def getStatesData(self,electionType,states,startDate,endDate):
        '''
            Returns the election data for given states
            @String electionType
            @int startDate, endDate
            @String list states 
            @returns (years,data1,data2,....) where data1, data2 currently would
                be percentage of votes the dems and republicans get.
    '''

    def aggregate(self,datalabel,data):
        #somehow aggregates the data
        return [datalabel,aggregatedData]

    def generateDownloadableData(self):
        ''' After a given query is done, generate an csv for download
        '''
