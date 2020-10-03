#學號: 107213067
#姓名: 鍾明智
def leapYear(year):
    if year % 400 == 0: 
        return 'increased pay' #if input divided until zero, it's Leap Year, if else next down
    elif year % 100 == 0: 
        return 'without increased pay' #if input divided until zero, it isn't Leap Year, if else next down
    elif year % 4 == 0:
        return 'increased pay' #if input divided until zero, it's Leap Year, if else next down
    else:
        return 'without increased pay' #if the year not above
print(leapYear(int(input('Please input a year : ')))) #print out the result