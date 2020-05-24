#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
     #Convert the extracted value to a floating point number and print it out.

    #ANSWER :

    text = "X-DSPAM-Confidence:    0.8475";

    spacePos = text.find(" ")
    number = text[spacePos::1]
    strippedNumber = number.lstrip()
    result = float(strippedNumber)
    print(result)



#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
     #Use the file words.txt to produce the output below.
     #You can download the sample data at http://www.py4e.com/code3/words.txt

     #ANSWER :

     fname = input("Enter file name: ")
     fh = open(fname)
     for i in fh:
         x=i.rstrip()
         print(x.upper())



#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
     #X-DSPAM-Confidence:    0.8475
     #Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
     #Do not use the sum() function or a variable named sum in your solution.
     #You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


    #ANSWER :

     fname = input("Enter file name: ")
     fh = open(fname)
     count=0
     tot=0
     ans=0
     for line in fh:
         if not line.startswith("X-DSPAM-Confidence:") : continue

         count=count+1
         num=float(line[21:])
         tot=num+tot
     ans = tot/count
     print("Average spam confidence:",ans)



#8.4 Open the file romeo.txt and read it line by line.
     #For each line, split the line into a list of words using the split() method.
     #The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
     #When the program completes, sort and print the resulting words in alphabetical order.
     #You can download the sample data at http://www.py4e.com/code3/romeo.txt.


     #ANSWER :

     fname = input("Enter file name: ")
     fh = open(fname)
     x = list()
     for line in fh:
        line=line.rstrip()
        line=line.split()
        for c in line:
            if c in x:
                continue
            else:
                x.append(c)
     x.sort()
     print(x)




#8.5 Open the file mbox-short.txt and read it line by line.
    #When you find a line that starts with 'From ' like the following line:
    #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    #You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
    #Then print out a count at the end.
    #Hint: make sure not to include the lines that start with 'From:'.

    #You can download the sample data at http://www.py4e.com/code3/mbox-short.txt


    #ANSWER :

    fname = input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"

    fh = open(fname)
    count = 0
    for line in fh :
        line = line.rstrip()
        if not line.startswith('From '): continue
        words = line.split()
        print( words[1])
        count +=1

    print("There were", count, "lines in the file with From as the first word")




#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
    #The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
    #The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
    #After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


    #ANSWER :

    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    name = "mbox-short.txt"
    handle = open(name)
    text = handle.read()

    words = list()

    for line in handle:
        if not line.startswith("From:") : continue
        line = line.split()
        words.append(line[1])


    counts = dict()

    for word in words:
               counts[word] = counts.get(word, 0) + 1


    maxval = None
    maxkey = None
    for key,val in counts.items() :

      if val > maxval:
          maxval = val
          maxkey = key

    print (maxkey, maxval)




#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
     #You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
     #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
     #Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


     #ANSWER :

    name =input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    text = open(name)

    hours = dict()

    for line in text:
        line.rstrip()
        if not line.startswith("From "): continue
        words = line.split()

        hour = words[5].split(":")
        hours[hour[0]] = hours.get(hour[0],0) + 1

    lst = []

    for a,b in hours.items():
        lst.append((a,b))

    lst.sort()


    for a,b in lst:
        print (a,b
