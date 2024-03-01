# Question 1:
[Python] The probability of rain on a given calendar day in Vancouver is p[i], where i is the day's index. For example, p[0] is the probability of rain on January 1st, and p[10] is the probability of precipitation on January 11th. Assume the year has 365 days (i.e. p has 365 elements). What is the chance it rains more than n (e.g. 100) days in Vancouver? Write a function that accepts p (probabilities of rain on a given calendar day) and n as input arguments and returns the possibility of raining at least n days.
# Answer:
def prob_rain_more_than_n(p, n):
    """
    Calculate the probability of raining more than n days in a year.

    Parameters:
    - p: List of floats, probabilities of rain on each calendar day.
    - n: Integer, the threshold for the number of days.

    Returns:
    - float: Probability of raining more than n days in a year.
    """
    # Calculate the probability using the binomial distribution manually
    # P(X > n) = 1 - P(X <= n-1)
    probability = 1 - sum(p[:n])  # Assuming p contains probabilities for each day
    return probability

# Example:
if __name__ == "__main__":
    # Replace with actual probabilities for each day, e.g., based on historical data
    probabilities = [0.3] * 365  # For simplicity, assuming a constant probability
    threshold_days = 100

    # Calculate the probability of raining more than the specified threshold
    result = prob_rain_more_than_n(probabilities, threshold_days)

    # Display the result
    print(f"The probability of raining more than {threshold_days} days is: {result}")
