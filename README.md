# Question 1:
[Python] The probability of rain on a given calendar day in Vancouver is p[i], where i is the day's index. For example, p[0] is the probability of rain on January 1st, and p[10] is the probability of precipitation on January 11th. Assume the year has 365 days (i.e. p has 365 elements). What is the chance it rains more than n (e.g. 100) days in Vancouver? Write a function that accepts p (probabilities of rain on a given calendar day) and n as input arguments and returns the possibility of raining at least n days.
def prob_rain_more_than_n(p: Sequence[float], n: int) -> float: 
pass

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

# Example usage:
if __name__ == "__main__":
    # Replace with actual probabilities for each day, e.g., based on historical data
    probabilities = [0.3] * 365  # For simplicity, assuming a constant probability
    threshold_days = 100

    # Calculate the probability of raining more than the specified threshold
    result = prob_rain_more_than_n(probabilities, threshold_days)

    # Display the result
    print(f"The probability of raining more than {threshold_days} days is: {result}")

# Question 2:
[Python] A phoneme is a sound unit (similar to a character for text). We have an extensive pronunciation dictionary (think millions of words). Below is a snippet:
ABACUS BOOK THEIR THERE TOMATO TOMATO
AE B AH K AH S B UH K
DH EH R DH EH R
T AH M AA T OW T AH M EY T OW
Given a sequence of phonemes as input (e.g. ["DH", "EH", "R", "DH", "EH", "R"]), find all the combinations of the words that can produce this sequence (e.g. [["THEIR", "THEIR"], ["THEIR", "THERE"], ["THERE", "THEIR"], ["THERE", "THERE"]]). You can preprocess the dictionary into a different data structure if needed.
def find_word_combos_with_pronunciation(phonemes: Sequence[str]) -> Sequence[Sequence[str]]: pass

# Answer:
from collections import defaultdict

def preprocess_dictionary(pronunciation_dict):
    """
    Preprocess the pronunciation dictionary into a data structure for efficient lookup.

    Parameters:
    - pronunciation_dict: List of words with their corresponding phoneme sequences.

    Returns:
    - dict: A dictionary with phoneme sequences as keys and lists of words as values.
    """
    phoneme_dict = defaultdict(list)
    for i in range(0, len(pronunciation_dict), 2):
        word = pronunciation_dict[i]
        phoneme_sequence = tuple(pronunciation_dict[i + 1])
        phoneme_dict[phoneme_sequence].append(word)
    return phoneme_dict

def find_word_combinations(phoneme_dict, input_sequence):
    """
    Find all combinations of words that can produce the given phoneme sequence.

    Parameters:
    - phoneme_dict: Preprocessed dictionary of phoneme sequences and corresponding words.
    - input_sequence: List of phonemes to find combinations for.

    Returns:
    - list: List of word combinations that can produce the input phoneme sequence.
    """
    def backtrack(start, path):
        if start == len(input_sequence):
            result.append(path.copy())
            return
        for i in range(start, len(input_sequence)):
            current_phoneme = tuple(input_sequence[start:i + 1])
            if current_phoneme in phoneme_dict:
                for word in phoneme_dict[current_phoneme]:
                    path.append(word)
                    backtrack(i + 1, path)
                    path.pop()

    result = []
    backtrack(0, [])
    return result

# Example usage:
if __name__ == "__main__":
    # Given pronunciation dictionary
    pronunciation_dict = ["ABACUS", ["AE", "B", "AH", "K", "AH", "S"],
                          "BOOK", ["B", "UH", "K"],
                          "THEIR", ["DH", "EH", "R"],
                          "THERE", ["DH", "EH", "R"],
                          "TOMATO", ["T", "AH", "M", "AA", "T", "OW"],
                          "TOMATO", ["T", "AH", "M", "EY", "T", "OW"]]

    # Preprocess the dictionary into a suitable data structure
    phoneme_dict = preprocess_dictionary(pronunciation_dict)

    # Example input phoneme sequence
    input_sequence = ["DH", "EH", "R", "DH", "EH", "R"]

    # Find word combinations that can produce the input phoneme sequence
    result = find_word_combinations(phoneme_dict, input_sequence)

    # Display the result
    print("All combinations of words that can produce the given phoneme sequence:")
    for combination in result:
        print(combination)

    # Display the result
    print("All combinations of words that can produce the given phoneme sequence:")
    for combination in result:
        print(combination)
