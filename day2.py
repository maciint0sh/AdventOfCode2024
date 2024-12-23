data = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

reports = data.split("\n")
reports.pop(0); reports.pop(-1)

# for each report, check that:
# - it is increasing/decreasing only
# difference between adjacent values is 1,2,3
safe = 0
for report in reports:
    increasing = None
    for i in range(len(report)-1):
        # check increasing/decreasing
        if report[i] < report[i+1]:
            if increasing != False:
                increasing = True
            else:
                break
        elif report[i] > report[i+1]:
            if increasing != True:
                increasing = False
            else:
                break

        