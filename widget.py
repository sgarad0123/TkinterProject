def most_frequent(is_canceled_list):
    counter = 0
    num = is_canceled_list[0]

    for i in is_canceled_list:
        curr_frequency = is_canceled_list.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

is_canceled_list=[1,2,1,2,2,2,3,4,5]
data=(most_frequent(is_canceled_list))
print(f" 0 for Not cancelled & 1 for cancelled {data}")
