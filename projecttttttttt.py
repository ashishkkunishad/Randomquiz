while True:
    import random
    print('''          >>>> QUIZ <<<<''')
    print('''1.Start quiz
2.Exit''')
    f=input('Select one option :- ')
    if f=='1':
        count=0
        for j in range(5):
            if j==0:
                print('''----> First round of Quiz starts now <----
        ANSWER TO QUESTION ONLY IN True and False''')
                QUESTIONSp = [[">> The expression int(x) implies that the variable x is converted to integer:  ","True"],
 [">> The value of the expressions 4/ (3*(2 - 1)) and 4/3*(2- 1) is the same:  ","True"]
,[">> The expression 2**2**3 is evaluated as: (2**2) **3:  ","False"]
,[">> A string can be surrounded by three sets of single quotation marks or by three sets of double quotation marks:  ","True"]]
    
                random.shuffle(QUESTIONSp)
                for i in QUESTIONSp:
                    answer=input(i[0])
                    if answer == i[1]:
                        print("Congrats you have selected right answer")
                        count+=1
                    else:
                        print("The answer is", i[1], 'not' ,answer)
                print('----> First round of Quiz ends now <----')
            if j==1:
                QUESTIONSp = [[">> Variables can be assigned only once:  ","False"],[">> In Python, a variable is a placeholder for data:  ","False"],["In Python, only if statement has else clause:  ","False"]
                            ,[">> Python loops can also have else clause:  ","True"],[">> In a nested loop, a break statement terminates all the nested loops in one go:  ","False"]]

                print('----> Second round of Quiz starts now <----')
                random.shuffle(QUESTIONSp)
                for i in QUESTIONSp:
                    answer = input(i[0])
                    if answer == i[1]:
                        print("Correct!")
                        count+=1
                    else:
                        print("The answer is", i[1], 'not' ,answer)
                print('----> Second round of Quiz ends now <----')
            
            if j==2:
                print('----> Third round of Quiz starts now <----')
            
                QUESTIONSp = [[">> Do both the following represent the same list ['a', b, c'],['c', 'a', 'b']:  ","False"]
,[">> A list may contain any type of objects except another list:  ","False"]
,[">> There is no conceptual limit to the size of a list:  ","True"]
,[">> All elements in a list must be of the same type:  ","False"]
,[">> A given object may appear in a list more than once:  ","True"]
    
            ]
                random.shuffle(QUESTIONSp)
                for i in QUESTIONSp:
                    
                    answer = input(i[0])
                    if answer == i[1]:
                        print("Correct!")
                        count+=1
                    else:
                        print("The answer is", i[1], 'not' ,answer)
                print('----> Third round of Quiz ends now <----')
            if j==3:
                print('----> Fourth round of Quiz starts now <----')
            
            
                QUESTIONSp = [[">> The keys of a dictionary must be of immutable types:  ","True"]
,[">> You can combine a numeric value and a string by using the + symbol: ","False"]
,[">> The clear( ) removes all the elements of dictionary but does not delete the empty dictionary:  ","True"]
,[">> The max() and min() when used with tuples, can work if elements of the tuple are all of the same type:  ","True"]
,[">> A list of characters is similar to a string type:  ","False"]
    
            ]

            
                random.shuffle(QUESTIONSp)
                
                for i in QUESTIONSp:
                    answer = input(i[0])
                    if answer == i[1]:
                        print("Correct!")
                        count+=1
                    else:
                        print("The answer is", i[1], 'not' ,answer)
                print('----> Fourth round of Quiz ends now <----')
            
            
            
            if j==4:
                print('----> Fifth round of Quiz starts now <----')
                QUESTIONSp = [[">> For any index n, s [: n] + s [n :] will give you original string s:  ","True"]
,[">> A dictionary can contain keys of any valid Python types:  ","False"]
,[">> The two statements x int(22=0/7) and x=int(22/7=0) yield the same results:  ","True"]
,[">> The given statement: x + 1 = x is a valid statement:  ","False"]
,[">> List slice is a list in itself:  ","True"]]
                random.choice(QUESTIONSp)
                for i in QUESTIONSp:
                    answer = input(i[0])
                    if answer == i[1]:
                        print("Correct!")
                        count+=1
                    else:
                        print("The answer is", i[1], 'not' ,answer)
                print('----> Fifth round of Quiz ends now <----')
                print("          <<<RESULT>>>")
            print("- - - ->",count,'the correct option you have given <- - - -')
    elif f=='2':
        break
    else:
        print('Invalid')
    
