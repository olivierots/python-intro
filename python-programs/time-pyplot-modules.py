# exercise: time & Pyplot
# create a program to help the user type faster. Give him a word and ask him to write it 5 times
# check how many seconds it took him to type the word at each round
# in the end, tell the user how many mistakes were made and show a chart with the typing speed
# evolution during 4 secs

# import modules first 
import matplotlib.pyplot as plt
import time as t

# list of the times
times = []
# var to store the No of mistakes
mistakes = 0

print(" this program will help you type faster. You will have to type the word 'programming' as fast as you can for 5 times")
input("Press enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)
    if (word.lower() != "programming"):
        mistakes += 1

print ("you made " + str(mistakes) + " mistake(s).")
print("Now lets see your evolution")
t.sleep(3)

# the attempts
x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x,legend)
plt.ylabel('Time in seconds')
plt.xlabel('attempts')
plt.title('your typing evolution')

plt.show()




