# Pomodoro
# Final project
import time
seconds = 1 
minutes = 0.1 #60 * seconds 
hours = 60 * minutes  
work_duration=25 
short_break = 5*minutes 
long_break = 15*minutes
#Pomodoro_set = Pomodoro + short_break 
#Pomodoro_set_long = Pomodoro+long_break	
short_set_count = 3
long_set_count = 1
#Full_Pomodoro_set= Pomodoro_set*3 + Pomodoro_set_long
keep_running = 'y'
break_count = 0
ratings = []

def run_pomodoro_set():
 #import time and date 
 print "starting set"
 #time.sleep (work_duration)
 for minutes_count in range (work_duration):
 	time.sleep (minutes)
 	print minutes_count
 #once work_duration is complete print "You're done - good job! Take a break!"
 print "You're done - good job! Take a break!"
 print 
 #read input for answer
 performance_rating = raw_input("How did it go? 1-5:  ")
#accumulate information
 time.sleep (short_break)
 print "Break's over - get back to work!"
 return performance_rating
 
def run_long_pomodoro_set():
 #import time and date 
 time.sleep (work_duration)
 #once work_duration is complete print "You're done - good job! Take a break!"
 print "You're done - good job! Take a break!"
 performance_rating = raw_input("How did it go? 1-5:  ")
 #read input for answer
 time.sleep (long_break)
 print "Long break's over - get back to work!"
 return performance_rating
  
#start program
while keep_running == 'y':
  for set_count in range (short_set_count):
  	break_count += 1
 	ratings.append (run_pomodoro_set())
  for set_count in range (long_set_count):
  	break_count += 1
    ratings.append (run_long_pomodoro_set())
  keep_running = raw_input( "Start a new set? Y/N")

for set_count in range (len(ratings)):
	print "set",set_count+1, ratings[set_count]


print 'thanks for using Pomodoro. You took ', break_count, ' breaks today.'








