---
title: Time Efficiency
date: 2019-03-20
tags: ["python", "code"]
---

Some time ago I have started to do Python coding and subscribed myself to [Dailycoding](https://www.dailycodingproblem.com) to improve my Python skills. It works the way that they send you a coding problem each day that you can solve.

First day I have received a coding problem [Feb27_2019.py](https://gitlab.com/zerodayz/dailycoding/blob/master/Feb27_2019.py) that gives you `list of integers` and number `k` as an input. You need to find whether any two numbers from the `list` adds up to `k`.

The first solution that came to my mind was using `double for-loop`, basically iterate over each element in the given `list` and try to `sum` the two values to see if they adds up to `k`:

## Double for-loop

```bash
def double_for_loop(l, n):
    for i in range(len(l)):
        # print("Processing number at position i: ", i)
        # print(l[i])
        for j in range(len(l)):
            if i == j:
                pass
            elif l[i] + l[j] == n:
                # print("Found number ", l[i], " + ", l[j], " is ", n, ".")
                return True, l[i], l[j]
```

This code worked on the given input quite fast:

```bash
mylist = [10, 15, 11, 5, 20]
k = 30
```

However I wanted to see how fast this code works, I have added additional code with `time.time()` and measured time.

## Measuring time with time.time()

```bash
def double_for_loop(l, n):
    start = time.time()
    for i in range(len(l)):
        # print("Processing number at position i: ", i)
        # print(l[i])
        for j in range(len(l)):
            if i == j:
                pass
            elif l[i] + l[j] == n:
                # print("Found number ", l[i], " + ", l[j], " is ", n, ".")
                end = time.time()
                print("Elapsed time: ", end - start)
                return True, l[i], l[j]
```

Apparently with small `list` like this, the code is pretty fast, so I needed to write code to generate my own `list` of `n` elements.

## Generating input

```bash
n = 100000


def generate_input(n):
    start = time.time()
    randomlist = [None] * n
    for i in range(0, len(randomlist)):
        randomlist[i] = random.randint(1, n)
    sortedrandomlist = sorted(randomlist)
    randomnumber = random.randint(1, n)
    end = time.time()
    print("Elapsed time: ", end - start)
    return randomnumber, randomlist, sortedrandomlist
```

With all the `print` statement it showes that processing took:

```bash
Searching for two numbers using double for-loop method that adds up to  7838  within  100000 items.
Elapsed time:  0.3900914192199707
double_for_loop: Found  7462  and  376  adds up to  7838
```

Since I am curious person I started to slowly increase the `n` number of elements in the list up to `10 millions` and eventually run into issues where my laptop got stuck and I had to reboot.

This is where I started to look for better method solving this problem.

I found efficient `algorithm` that could do a job that took previously minutes into few seconds on `list` with millions and millions of elements. Eventually I run into problem generating huge `list` of elements but that is another problem.

My implementation of `Binary search` algorithm is here.

## Binary search

```bash
def binary_search(l,n):
    start = time.time()
    high_val_index = len(l)-1
    low_val_index = 0

    while low_val_index != high_val_index:
        if l[low_val_index] + l[high_val_index] == n:
            end = time.time()
            print("Elapsed time: ", end - start)
            return True, l[low_val_index], l[high_val_index]
        elif l[low_val_index] + l[high_val_index] > n:
            high_val_index -= 1
        elif l[low_val_index] + l[high_val_index] < n:
            low_val_index += 1
    return False
```

Based on this experience I have decided to enroll in [Data Structures and Algorithms](https://classroom.udacity.com/courses/ud513/) course which I believe is benefical for everyone who really care about good coding.

The full source code can be found [here](https://gitlab.com/zerodayz/dailycoding/blob/master/Feb27_2019.py)
