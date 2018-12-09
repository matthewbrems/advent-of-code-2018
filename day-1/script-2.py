import time
t0 = time.time()

file = open('./day_1_input.txt', 'r')

current_freq = [int(i) for i in file]

resulting_freq = [sum(current_freq[:1])]
last_i = 1
i = 2

while True:
    for j in range(last_i, i):
        mod = j % len(current_freq)
        resulting_freq.append(resulting_freq[-1] + current_freq[mod])
    if len(set(resulting_freq)) != i:
        break
    print(f"We have {i} iterations in {round(time.time() - t0, 1)} seconds.")
    last_i = i
    i *= 2

print(f"Changing loops - answer is between {last_i} and {i}. Time elapsed is {round(time.time() - t0, 1)} seconds.")

min_value = last_i
max_value = i

while True:
    mean_value = round((min_value + max_value) / 2)
    print(f"Min: {min_value}, Mean: {mean_value}, Max: {max_value}")
    
    if len(set(resulting_freq[0:(mean_value + 1)])) != (mean_value + 1):
        if max_value - min_value <= 1:
            print(mean_value, resulting_freq[mean_value])
            break
        else:
            max_value = mean_value
    else:
        min_value = mean_value

print(f"This all took {time.time() - t0} seconds!")
