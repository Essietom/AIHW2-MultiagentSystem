# -*- coding: utf-8 -*-


import threading
import time
import utility


def _main():
    while True:
        agent_number = input("Enter number of students in the class: ")
        try:
            val = int(agent_number)
            if val < 0:  # if not a positive int print message and ask for input again
                print("Sorry, input must be a positive integer, try again")
                continue
            break
        except ValueError:
            print("That's not an int!")   


    for i in range(1, int(agent_number) + 1):
        account_info = ("agent@rec.foi.hr", "tajna")
        thread1 = threading.Thread(
            target=utility.create_student_agent(account_info, i), args=(account_info, i)
        ).start()

    account_info = ("bzitkovic@rec.foi.hr", "agent48")
    thread2 = threading.Thread(
        target=utility.create_cordinator_agent(account_info), args=(account_info)
    ).start()

    account_info = ("posiljatelj@rec.foi.hr", "tajna")
    thread3 = threading.Thread(
        target=utility.create_voting_agent(account_info), args=(account_info)
    ).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping program...")    


if __name__ == "__main__":
    _main()
        
