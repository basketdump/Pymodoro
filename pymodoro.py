'''Python implementation of the Pomodoro Technique'''
import time
import notify2


def format_time(t):
    '''This method prints the time formatted to "hh:mm AM/PM"'''
    t_struct = time.localtime(t)
    return time.strftime("%I:%M %p", t_struct)



def notify(activity, end):
    '''This method sends a desktop notification of current activity'''
    activity_message = "Your " + activity + " has started."
    end_message = "It will end at " + end 
    notify2.Notification(activity_message, end_message).show() 
    return


def time_estimate(length):
    '''this method returns time now + length in minutes'''
    return time.time() + length # current time + length(mins)

def break_session(break_length):
    '''This method implements the small or long break sessions'''
    end = format_time(time_estimate(break_length))
    print("BREAK STARTED. Work resumes at", )
    notify("break", end)
    # pause for break_length minutes
    time.sleep(break_length)
    return


def work_session(work_length):
    '''This method implements the work session'''
    end = format_time(time_estimate(work_length))
    print("WORK STARTED. Next break is at", end)
    notify("work", end)
    # pause for work_length minutes
    time.sleep(work_length)
    return


def main():
    '''this is our main method to call and manage arguments to work and break
       and handle initial input'''
    
    # initialize notify2
    notify2.init('Pymodoro')

    work_length = int(input("Enter work interval (minutes): ")) * 60
    break_length = int(input("Enter short break interval (minutes): ")) * 60
    work_count = 0

    while (True):
        work_session(work_length)
        work_count += 1
        
        # is it time for a long break?
        if work_count % 4 == 0:
            break_session(break_length * 3) 
        
        else:
            break_session(break_length)

    return


main()

