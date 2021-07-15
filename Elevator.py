#!/usr/bin/env python
# Simone Susino D18124815

'''
The goal of this project is to gain more practice with classes and Object-Oriented Programming. In this project, we are going to simulate a simple elevator. You can also show how different strategies can affect the efficiency of an elevator.
Task

Your task is to implement the simple elevator in Python using classes. The default strategy is the simple "start at the bottom, go to the top, then go to the bottom". Can you write a better strategy, one that is more efficient? You don't have to use this, you can take an alternative approach such as random start location for the elevator.
Project Description / Specification

    Create three classes: Building, Elevator, and Customer.
    Equip the building with an elevator. Ask user to customize the number of floors and the number of customers.
    Program should have error checking to make sure the user inputs are valid. For example, if a user gives non-integer inputs, notify the user that the inputs are incorrect and prompt again.
    Each customer starts from a random floor, and has a random destination floor.
    Each customer will use the elevator only once, i.e., when a customer moves out of the elevator, he/she will never use it again.
    When all customers have reached their destination floor, the simulation is finished.
    Part of the grade on this assignment will be the appropriateness of your classes, methods, and any functions you use. The quality of the code will now matter as well as the performance.
    All classes' methods require a docstring for a general description of the method.
    Create an appropriate GUI front-end for your program using Tkinter.
    Implement both your own strategy and the default strategy and compare. Your strategy does not have to be better but the comparison is required.
    Don't use any global variables.


    Two run methods created that works in a different way (explained in the comments)

    I added a counter to count the moves of the elevator so I can estimate the performance for the 2 different methods
    (ex. run the code 3/4 times and do an average how many moves the elevator did with a certain number of floors and customers

'''
import random


class Building(object):
    '''Building class, to create an instance of the building object that contains the elevator'''

    def __init__(self, floors=0, customers=0):
        '''Initialise the building with floors, customers,
        a list of processed customer and an instance of the object elevator'''
        self.floors = floors # Number of floors in the building
        self.custList = [] # The customer list waiting for the elevator
        self.processedList = [] # The customer that have already been served
        self.elevator = Elevator(floors) # The elevator of the building

    # def run(self):
    #     '''Another of the method to run the elevator
    #     this method is not the best if we consider the performance as in the first loop we load all the passenger in the elevator.
    #     Once all the passenger are in the elevator, we start to leave the customer to the floor requested'''
    #     while len(self.custList) != 0:                            # run until the len of waiting list is 0
    #         for customer in self.custList:                        # loop for the list of waiting customers
    #             print(self)
    #             if self.elevator.currFloor == customer.currFloor:   # check if the elevator is in the same floor where customer is waiting
    #                 self.elevator.registerCust(customer)            # call the method to add the current customer to the registered list
    #                 self.custList.remove(customer)                  # and remove it from the waiting list
    #         self.elevator.move()                                    # call the method to move the elevator
    #
    #     while len(self.elevator.registeredList) != 0:
    #         for x in self.elevator.registeredList:              # loop for the customer inside the elevator
    #             print(self)
    #             if self.elevator.currFloor == x.destFloor:      # if the elevator is at the same floor where customer is
    #                 # self.elevator.cancelCust(x)
    #                 self.elevator.registeredList.remove(x)      # remove it from the registered list and add the customer
    #                 self.processedList.append(x)                # to the processed list
    #         self.elevator.move()

    def run(self):
        '''One of the method to run the elevator
        This method will check the customer in the waiting list and depends which floor is the elevator will get the
        customer and leave him at the floor selected. Once a customer is done, another customer is allowed to enter in
        the elevator. Not the best, as multiple customer cannot be served at the same time'''
        while len(self.custList) != 0:
            for customer in self.custList:
                # print(self)
                if self.elevator.currFloor == customer.currFloor:
                    self.elevator.registerCust(customer)
                    self.custList.remove(customer)
                    while customer.inElevator == True:
                        for x in self.elevator.registeredList:
                            print(self)
                            if self.elevator.currFloor == x.destFloor:
                                self.elevator.cancelCust(x)
                                self.elevator.registeredList.remove(x)
                                self.processedList.append(x)
                        self.elevator.move()
            self.elevator.move()

    def __str__(self):
        '''The string representation for the output'''
        retStr = "-" * 80
        retStr += "\n" + str(self.custList)
        retStr += "\nWaiting" + str(self.custList) # Customers waiting for the elevator
        retStr += "\nIn elevator" + str(self.elevator.registeredList) # Customers inside the elevator
        retStr += "\nFinished" + str(self.processedList) # Customer that reached the destination floor
        return retStr

    def __repr__(self):
        return self.__str__()


class Elevator(object):
    '''Elevator class, each building has an instance of Elevator.
    We randomly assign the current floor where it starts
    When the elevator reach the top floor, it goes down and vice versa when it reaches the ground floor'''
    def __init__(self, floors=0):
        self.moves = 0
        self.floors = floors # Number of floors
        self.registeredList = [] # Customer in the elevator
        self.currFloor = random.randint(0, self.floors - 1) # Random number for the floor of the elevator
        self.direction = random.choice((-1, 1)) # Direction for the elevator, up and down
        self.count = 0 # count how many times elevator moves

    def __str__(self):
        '''The string representation for the output'''
        return "Elevator at Floor " + str(self.currFloor) + " direction is " + str(self.direction) + " moves " + str(
            self.moves)

    def __repr__(self):
        return self.__str__()

    def move(self):
        '''Move the elevator up and down'''
        if self.currFloor == self.floors - 1:
            self.direction = -1
        elif self.currFloor == 0:
            self.direction = 1

        self.currFloor += self.direction
        self.count += 1 # counter for the moves
        print(self.count)

    def registerCust(self, customer):
        '''Customer enters in the elevator'''
        self.registeredList.append(customer)
        customer.inElevator = True
        # customer.finished = False

    def cancelCust(self, customer):
        '''Customer exited from the elevator'''
        customer.inElevator = False
        customer.finished = True


class Customer(object):
    '''Create the instance of Customer
    The customer enters in the elevator at a certain floor and exits from the elevator
    when he reaches a determined floor'''
    def __init__(self, currFloor, destFloor, custId):
        self.currFloor = currFloor # Current floor of the elevator
        self.destFloor = destFloor # Destination floor of the elevator
        self.custId = custId # Customer ID
        self.inElevator = False # Customer in/out flag
        self.finished = False # Customer served flag

    def __str__(self):
        '''The string representation for the output'''
        return str(self.currFloor) + "-" + str(self.destFloor)

    def __repr__(self):
        return self.__str__()


def main():
    '''The function main start the program.
    Values of numbers of floors and customers are inserted by the user.
    He generates the instance of Building and Customers'''
    try:
        floors = int(input("Number of floors:\n"))
        if floors < 0:
            raise ValueError
    except ValueError:
        print("Number of floors must be a positive number\n")
        quit()

    try:
        customers = int(input("Number of customers:\n"))
        if customers <= 0:
            raise ValueError
    except ValueError:
        print("Number of customers must to be a positive integer\n")
        quit()

    print("=" * 80)
    print("Sample Run\nBuilding has", str(floors), "floors and", str(customers), "customers")

    newBuilding = Building(floors, customers)

    # add a customer in the Building object

    for cust in range(customers):
        new = Customer(random.randint(0, floors - 1), random.randint(0, floors - 1), cust)
        # check the current floor of the customer, to ignore if the customer is already in the destination floor
        if new.currFloor != new.destFloor:
            newBuilding.custList.append(new)
        else:
            newBuilding.processedList.append(new)
            new.finished = True
            print("=" * 80)

    while not (len(newBuilding.custList) == 0 and len(newBuilding.elevator.registeredList) == 0):
        newBuilding.run()

    print("=" * 80)

if __name__ == '__main__':
    main()
