import matplotlib.pyplot as plt
import math

# conclusion this is NOT log
# for loops seperated for readability

results=[]
x_value=[]

times_to_loop = 500


quad = []
for i in range(1, times_to_loop):
    quad.append(i**2)

#log!?
for c in range(1, times_to_loop):
    arr =[]

    count = 0
    number_of_times_we_iterate = c
    


    for i in range(1, number_of_times_we_iterate):
        for j in range(i+1, number_of_times_we_iterate):
            arr.append(count)
            count+=1

    results.append(count)
    x_value.append(c)

log=[]
# log base 2
for i in range(1, times_to_loop):
    log_at_i = math.log2(i)
    log.append(log_at_i)



# add labels
plt.xlabel("Number of elements")
plt.ylabel("Operations performed")

# give each scatter a name for the legend
weird_algorithm_from_class=plt.scatter(x_value, results, color='k', s=5)
quadratic=plt.scatter(x_value, quad)
log=plt.scatter(x_value, log)

# append legend
plt.legend((weird_algorithm_from_class, quadratic, log),("Algorithm from class", "Quadratic", "Logarithm"))
plt.title("Different algorithm times")

plt.show()