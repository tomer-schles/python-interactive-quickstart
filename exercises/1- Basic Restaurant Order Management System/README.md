

# Exercise #1 - Basic Food Ordering System
### Tomer's Interactive python quickstart guide

## Topics Covered:
  * String manipulation
  * input
  * parsing 
  * for loops
  * dictionaries


# Instructions:
  The written instructions below complements the code *template provided in - orders_management_system.py

  You are hired to program an easy to use food ordering system.
  Your system need to support commands with the following syntax
    
  ```
  COMMAND ARG1 ARG2 ARG3 ARG4
  ```
  
  Required Commands:
  * add / remove - dish addition & removal
    
    ```"add" [/ "remove"] "dish1" "dish2" "dish3" ... ``` - where by each food is the food to add
      
    example: ```add Pizza Pasta Potatos```
    
  * order - orders a new dish
          
    ```"order" "dish1:amound2" "dish2:amound2" ...```

    When an invalid dish is ordered it should notify the user about the error
          
    example: ```order pizza:1 pasta:2```
    
  * print order status - prints which foods have been ordered and amount ordered

    ```"status"```
    
    example: ```status```

    example output:

    ```
    Current Orders:
        Pizza   -  2
        Pasta   -  3
        Potatos -  0
    ```
    
  * reset orders - resets all foods to 0

    ```"reset"```

    example: ```reset```



# Steps:
  Not yet available :-)
    
    
  
# Pro Challenges
  Complete This Challenges after everything is working
  * Change OrderManagementSystem.__orders to a collections.Counter object - https://docs.python.org/2/library/collections.html#collections.Counter

# Other Solutions
  A sneaky one, aren't you? don't cheat. When you'll finish your solution you'll get to see other solutions to compare and learn.