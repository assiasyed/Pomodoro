# Pomodoro
Final project

#second = seconds = 1 
#minute = minutes = 60 * seconds 
#hour = hours = 60 * minutes  
#Work_duration= Pomodoro = 25*minutes 
#short_break = 5*minutes 
#long_break = 15*minutes
#Pomodoro_set = Pomodoro + short_break 
#Pomodoro_set_long = Pomodoro+long_break	
short_set_count = 3
long_set_count = 1
#Full_Pomodoro_set= Pomodoro_set*3 + Pomodoro_set_long
keep_running = 'y'
break_count = 0

def run_pomodoro_set():
 #import time and date 
 sleep (work_duration)
 #once work_duration is complete print "You're done - good job! Take a break!"
 print "You're done - good job! Take a break!"
 print "How did it go?"
 #read input for answer
 sleep (short_break)
 print "Break's over - get back to work!"
 
def run_long_pomodoro_set():
 #import time and date 
 sleep (work_duration)
 #once work_duration is complete print "You're done - good job! Take a break!"
 print "You're done - good job! Take a break!"
 print "How did it go?"
 #read input for answer
 sleep (long_break)
 print "Long break's over - get back to work!"
  
#start program
while keep_running == 'y':
  for set_count in range (short_set_count):
    run_pomodoro_set()
  for set_count in range (long_set_count):
    run_long_pomodoro_set()
print "Start a new set? Y/N"
read keep_running == 'y':


print 'thanks for using Pomodoro. You took ' + break_count + ' breaks today.'








