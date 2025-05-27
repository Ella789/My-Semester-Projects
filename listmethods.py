#Ella Leung
#1/22/25
#Initialize
#mySchedule stores a list of the classes you are currently taking at Jones  as strings
#Initialize the list with your first three periods ONLY
mySchedule = ["math 3", "english 2", "AP CSP"]
#Main

#Complete the following tasks using list/array methods. Print the result for each task.

#Task 1: Append periods 4 - 7 to the list
mySchedule.append("chem")
mySchedule.append("PE")
mySchedule.append("mandarin")
mySchedule.append("HUSH")
#Task 2: Insert your two lunch periods(A day and B Day) in their appropriate location
mySchedule.insert(3,"C lunch")
mySchedule.insert(7,"B lunch")
#Task 3: Remove your least favorite class
mySchedule.pop(0)
#Task 4: Print just your 2nd period class by accessing the appropriate index in your array
print(mySchedule[1])
#Task 5: Print only your A day schedule and then only your B day schedule
print(mySchedule[0:4])
print(mySchedule[4:8])
