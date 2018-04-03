
with open('inc5000.csv', 'r') as f:
    '''
    #print line by line
    f_contents = f.readline()
    print(f_contents)

    #print al the lines
    f_contents = f.readlines()
    print(f_contents)
    '''
    for line in f:
        print (line, end= '')



#Is always importat to close the files that we oppened , we work as below

'''
f = open('inc5000.csv', 'r')
print(f)
f.close()
'''
