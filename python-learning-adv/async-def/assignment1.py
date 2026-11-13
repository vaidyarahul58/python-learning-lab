# Perform tree different task using async/await method
# Task 1 : Calculate sum of n integers
# Task 2 : Find out factorial of givn numbers
# Task 3 : Calculate area of Circle

import asyncio
import math


class Calculate:
    def __init__(self, num1, num2, redi):
        self.num1 = num1
        self.num2 = num2
        self.redi = redi

    async def calc(self):
        return sum(range(1, self.num1 + 1))

    async def get_factorial_math(self):
        if self.num2 < 0:
            return "Factorial is not defined for negative numbers."
        return math.factorial(self.num2)

    async def circle(self):
        return math.pi * self.redi * self.redi

async def main():
    num1 = int(input("Enter the number to calculate sum: "))
    num2 = int(input("Enter the number to calculate factorial: "))
    redi = float(input("Enter the radius of the circle: "))
    owner = Calculate(num1, num2, redi)
    total, factorial, area = await asyncio.gather(
        owner.calc(),
        owner.get_factorial_math(),
        owner.circle(),
    )

    print(f"The sum is {total}")
    print(f"The factorial is {factorial}")
    print(f"The area of the circle is {area}")

asyncio.run(main())