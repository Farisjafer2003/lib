'''Library Management System
1. User Functionality
    * Borrow book
    * Return book
2. Common Functionality
    * View Available books
    * Search book
'''

import library
import sys
from common import get_all_books, get_available_books, bookexists

def libraryHome():
    print("************************* WELCOME TO FARIS LIBRARY ********************\n")
    #print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n""")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. List all books\n2. List available books\n3. Search Book\n4. Borrow Book\n5. Return Book\n6. exit the library\n""")

    while True:
        # print(track)
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # All books
                get_all_books()
            elif usr_response == 2:  # Available books
                get_available_books()
            elif usr_response == 3:  # Search books
                bookname = input("Enter book name to search : ")
                bookexists(bookname)
            elif usr_response == 4:  # Borrow book
                bookname = input("Enter book name to borrow : ")
                library.borrow_book(bookname)
            elif usr_response == 5:  # Return book
                bookname = input("Enter book name to return : ")
                library.return_book(bookname)
            

            elif usr_response == 6:  # exit
                print("THANK YOU ! \n")
                sys.exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:  # catch errors
            print(f"{e}---> INVALID INPUT!,PLEASE ENTER VALID INPUT \n")

libraryHome()














