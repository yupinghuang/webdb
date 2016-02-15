#!/usr/bin/python
''' index.py

    Yuping Huang
    with previous work done by Phineas Callahan

    adapted from Jeff Ondich's webapp.py

'''

import cgi
import cgitb; cgitb.enable() #for troubleshooting
from datasource import DataSource

templateFileName='template.html'

states=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut',
'Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas',
'Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
'Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas',
'Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

offices=['Presidential','Governor']

def getCGIParameters():
    ''' This function grabs the HTTP parameters we care about
        and provides default values for each parameter is no parameter
        is provided by the incoming request, and returns the resulting values.
    '''
    form = cgi.FieldStorage()
    parameters={'electionType':'','state':'','startYear':0,'endYear':0}

    if 'election' in form:
        parameters['electionType'] = form['election'].value
    if 'startYear' in form:
        parameters['startYear'] = form['startYear'].value
    if 'endYear' in form:
        parameters['endYear'] = form['endYear'].value
    if 'state' in form:
        parameters['state'] = form['state'].value
    return parameters

def printMainPageAsHTML(parameters,templateFileName):
    ''' Prints to standard output the main page for this web application, based on
        the specified template file and parameters. The content of the page is
        preceded by a "Content-type: text/html" HTTP header.
    '''
    db = DataSource()
    with open(templateFileName,'r') as f:
        templateText = f.read()

    # initialize the web form options
    stateOptions=''
    for state in states:
        stateOptions+=makeOption(state,parameters['state'])
    startYearOptions = ''
    endYearOptions = ''
    minyear,maxyear = db.getYearRange()
    for year in range(minyear,maxyear+1):
        startYearOptions+=makeOption(str(year),str(parameters['startYear']))
        endYearOptions+=makeOption(str(year),str(parameters['endYear']))

    officeOptions=''
    for office in offices:
        officeOptions+=makeOption(office,parameters['electionType'])

    # Query the DB if the form is completed
    electionType,startYear,endYear,state = parameters['electionType'],parameters['startYear'],parameters['endYear'],parameters['state']
    # the header of the data display table
    header="""<tr>
                <th>Year</th><th>State</th><th>County</th><th>RepVotes</th><th>DemVotes</th><th>ThirdVotes</th>
                </tr>"""
    if electionType=="" and startYear==0 and endYear==0 and state=="":
        # no input detected
        outputText = templateText % (officeOptions,stateOptions,startYearOptions,endYearOptions,header,)
    else:
        result = db.getStateData(electionType,state,startYear,endYear)
        table = header + makeTable(result,[2,1,3,5,8,12])
        outputText = templateText % (officeOptions,stateOptions,startYearOptions,endYearOptions,table)

    print 'Content-type: text/html\r\n\r\n',
    print outputText

def makeTable(result,colNums):
    '''make a html table out of the result of the data query
       INPUT: List of Tuples result: the db query output
              list colNums: the number of columns to be incorporated into the table
       RETURN: string a html table row
    '''
    output=''
    for row in result:
        tableRow='<tr>\r\n'
        for col in colNums:
            tableRow+='<td>'+str(row[col])+'</td>'
        tableRow+="\r\n</tr>\r\n"
        output+=tableRow
    return output

def makeOption(entry,currentValue):
    '''Helper function to make an string entry an html form option 
       use currentValue to decide if the selected attributed should be used
       INPUT; string entry,currentValue
       RETURN: the corresponding html option script
    '''
    if entry==currentValue:
        return '<option value="'+entry+'" selected="selected">'+entry+'</option>\n'
    else:
        return '<option value="'+entry+'">'+entry+'</option>\n'

def main():
    parameters = getCGIParameters()
    printMainPageAsHTML(parameters,'template.html')
        
if __name__ == '__main__':
    main()


