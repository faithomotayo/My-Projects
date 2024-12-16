"""
Author: Faith Omotayo
Date: 03/11/24
"""

def solution():
    # Prompt user to enter how many stations they visited
    n = int(input("Enter in how many stations you visited: "))
    
    startPoint = []  # List to store starting station numbers
    finalStop = []   # List to store destination station numbers
    maxFee = []      # List to store calculated fees

    # Get starting station numbers from user
    for i in range(n):
        stations1 = int(input(f"Enter your starting station number {i+1}: "))
        startPoint.append(stations1)

    # Get destination station numbers from user
    for i in range(n):
        stations2 = int(input(f"Enter your destination station number {i+1}: "))
        finalStop.append(stations2)

    # Calculate the fee for each journey
    for i in range(n):
        distance = abs(startPoint[i] - finalStop[i])  # Distance is the absolute difference
        fee = 1 + distance * 2  # Initial fee is 1, add the calculated fee based on distance
        maxFee.append(fee)

    # Return the start, destination, and calculated fees
    return startPoint, finalStop, maxFee


# Main execution
start, dest, limit = solution()  # Call the function and unpack the returned values

# Find the maximum fee from the limit list
finalFee = max(limit)

# Print the result
print(f"The user's max fee is: {finalFee}")
