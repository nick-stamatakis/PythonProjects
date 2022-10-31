# -*- coding: utf-8 -*-
"""Nicholas Stamatakis CSE 101 Lab Exercises Set #2: Functions

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JdtSFRWAJJVVqWXblB3v_vLqnA8rJu-c

#CSE 101: Computer Science Principles

#### Stony Brook University, Summer 2021, Session I Extended

### Lab Exercises Set #2

#### Due: Sunday, June 6, 2021 at 11:59 pm EDT

### Learning Outcomes
By the end of these exercises you should be able to:
* Write and call simple functions in Python.

### Functions

For this set of exercises you will write a function and then call it to verify its correctness. An example of this process is given below.

*(Simulated exercise)* The [centripetal force](https://www.youtube.com/watch?v=KvCezk9DJfk&ab_channel=PlanetNutshell) is the force which keeps an object moving along the axis of rotation of a curved path. The force is computed as $F=\dfrac{mv^2}{r}$ where:
* $F$ = the centripetal force in Newtons
* $m$ = mass in kilograms
* $v$ = velocity in meters per second
* $r$ = radius in meters

Complete the function `centripetal_force(mass, velocity, radius)`, which computes and returns the centripal force (in Newtons) of a body with a mass of `mass` kilograms, velocity of `velocity` meters per second, and radius of `radius` meters. For example, for the arguments `0.15, 30, 1.5` your function should return `90.0`.

*You would be provided a cell with the following contents:*
"""

def centripetal_force(mass, velocity, radius):

"""*(Simulated exercise) You would then complete the function by typing some code into the cell immediately above this one. The final result would look like the following:*"""

def centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

"""*(Simulated exercise)* Call your function with the arguments `0.15, 30, 1.5` and display the return value to verify its correctness.

*A blank cell would be provided below this one, in which you would fill with the code shown below, and then you would execute the cell.*
"""

centripetal_force(0.15, 30, 1.5)

"""Now you should be able to complete the exercises given below. If you have any trouble with them, be sure to ask a TA for help or make a post in the online Q&A discussion boards.

E1. The formula for converting a Fahrenheit temperature to Celsius is $T_C = (T_F - 32) \times \frac{5}{9}$. Complete the definition of the function `convert(temp_f)` that computes and returns the Celsius equivalent of the Fahrenheit temperature given as `temp_f`.
"""

def convert(temp_f):
    return (temp_f-32) * (5/9)

"""E2. Call your function and display the returned values for the following Fahrenheit temperatures:
* 32°
* 212°
* -40°
"""

convert(32)

convert(212)

convert(-40)

"""E3. The formula for simple interest is $Prt$, where:
* $P$ is the principal
* $r$ is the annual interest rate, as a decimal
* $t$ is the time period involved

Complete the definition of the function `def new_balance(principal, rate, years)` that computes the total amount of money in a bank account after `years` years, assuming we started with $`principal` and the interest rate (as a decimal) is `rate`. Note that we don't simply want the interest earned, but rather the interest earned *plus* the starting principal. For example, for the arguments `1000, 0.05, 3` your function should return `1150.0`.

"""

def new_balance(principal, rate, years):
    return principal + principal * rate * years

"""E4. Call your function with the arguments `1000, 0.05, 3` and display the return value to verify its correctness."""

new_balance(1000, 0.05, 3)

"""E5. Recall from lecture that one way of modeling population growth in the field of ecology is the logistic growth model, which uses this equation: $P_{n+1} = P_n + r P_n\left(1 - \frac{P_n}{M}\right)$, where:
* $P_{n+1}$ is the population of the next generation
* $P_n$ is the population of the current generation
* $r$ is the rate of population growth, given as a decimal
* $M$ is the carrying capacity (maximum population size)

Complete the definition of the function `def next_population(current_pop, growth_rate, carrying_capacity)` that computes the population of the next generation of organisms, assuming we currently have `current_pop` individuals, a growth rate of `growth_rate` and a carrying capacity of `carrying_capacity`. For example, for the arguments `5000, 0.03, 4000` your function should return `4962.5`.
"""

def next_population(current_pop, growth_rate, carrying_capacity):
    return current_pop + growth_rate * current_pop * (1-(current_pop/carrying_capacity))

"""E6. Call your function with the arguments `5000, 0.03, 4000` and display the return value to verify its correctness. """

next_population(5000, 0.03, 4000)

"""E7. As its name suggests, the Du Bois [body surface area (BSA)](https://en.wikipedia.org/wiki/Body_surface_area) formula calculates the approximate surface area in square meters of a person's body, given that individual's mass in kilograms and height in centimeters. The formula is $BSA = 0.007184 \times W^{0.425} \times H^{0.725}$ where:
* $BSA$ = computed body surface area
* $W$ = mass in kilograms
* $H$ = height in centimeters

Complete the definition of the function `def bsa(mass, height)` that computes the body surface area in square meters of a person whose mass is `mass` kilograms and whose height is `height` *meters*. (Note that you have to convert the value of `height` from meters to centimeters *inside the function*.) For example, for the arguments `75, 1.78` your function should return approximately `1.93`.
"""

def bsa(mass, height):
    return 0.007184 * mass**0.425 * ((height*100)**0.725)

"""E8. Call your function with the arguments `75, 1.78` and display the return value to verify its correctness. """

bsa(75, 1.78)

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