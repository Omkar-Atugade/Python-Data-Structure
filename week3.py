#1 rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma.
    #Write code to compute the number of months that have more than 3 inches of rainfall.
    #Store the result in the variable num_rainy_months.
    #In other words, count the number of items with values > 3.0.

    #Hard-coded answers will receive no credit.


    #ANSWER :


    rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
    y=rainfall_mi.split(",")
    count=0
    for i in y:
        i=float (i)
        if i > (3):
            count=count+1
        num_rainy_months=count
    print (num_rainy_months)



#2. The variable sentence stores a string.
     #Write code to determine how many words in sentence start and end with the same letter, including one-letter words.
     # Store the result in the variable same_letter_count.

     #Hard-coded answers will receive no credit.


     #ANSWER :

    sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

    count=0
    y=sentence.split()
    for i in y:
        if i[0]==i[-1]:
            count=count+1
        same_letter_count=count
    print (same_letter_count)



#3. Write code to count the number of strings in list items that have the character w in it.
     # Assign that number to the variable acc_num.

     #HINT 1: Use the accumulation pattern!

     #HINT 2: the in operator checks whether a substring is present in a string.

     #Hard-coded answers will receive no credit.


     #ANSWER :

    items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

    count=0
    for i in items:
        if 'w' in i:
            count=count+1

        acc_num=count
    print (acc_num)



#4. Write code that counts the number of words in sentence that contain either an “a” or an “e”.
     #Store the result in the variable num_a_or_e.

     #Note 1: be sure to not double-count words that contain both an a and an e.

     #HINT 1: Use the in operator.

     #HINT 2: You can either use or or elif.

     #Hard-coded answers will receive no credit.


     #ANSWER :

        sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
        count=0
        for i in sentence.split():
            if ('a' in i) or ('e'in i ):
                count= count+1
            num_a_or_e= count
        print (num_a_or_e)
