from tower_logic import Stack

disk1 = Stack()
disk2 = Stack()
disk3 = Stack()

def main():
    while True: 
        #ok na to validation for number 3-10 only
        try: 
            disknum = int(input("Enter number of disks (3-10): ").strip())
            if 3<= int(disknum) <=10:
                break
            print("Enter a number between 3-10.")
        except ValueError:
            print("Enter an integer.")
    
    initializeStacks(disknum) #initializes stacks
    #printStacks()
    display()
    
    print("\nGame start! Move all disks from A to C.")
    print("Type 'X' to exit. ")
    
    while True:
        move = input("Enter move (e.g., A C): ").strip().upper()
        if move == "X":
            print("Exited successfully")
            break
        
        #splitting the move into two seperate parts
        splittedmove = move.split()
        if len(splittedmove) != 2:
            print("Please enter only two letters.")
        if splittedmove[0] not in "ABC" or splittedmove[1] not in "ABC":
            print("Please enter from ABC only ganire format A C not AC")
            

def display():
    current = disk1.top
    currentt = disk2.top
    currenttt = disk3.top
    while current and currentt and currenttt:
        print(current.value,currentt.value,currenttt.value)
        current = current.next
        currentt  = currentt.next
        currenttt = currenttt.next
    
def initializeStacks(num:int):
    space = ((num*2+1)-1)//2
    disk1.push(f"{space*' '}{" A"}{space*' '}")
    disk2.push(f"{space*' '}{" B"}{space*' '}")
    disk3.push(f"{space*' '}{"C"}{space*' '}")

    #need to solvbe
    for i in range(num ,0, -1):
        chuchu = 2 * i + 1 
        space = (num - i + 1)
        stringg = f"{space*' '}{chuchu*'*'}{space*' '}"
        disk1.push(stringg)

    for i in range(num ,0, -1):
        space = ((num*2+1)-1)//2
        stringg = f"{space*' '}{'|'}{space*' '}"
        disk2.push(stringg)
        disk3.push(stringg)

       




if __name__ == "__main__": 
    main()
    

def moveDiskAgain():
    pass





'''
def printTower():
    list1, list2, list3 = list()

{"   |   ","   |   "} 
{"   |   ","   |   "} 
{"   |   ","   |   "} 

for i in DISK_NUM:
    print(list1[i],list2[i], list3[i])

'''
