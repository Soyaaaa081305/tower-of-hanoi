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
            continue
        if splittedmove[0] not in "ABC" or splittedmove[1] not in "ABC":
            print("Please enter from ABC only ganire format A C not AC")
            continue
        movediskAgain(splittedmove[0], splittedmove[1], disknum)
            

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
    maxwidth = num * 2 + 1
    disk1.push(f"{'A'.center(maxwidth)}")
    disk2.push(f"{'B'.center(maxwidth)}")
    disk3.push(f"{'C'.center(maxwidth)}")
    for i in range(num ,0, -1):
        disk_width = 2 * i - 1 
        stringg = ("*" * disk_width).center(maxwidth)
        disk1.push(stringg)


    for i in range(num ,0, -1):
        spacer = "|".center(maxwidth)
        disk2.push(spacer)
        disk3.push(spacer)

              
        
def movediskAgain(source, destination, maxDisk):
    s = {
        "A": disk1,
        "B": disk2,
        "C": disk3
    }

    src_ = s[source]
    dst_ = s[destination]
    
    if len(str((src_.peek())).strip()) > len(str((dst_.peek())).strip()):
        
        disk = src_.pop().strip()
        lines = -1
        while not dst_.is_empty():
            current = dst_.peek()
            if "A" in str(current).strip() or "B" in str(current).strip() or "C" in str(current).strip() or "*" in str(current).strip():
                break
            if str(current).strip() == "|":
                lines += 1
                dst_.pop()

        #for disk and spacers nya
        maxwidth = maxDisk * 2 + 1
        dst_.push(disk.center(maxwidth))   

        #for spacers
        for i in range(lines):
            spacer = "|".center(maxwidth)
            dst_.push(spacer) 
        

        
        display()

    else:
        print("INVALID MOVE!")
    
    


if __name__ == "__main__": 
    main()
    

'''
def printTower():
    list1, list2, list3 = list()

{"   |   ","   |   "} 
{"   |   ","   |   "} 
{"   |   ","   |   "} 

for i in DISK_NUM:
    print(list1[i],list2[i], list3[i])

'''
