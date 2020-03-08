# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# November 5, 2019                                    |
# Kristoff Finley                                     |
# -----------------------------------------------------

class Queue:
    def __init__(self, number): #inializing variables needed in program 
        self.number = number
        self.empty_list = []
        self.empty_string = ''
        self.item_dequeue = 0

    def __str__(self):
        result = "Contents: " + str(self.empty_string) #formatting for prnting 
        return result

    def __iadd__(self, other):
        result = self.enqueue(other)
        return result  
        
    
    def enqueue(self, number): #adds elements to the list if not allready in, incrementally
        self.empty_list.append(number)
        for i in self.empty_list:
            if str(i) not in self.empty_string:
                self.empty_string += str(i) + " "
        return self.empty_string

    def dequeue(self): #removes the first item from the list 
        if len(self.empty_list) > 0:
            self.item_dequeue = self.empty_list[0]
            self.empty_list.remove(self.item_dequeue)
            self.empty_string = self.empty_string[2:]
            
        return self.item_dequeue


    def is_empty(self): #checks to see if the list is empty 
        flag = False
        count = len(self.empty_list)
        while count > 0 and flag == False: #if more than one element in the list, return false 
                count -= 1
                return flag
        flag = True
        return flag #return true if there is no more elements in the list 

    
        
            
            
            
    
        

# -----------------------------------------------------

def main():
    numbers = Queue("Numbers") #instantiating the "Queue class" with "numbers"

    print("Enqueue 1, 2, 3, 4, 5") #adding elements to the list 
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item") #taking away one item from the list 
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items") #taking out all of the items from the list 
    print("---------------")
    while not numbers.is_empty():  
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15): #queuing elements 10 to 14 to the list (does not start at 1) 
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15 #uses the __iadd__ method to "add" 15 to the end of the list

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
