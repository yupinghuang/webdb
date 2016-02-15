import psycopg2
import getpass
class DataSource:
    ''' The WebDB project database interface, handles query and returns results
    '''
    
    def __init__(self):
        ''' Initializer of the DataSource object, establish the connection to the db
            and store it as the connection instance variable. Set up cursor and store
            it as an instance variable.
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
        ''' return the tuple of maximum and minumum date (year) that the dataset has.
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

    def getStateData(self,electionType,state,startDate,endDate):
        '''Query the database for a state in a given data range
        INPUT: string electionType, state
               int startDate,endDate
        RETURN:
               a list of tuples representing the query results
        '''
        try:
            if electionType=='Presidential':
                query = "SELECT * FROM presidential WHERE State=%s AND RaceYear>=%s AND RaceYear<=%s ORDER BY Area"
            elif electionType=='Governor':
                query = "SELECT * FROM governor WHERE State=%s AND RaceYear>=%s AND RaceYear<=%s ORDER BY Area"
            self.cursor.execute(query,(state,startDate,endDate))
            return self.cursor.fetchall()
        except Exception as e:
            print e
            self.resetCursor()
            return []


