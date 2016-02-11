import psycopg2
import getpass
class DataSource:
    ''' The WebDB project database interface, handles query and returns results
        02/01/2016 method stubs implemented
    '''
    
    def __init__(self):
        ''' Initializer of the DataSource object, establish the connection to the db
            and store it as the connection instance variable
        '''
        database='huangy'
        user='huangy'
        #password=getpass.getpass()
        password='farm854field'
        # establish the connection and get a cursor
        try:
            self.connection=psycopg2.connect(database=database,user=user,password=password)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print 'Connection Error: ', e
            exit()

    def resetCursor(self):
        ''' Error handling code for all queries. Should something goes wrong,
            try reset the cursor. If this attempt fails, exit.
        '''
        try:
            self.cursor.close()
            self.cursor = self.connection.cursor()
        except Exception as e:
            print 'Failed to reset cursor: ',e
            self.connection.close()
            exit()

    def getYearRange(self):
        ''' return the maximum and minumum date (year) that the dataset has.
            can be used by webapp.py to initialize the dropdown list for start
            and end date selection and allows for a more robust database update
        '''
        try:
            query = "SELECT MIN(RACEYEAR),MAX(RACEYEAR) FROM presidential"
            self.cursor.execute(query)
            [minyear,maxyear] = self.cursor.fetchall()[0]
            return (minyear,maxyear)
        except Exception as e:
            print 'failure to get year range for the data',e
            exit()

    def getCountyData(self,electionType,county,state,startDate,endDate):
        '''Return the election data of a county in a given state in a given date range
            In the case of congressional election, county is actually congressional district
            Arguments:
                String electionType,state county
                int startDate endDate
            Return:
                a list of tuples where a tuple is one row.
                if there is an error, return an empty list
        '''
        try:
            if electionType=='presidential':
                query = "SELECT * FROM presidential WHERE State=%s AND Area=%s AND RaceYear>=%s AND RaceYear<=%s"
            elif electionType=='governor':
                query = "SELECT * FROM governor WHERE State=%s AND Area=%s AND RaceYear>=%s AND RaceYear<=%s"
            elif electionType=='senate':
                query = "SELECT * FROM senate WHERE State=%s AND Area=%s AND RaceYear>=%s AND RaceYear<=%s"
            self.cursor.execute(query,(state,county,startDate,endDate))
            return self.cursor.fetchall()
        except Exception as e:
            self.reset_cursor()
            return []

    def getStateData(self,electionType,state,startDate,endDate):
        '''A  wraper of getCountyData, return the data for a given state in given date range
            Arguments:
                String electionType, state
                int startDate, endDate
            Returns:
                {state:[table]}
                A dictionary with state as the key and the data table as values.
        '''
        try:
            if electionType=='presidential':
                query = "SELECT * FROM presidential WHERE State=%s AND RaceYear>=%s AND RaceYear<=%s"
            elif electionType=='governor':
                query = "SELECT * FROM governor WHERE State=%s AND RaceYear>=%s AND RaceYear<=%s"
            elif electionType=='senate':
                query = "SELECT * FROM senate WHERE State=%s AND RaceYear>=%s AND RaceYear<=%s"
            self.cursor.execute(query,(state,startDate,endDate))
            return self.cursor.fetchall()
        except Exception as e:
            print e
            self.reset_cursor()
            return []


