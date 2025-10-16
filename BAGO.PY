from tower_logic import Stack 

disk1 = Stack()
disk2 = Stack()
disk3 = Stack()
isRunnable = True
def main():
    global maxDisk
    while isRunnable: 
        #ok na to validation for number 3-10 only
        try: 
            maxDisk = int(input("Enter number of disks (3-10): ").strip())
            if 3<= int(maxDisk) <=10:
                break
            print("Enter a number between 3-10.")
        except ValueError:
            print("Enter an integer.")
    
    initializeStacks(maxDisk) #initializes stacks
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
        movediskAgain(splittedmove[0], splittedmove[1])
            

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
    maxwidth = num * 2 + 3
    disk1.push(f"{'A'.center(maxwidth)}")
    disk2.push(f"{'B'.center(maxwidth)}")
    disk3.push(f"{'C'.center(maxwidth)}")
    for i in range(num ,0, -1):
        disk_width = 2 * i + 1 
        stringg = ("*" * disk_width).center(maxwidth)
        disk1.push(stringg)


    for i in range(num ,0, -1):
        spacer = "|".center(maxwidth)
        disk2.push(spacer)
        disk3.push(spacer)


def getLastDisk(stack):
    lines = 0
    maxwidth = maxDisk * 2 + 3
    spacer = "|".center(maxwidth)

    while not stack.is_empty():
        current = stack.peek()
        if "A" in str(current).strip() or "B" in str(current).strip() or "C" in str(current).strip() or "*" in str(current).strip():
            nahanapnadisk = str(current).strip()
            break
        if str(current).strip() == "|":
            lines += 1
            stack.pop()  
            
    #for spacers
    for i in range(lines):
        stack.push(spacer)
    lines = 0
    return nahanapnadisk
        





def movediskAgain(source, destination):
    
    s = {
        "A": disk1,
        "B": disk2,
        "C": disk3
    }

    #mismung stack
    src_ = s[source]
    dst_ = s[destination]
    
    #mga last disk
    src_lastdisk = getLastDisk(s[source])
    dst_lastdisk = getLastDisk(s[destination])


    
    if len(src_lastdisk) < len(dst_lastdisk) or len(src_lastdisk) == 1 or len(dst_lastdisk) == 1:

        #TRAVERSE THRU SOURCE AND POP IT------------------------------BRUH
        srclinesS = 0
        
        while not src_.is_empty():
        
            current = src_.peek()
            if "A" in str(current).strip() or "B" in str(current).strip() or "C" in str(current).strip() or "*" in str(current).strip():
             
                src_.pop()
                break
            if str(current).strip() == "|":               
                srclinesS += 1
                src_.pop()

        #for disk and spacers nya
        maxwidth = maxDisk * 2 + 3
        spacer = "|".center(maxwidth)

        for i in range(srclinesS+1):
            src_.push(spacer)

            
        #TRAVERSE THRU THE DESTINATION--------------------------------
        dstlines = 0
        while not dst_.is_empty():
            
            current = dst_.peek()
            if "A" in str(current).strip() or "B" in str(current).strip() or "C" in str(current).strip() or "*" in str(current).strip():
                break
            if str(current).strip() == "|":               
                dstlines += 1
                dst_.pop()

        #for disk and spacers nya
        maxwidth = maxDisk * 2 + 3
        dst_.push(src_lastdisk.center(maxwidth))   

        
        spacer = "|".center(maxwidth)
        #for spacers
        for i in range(dstlines-1):
            dst_.push(spacer) 
        

        display()
        if "*" in str(disk3.peek()):
            print("Congratulations! You've solved the Tower of Hanoi!")
            isRunnable == False 


    else:
        print("\nInvalid move! Cannot place larger disk on top of smaller disk.")

    


if __name__ == "__main__": 
    main()
    
