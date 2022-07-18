def isYearLeap(year):
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
       return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Fallo")
        
def daysInMonth(year, month):
    
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]
testYears = [1900, 2000, 2016, 1987] 
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Fallo")

def dayOfYear(year, month, day):
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None
    if day < daysInMonth(year, month) or day < 1:
        return None
    
    totalDays = day
    month = month - 1
    while month > 0:
        totalDays += daysInMonth(year, month)
        month -= 1
    return totalDays
print(dayOfYear(2000, 12, 31))