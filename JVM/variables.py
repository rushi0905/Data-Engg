class variable:

    var1 = "Awesome"
    def my_func():
        global var1
        var1 = 'fantastic'
 
    my_func()
    print("Python is ", var1)