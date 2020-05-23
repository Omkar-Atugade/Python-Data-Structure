#1. Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.


     #ANSWER :

    sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

    sports.insert(2,"horseback riding")
    print (sports)



#2. Write code to take ‘London’ out of the list trav_dest.


    #ANSWER :

    trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']

    trav_dest.remove("London")
    print (trav_dest)



#3. Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.


     #ANSWER :

    trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']

    trav_dest.append("Guadalajara")
    print (trav_dest)



#4. Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.


    #ANSWER :

    winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']

    winners.sort()
    print (winners)



#5. Write code to switch the order of the winners list so that it is now Z to A.
      #Assign this list to the variable z_winners.


      #ANSWER :

        winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']

        winners.reverse()
        z_winners=winners
        print (z_winners)



#6. Currently there is a string called str1.
     #Write code to create a list called chars which should contain the characters from str1.
     #Each character in str1 should be its own element in the list chars.


     #ANSWER :

    str1 = "I love python"

    chars=[]
    for i in str1:
        chars.append(i)

    print (chars)



#7. For each character in the string saved in ael, append that character to a list that should be saved in a variable app.


     #ANSWER :

    ael = "python!"

    app=[]

    for i in ael:
        app.append(i)
    print (app)



#8. For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense).
     # Save these past tense words to a list called past_wrds.


     #ANSWER :

    wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

    past_wrds=[]

    for i in wrds:
        past_wrds.append(i+'ed')

    print (past_wrds)
