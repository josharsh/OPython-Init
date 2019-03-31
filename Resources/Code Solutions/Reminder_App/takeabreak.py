import webbrowser
import time
total_time=3
time_counter=0
print("This Program started on "+time.ctime())
while(time_counter<total_time):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=bmjYdc56gus")
    time_counter+=1

