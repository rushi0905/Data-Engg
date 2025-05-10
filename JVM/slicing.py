class slice:

    str = 'welcome to my blog'
    # print(str.index(str))
    print(str[3:18]) # come to my blog
    print(str[2:14:2]) # loet y
    print(str[:7]) # welcome
    print(str[-9:-15]) # Blank as 25 char is not in index (star:diff:stop)
    print(str[8:25:3]) # tmbg
    print(str[0:9:3]) # wce
    #
    # str = 'welcome to my blog'
    #
    # for index, char in enumerate(str):
    #     print(f" Index {index}: '{char}'")

    num1 =float(input('Enter first num')) #12
    num2= float(input('Enter second num'))#12
    num3 = float(input('Enter third num'))#12
    total = num1+num2+num3
    aveg = total/3
    print("Sum of 3 num :",total)
    print("Average of 3 num :",aveg)