# Pomodoro Timer

import time

def pomodoro_timer(work_minutes, break_minutes, rounds):
    for round_count in range(rounds):
        print("Round", round_count + 1)
        
        # Work interval
        print("Work for", work_minutes, "minutes.")
        time.sleep(work_minutes * 60)
        
        # Break interval
        print("Take a break for", break_minutes, "minutes.")
        time.sleep(break_minutes * 60)
    
    print("Pomodoro timer completed!")

# Test the Pomodoro Timer
work_time = int(input("Enter the work time in minutes: "))
break_time = int(input("Enter the break time in minutes: "))
rounds = int(input("Enter the number of rounds: "))

pomodoro_timer(work_time, break_time, rounds)


'''
=================================
Test Case:
=================================

Enter the work time in minutes: 30
Enter the break time in minutes: 20
Enter the number of rounds: 4
Round 1
Work for 30 minutes.

'''