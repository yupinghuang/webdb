
def main():
    path = ['data/governor%s_data.csv',
            'data/senate%s_data.csv',
            'data/house%s_data.csv',
            'data/presidential%s_data.csv' ]

    for p in path:
        a = open(p%(""), 'a') 
        f = open(p%('_failed'), 'rb') 
        for entry in f:
            string_entry = entry.decode('utf-8', errors = 'replace').split('\r')
            for line in string_entry:
                a.write(line)

if __name__=="__main__":
    main()
