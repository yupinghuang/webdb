#!/usr/bin/python
''' index.py

    Phineas Callahan and Yuping Huang

    adapted from Jeff Ondich's webapp.py

    02/01/2016 implemented a view of the final site:
        returning data to visualize in a given time period
        for a given state. Data visualization and state selection
        will eventually be done in Javascript (D3).

        TODO: Implement data query in printMainPageAsHTML so that the query results
        go through the html to the javasrcipt visualizer.


'''

import cgi
import cgitb; cgitb.enable() #for troubleshooting
from datasource import DataSource

templateFileName='template.html'

states=['National','Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut',
'Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas',
'Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
'Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas',
'Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

def getCGIParameters():
    ''' This function grabs the HTTP parameters we care about, sanitizes the
        user input, provides default values for each parameter is no parameter
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
    # initialize the web form options
    with open(templateFileName,'r') as f:
        templateText = f.read()
    stateoptions=''
    for state in states:
        stateoptions+=makeOption(state)

    yearoptions=''
    minyear,maxyear = db.getYearRange()
    for year in range(minyear,maxyear+1):
        yearoptions+=makeOption(str(year))

    # Query the DB if the form is completed
    electionType,startYear,endYear,state = parameters['electionType'],parameters['startYear'],parameters['endYear'],parameters['state']
    # the header of the data display table
    header="""<tr>
                <th>State</th><th>County</th><th>DemVotes</th><th>RepVotes</th>
                </tr>"""
    if electionType=="" and startYear==0 and endYear==0 and state=="":
        outputText = templateText % (stateoptions,yearoptions,yearoptions,header,showsourceLinks())
    else:
        ############# FUDGE FOR PART 3 ############
        if state=='National':
            state='Alabama'
        electionType='presidential'
        ##########################################
        result = db.getStateData(electionType,state,startYear,endYear)
        table = header + makeTable(result,[1,3,6,9])
        outputText = templateText % (stateoptions,yearoptions,yearoptions,table,showsourceLinks())

    print 'Content-type: text/html\r\n\r\n',
    print outputText

def makeTable(result,colNums):
    '''make a html table out of the result of the data query
       List of Tuples: the db query output
       colNums: the number of columns to be incorporated into the table
    '''
    output=''
    for row in result:
        tableRow='<tr>\r\n'
        for col in colNums:
            tableRow+='<td>'+str(row[col])+'</td>'
        tableRow+="\r\n</tr>\r\n"
        output+=tableRow
    return output

def makeOption(entry):
    '''make an string entry an html form option 
    '''
    return '<option value="'+entry+'">'+entry+'</option>\n'

def printFileAsPlainText(fileName):
    ''' Prints to standard output the contents of the specified file, preceded
        by a "Content-type: text/plain" HTTP header.
    '''
    text = ''
    try:
        f = open(fileName)
        text = f.read()
        f.close()
    except Exception, e:
        pass

    print 'Content-type: text/plain\r\n\r\n',
    print text

def showsourceLinks():
    '''
    generate links that show the project source files
    '''
    links = '<p><a href="showsource.py?source=webapp.py">webapp.py source</a></p>\n'
    links += '<p><a href="showsource.py?source=datasource.py">datasource.py source</a></p>\n'
    links += '<p><a href="showsource.py?source=%s">%s source</a></p>\n' % (templateFileName, templateFileName)
    links += '<p><a href="showsource.py?source=showsource.py">the script we use for showing source</a></p>\n'
    links+='<p> AND THE JS FILES'
    return links

def main():
    parameters = getCGIParameters()
    printMainPageAsHTML(parameters,'template.html')
        
if __name__ == '__main__':
    main()


