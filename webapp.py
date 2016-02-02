#!/usr/bin/python
''' webapp.py

    Phineas Callahan and Yuping Huang

    adapted from Jeff Ondich's webapp.py

    02/01/2016 implemented a view of the final site:
    returning data to visualize in a given time period
    for a given state. Data visualization and state selection
    will eventually be done in Javascript (D3).

    TODO time series implementation
'''

import cgi
import cgitb; cgitb.enable() #for troubleshooting

#def sanitizeUserInput(s):
#    ''' There are better ways to sanitize input than this, but this is a very
#        simple example of the kind of thing you can do to protect your system
#        from malicious user input. Unfortunately, this example turns "O'Neill"
#        into "ONeill", among other things.
#    '''
#    charsToRemove = ';,\\/:\'"<>@'
#    for ch in charsToRemove:
#        s = s.replace(ch, '')
#    return s

templateFileName='template.html'

def getCGIParameters():
    ''' This function grabs the HTTP parameters we care about, sanitizes the
        user input, provides default values for each parameter is no parameter
        is provided by the incoming request, and returns the resulting values.
    '''
    form = cgi.FieldStorage()
    parameters={'election':'','state':'','startyear':0,'endyear':0}

    if 'election' in form:
        parameters['election'] = form['election'].value
    if 'year' in form:
        parameters['year'] = form['election'].value
    if 'state' in form:
        parameters['state'] = form['state'].value

    return parameters


def printMainPageAsHTML(parameters,templateFileName):
    ''' Prints to standard output the main page for this web application, based on
        the specified template file and parameters. The content of the page is
        preceded by a "Content-type: text/html" HTTP header.
        
        Note that this function is quite awkward, since it assumes knowledge of the contents
        of the template (e.g. that the template contains four %s directives), etc. But
        it gives you a hint of the ways you might separate visual display details (i.e. the
        particulars of the HTML found in the template file) from computational results
        (in this case, the strings built up out of animal and badAnimal). 
    '''
    with open(templateFileName,'r') as f:
        templateText = f.read()
    states='<option value="Alabama">Alabama</option>'
    years='<option value="2012">2012</option>'
    outputText = templateText % (states,years,showsourceLinks())

    print 'Content-type: text/html\r\n\r\n',
    print outputText

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
    # TODO: 
    parameters = getCGIParameters()
    printMainPageAsHTML(parameters,'template.html')
        
if __name__ == '__main__':
    main()


