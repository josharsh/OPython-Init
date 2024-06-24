# Practice Questions

 1. Create a **Cricle** class and intialize it with radius. Make two methods **getArea** and **getCircumference** inside this class.

    ```python
    class Circle():
        def __init__(self,radius):
            self.radius = radius
        def  getArea(self):
            return 3.14*self.radius*self.radius
        def getCircumference(self):
            return self.radius*2*3.14
    ```

 2. Create a **Temprature** class. Make two methods :
    * **convertFahrenheit** - It will take celsius and will print it into Fahrenheit.
    * **convertCelsius** - It will take Fahrenheit and will convert it into Celsius.

    ```python
    class Temprature():
        def  convertFahrenhiet(self,celsius):
            return (celsius*(9/5))+32
        def convertCelsius(self,farenhiet):
            return (farenhiet-32)*(5/9)
    ```

3. Create a **Student** class and initialize it with name and roll number. Make methods to :
    * **Display** - It should display all informations of the student.
    * **setAge** - It should assign age to student
    * **setMarks** - It should assign marks to the student.

    
    ```python
    class Student():
        def __init__(self,name,roll):
            self.name = name
            self.roll= roll
        def display(self):
            print self.name
            print self.roll
        def setAge(self,age):
            self.age=age
        def setMarks(self,marks):
            self.marks = marks
    ```

4. Create a **Time** class and initialize it with hours and minutes.
    * Make a method **addTime** which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
    * Make a method **displayTime** which should print the time.
    * Make a method **DisplayMinute** which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

    
    ```python
    class Time():
        def __init__(self, hours, mins):
            self.hours = hours
            self.mins = mins

        def addTime(t1, t2):
            t3 = Time(0,0)
            if t1.mins+t2.mins > 60:
            t3.hours = (t1.mins+t2.mins)/60
            t3.hours = t3.hours+t1.hours+t2.hours
            t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
            return t3

        def displayTime(self):
            print "Time is",self.hours,"hours and",self.mins,"minutes."

        def displayMinute(self):
            print (self.hours*60)+self.mins

        a = Time(2,50)
        b = Time(1,20)
        c = Time.addTime(a,b)
        c.displayTime()
        c.displayMinute()

    ```

5. Create a **deck** of cards class. Internally, the deck of cards should use another class, a **card** class. Your requirements are:

    * The Deck class should have a **deal** method to deal a single card from the deck
    * After a card is dealt, it is removed from the deck.
    * There should be a **shuffle** method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
    * The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

    
    ```python
    class Card:
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value

        def __repr__(self):
            return "{} of {}".format(self.value, self.suit)

    class Deck:
        def __init__(self):
            suits = ['Hearts','Diamonds','Clubs','Spades'] 
            values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
            self.cards = [Card(suit, value) for suit in suits for value in values]

        def __repr__(self):
            return "Cards remaining in deck: {}".format(len(self.cards))

        def shuffle(self):
            if len(self.cards) < 52:
                raise ValueError("Only full decks can be shuffled")
            shuffle(self.cards)
            return self

        def deal(self):
            if len(self.cards) == 0:
                raise ValueError("All cards have been dealt")
            return self.cards.pop()
     ```