# Learning Object Oriented Python

This repository walks you through the Object Oriented Programming in python. Illustrates real-world examples, working codes and going about finding a coding solution.

The course plan is as shown on the repository. There are four lessons which govern the flow of the course. It is highly recommended to refer to online resources for a detailed study about the mentioned topics which have been briefly covered.

For the Tasks study in depth about the problem statements, conduct online research about various available modules and then start coding. Coding solutions have been provided in the resources folder. 


# Python Data Structures



##   1.List
	
     * Lists in Python are one of the most versatile collection object types available.
     * Lists can be used for any type of object, from numbers and strings to more lists.

     * Python program to illustrate 
  
     * Declaring a list 
     L = [1, "a" , "string" , 1+2] 
     print L 
  
     * add 6 to the above list 
     L.append(6) 
     print L 
  
     * pop deletes the last element of the list 
     L.pop() 
     print L 
  
     print L[1] 
     
     Output:

     [1, 'a', 'string', 3]
     [1, 'a', 'string', 3, 6]
     [1, 'a', 'string', 3]
     a
    

##   2.Dictionary

     * In python, dictionary is similar to hash or maps in other languages. 
     * It consists of key value pairs. 
     * The value can be accessed by unique key in the dictionary.
 
     * Syntax:
       dictionary = {"key name": value}
       
     * Python program to illustrate 

     * Create a new dictionary  
 
     d = dict() # or d = {} 
  
     * Add a key - value pairs to dictionary 
     d['xyz'] = 123
     d['abc'] = 345
  
     * print the whole dictionary 
     print d 
  
     * print only the keys 
     print d.keys() 
  
     * print only values 
     print d.values() 
  

     * Output:
     {'xyz': 123, 'abc': 345}
     ['xyz', 'abc']
     [123, 345]


##   3.Tuple

      * Python tuples work exactly like Python lists except they are immutable,
        i.e. they can’t be changed in place. 
      *They are normally written inside parentheses to distinguish them from lists
  
      * Python program to illustrate 
      
       tup = (1, "a", "string", 1+2) 
       print tup 
       print tup[1] 

       * Output:
       (1, 'a', 'string', 3)
       a
  

##    4.Sets

      * Unordered collection of unique objects.
      * Set operations such as union (|) , intersection(&), difference(-) can 
        be applied on a set.
      * Sets are immutable i.e once created further data can’t be added to them
      * () are used to represent a set.

      * Python program to demonstrate working of Sets
   
      * Creating two sets 
        set1 = set() 
        set2 = set() 
   
      * Adding elements to set1 
        for i in range(1, 6): 
            set1.add(i) 
   
      * Adding elements to set2 
       for i in range(3, 8): 
           set2.add(i) 

      
      * Converting List to Set
	L = [1,1,2,3,4,4]
        set3 = set(L)
   
       print("Set1 = ", set1) 
       print("Set2 = ", set2)
       print("Set3 = ", set3) 
       
       Output:
       Set1 = {1, 2, 3, 4, 5}
       Set2 = {3, 4, 5, 6, 7}
       Set3 = {1,2,3}
     
         
