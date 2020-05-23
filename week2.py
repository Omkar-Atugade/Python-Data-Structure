#1. Write a program that extracts the last three items in the list sports and assigns it to the variable last.
    # Make sure to write your code so that it works no matter how many items are in the list.


    #ANSWER :

    sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

    last=sports[len(sports)-3:len(sports)]
    print(last)



#2. Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!” is assigned to the variable message.
    #Do not edit the values assigned to by, az, io, or qy.


    #ANSWER :

    by = "You are"
    az = "doing a great "
    io = "job"
    qy = "keep it up!"
    m1=" ".join(by,az)
    print (message)



#3. Write one for loop to print out each character of the string my_str on a separate line.


    #ANSWER :

    my_str = "MICHIGAN"

    for i in my_str:
        print (i)



#4. Write one for loop to print out each element of the list several_things.
    #Then, write another for loop to print out the TYPE of each element of the list several_things.
    #To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.


    #ANSWER :

    several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

    for i ian several_things:
        print (i)
    for i in several_things:
        print (type(i))



#5. Write code that uses iteration to print out the length of each element of the list stored in str_list.


    #ANSWER :

    str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

    for i in str_list:
        print (len(i))



#6. Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars.
    # Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)


    #ANSWER :

    original_str = "The quick brown rhino jumped over the extremely lazy fox."

    count=0
    for i in original_str:
        count=count+1

    num_chars=count
    print (num_chars)



#7. addition_str is a string with a list of numbers separated by the + sign.
    # Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer).
    #(You should use the .split("+") function to split by "+" and int() to cast to an integer).


    #ANSWER :

    addition_str = "2+5+10+20"

    sum_val=0
    for i in addition_str:
        sum_val=sum(map(int, addition_str.split("+")))
    print(sum_val)



#8. week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign.
     #Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp.
     #Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f)
     #(You should use the .split(",") function to split by "," and float() to cast to a float).


     #ANSWER :

     week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

    avg_temp=0.0
    for i in week_temps_f:
        avg_temp=sum(map(float, week_temps_f.split(",")))/7


    print (avg_temp)



#9. Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums.
     # Do not hard code the list.


     #ANSWER :

    nums=list()
    for i in range(0,68):
        nums.append(i)
    print(nums)



#10. Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list.
     #(You should use the len function).


     #ANSWER :

    original_str = "The quick brown rhino jumped over the extremely lazy fox"
    num_words_list=[]
    x=list(original_str.split())
    for i in x:
        num_words_list.append(len(i))
    print(num_words_list)



#11. Create an empty string and assign it to the variable lett.
     # Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").


     #ANSWER :

    lett=''
    for i in range(7):
        lett+='b'
        print(lett,end='')



#12. Write a program that uses the turtle module and a for loop to draw something.
     # It doesn’t have to be complicated, but draw something different than we have done in the past.
     # (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over.
     # Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)


     #ANSWER :

    import turtle
    wn=turtle.Screen()
    om=turtle.Turtle()

    for i in range(20):
        om.forward(100)
        om.right(70)
