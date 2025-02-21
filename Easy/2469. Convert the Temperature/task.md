# 2469. Convert the Temperature #

You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

__Note that:__

- Kelvin = Celsius + 273.15
- Fahrenheit = Celsius * 1.80 + 32.00
 

__Example 1:__

> __Input:__ celsius = 36.50
> __Output:__ [309.65000,97.70000]
> __Explanation:__ Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

__Example 2:__

> __Input:__ celsius = 122.11
> __Output:__ [395.26000,251.79800]
> __Explanation:__ Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
 

__Constraints:__

- 0 <= celsius <= 1000