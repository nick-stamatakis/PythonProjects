# -*- coding: utf-8 -*-
"""Nicholas Stamatakis CSE 101 Lab Exercises Set #9: Random Numbers and Simulation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oFFIPThg1P5A12qos2qebkeJJMH32Tm5

#CSE 101: Computer Science Principles

####Stony Brook University, Summer 2021, Session I Extended

### Lab Exercises Set #9

#### Due: Sunday, June 27, 2021 at 11:59 pm EDT

### Learning Outcomes
By the end of these exercises you should be able to:
* Write short code segments to generate random values.
* Write short code segments that access fields of objects and call methods on objects.

### Random Numbers: Basics

E1. Run the cell below.
"""

import random

"""E2. Using only `random.randint`, display a random integer in the range 100 through 200, inclusive. (Remember: `randint`'s second value is *inclusive*, not *exclusive*! `randint` and `range` don't work the same way.)"""

random.randint(100,200)

"""E3. Using `random.random()` only, generate a random real number in the range $[0.0, 5.0)$. Don't use `random.uniform()` for this exercise!"""

random.random()*5

"""E4. Using `random.random()` only, generate a random real number in the range $[-10, 20)$. Don't use `random.uniform()` for this exercise!"""

-10 + random.random()*30

"""E5. Using `random.uniform()` only, generate a random real number in the range $[25.0, 75.0)$."""

random.uniform(25,75)

"""E6. Create a list of 5 names in a list called `names`. Then, using `random.choice()` only, choose a name at random from the list and display it."""

names=['John', 'Nick', 'Mike', 'Troy', 'Mary']
print(random.choice(names))

"""E7. Using `random.sample()` only, choose 4 names at random from your `names` list and display the 4 names."""

print(random.sample(names, 4))

"""E8. Using `random.sample()` only, attempt to choose 6 names at random from your `names` list. What happens?"""

print(random.sample(names, 6))
#There is a runtime error because the population is not big enough to support a k value of 6.
# This is because sample() doesn't replace the items in a list so there will be zero items 
# remaining at some point if the population is greater than the k value.

"""E9. Using `random.choices()`, choose names 8 times from your `names` list and store them in a list. Display the chosen names."""

print(random.choices(names, k=8))

"""E10. Consider the code below, which fills the list `nums` with the integers 1 through 10. Run the cell."""

nums = list(range(1, 11))
nums

"""E11. Using `random.shuffle()` only, *permute* (shuffle) the list and display the shuffled list."""

random.shuffle(nums)
print(nums)

"""### Random Numbers: Experiments

E12. Simulate the flipping of two *fair coins* 1000 times. A fair coin is one that has equal probability of showing heads or tails. Count the number of times two heads show up and display that count. The count should be close to 250. If not, double-check and fix your code. Hint: use the `random.random()` function, where a return value $\le 0.5$ means *heads*, and a return value $>0.5$ means *tails*.
"""

two_heads=0

for i in range(1000):
    if random.random() <= 0.5:
        if random.random() < 0.5:
            two_heads += 1
     
print(f'You flipped two heads {two_heads} times')

"""E13. Simulate the rolling of two 6-sided dice 1000 times and compute the average of the sums. Display that average. The average should be close to 7.0. If not, double-check and fix your code."""

import random 
sum=0
for i in range(1000): 
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    sum += die1 + die2
average=sum/1000
print(f'The average of the sums is {average}')

"""E14. Imagine that the price of a car starts at \$20,000 and with **50%** chance each day increases by \$50 in value and with **50%** chance decreases by $150 in value. Write a loop that simulates the price movement over 30 days and then display the final price of the car."""

price = 20000
for i in range(30):
    if random.random() > 0.5:
        price += 50
    else:
        price -= 150
print(f'The final price of the car after 30 days is {price}')

"""E15. Imagine that the price of a car starts at \$20,000 and with **25%** chance each day increases by \$50 in value and with **75%** chance decreases by $150 in value. Write a loop that simulates the price movement over 30 days and then display the final price of the car."""

price = 20000
for i in range(30):
    if random.random() > 0.75:
        price += 50
    else:
        price -= 150
print(f'The final price of the car after 30 days is {price}')

"""E16. Imagine that the price of a car starts at \$20,000 and with **15%** chance each day increases by \$50 in value, with **30%** chance stays at its current value, and with **55%** chance decreases by $150 in value. Write a loop that simulates the price movement over 30 days and then display the final price of the car."""

price = 20000
for i in range(30):
    if random.random() > 0.85:
        price += 50
    elif random.random() > 0.55:
        price += 0
    else:
        price -= 150
print(f'The final price of the car after 30 days is {price}')

"""### How to Submit Your Work

1. Go to the [course website](https://sites.google.com/stonybrook.edu/cse101sum/schedule-session-i).

1. Click the **Submit** link for this assignment.

1. Type your Net ID (Blackboard login) on the line provided.

1. Press the button marked **Add file**.

1. Click the **My Drive** tab.

1. Click on the file you wish to submit.

1. Hit **Select**.

1. Hit **Submit** to submit your file grading.
"""