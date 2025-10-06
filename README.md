boo scary

# Towers of Hanoi (Python)


![Primary Language](https://img.shields.io/badge/Primary_Language-Python-yellow)

## Description

implementation of  the **Towers of Hanoi** puzzle in Python which simulates the classic puzzle where the goal is to move all disks from **Tower A** to **Tower C**, following specific rules.
The project shows the use of **STACK and LINKED LIST data structures** in Python.


## Project Report

You can view the full project documentation and code explanation here:  
📄 [Download Tower_of_Hanoi_Project_Report.docx](./Tower_of_Hanoi_Project_Report.docx)


## Features

* Implemented using **Stacks** with **Linked List** structure
* Three towers (A, B, C) represented as stack objects
* Disk using `*` characters
* User input validation (3–10 disks only)=
* Move validation following game rules
* Option to exit anytime using `X`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Soyaaaa081305/tower-of-hanoi.git
   ```
2. Navigate to the project directory:

   ```bash
   cd tower-of-hanoi
   ```

## Usage

Run the program using Python:

```bash
python main.py
```

When prompted, enter the number of disks (between 3 and 10).
The program will display three towers labeled **A**, **B**, and **C**, with disks represented by `*` symbols.

Example of console interaction:

```python
Enter number of disks (3-10): 3

Game start! Move all disks from A to C.
Type 'X' anytime to exit.
Enter move (e.g., A C): A B
Enter move (e.g., A C): A C
Invalid move: You cannot place a larger disk on smaller one!
```

## Rules of the Game

1. Only one disk may be moved at a time.
2. A disk can only be moved if it is the top disk of a tower.
3. No larger disk may be placed on top of a smaller disk.
4. The game ends when all disks are successfully moved to Tower C or when the user types `X` to exit.

## Dependencies

* Python 3.x
* No external libraries required

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


