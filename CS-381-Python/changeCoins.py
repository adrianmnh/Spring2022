"""Write a program to provide change in coins.
Input
Have your program ask the user to input some amount of money.
Output
Your program should output the minimum number of coins required to render the amount entered into
coins. The coins are half-dollars, quarters, dimes, nickels and pennies.
Your program should also list how many of each coin needs to be provided. Each denomination on its
own line, starting with half-dollars."""


coins = float(input("How much you got?\n"))*100
print("You need",int(coins/50),"half dollars")
coins = coins%50
print("You need",int(coins//25),"quarters")
coins = coins%25
print("You need",int(coins//10),"dimes")
coins = coins%10
print("You need",int(coins//5),"nicks")
coins = coins%5
print("You need",int(coins//1),"pennies")


