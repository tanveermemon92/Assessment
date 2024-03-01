# Question 2:
# [Python] A phoneme is a sound unit (similar to a character for text). We have an extensive pronunciation dictionary (think millions of words).
# Below is a snippet:
# ABACUS BOOK THEIR THERE TOMATO TOMATO
# AE B AH K AH S B UH K
# DH EH R DH EH R
# T AH M AA T OW T AH M EY T OW
# Given a sequence of phonemes as input (e.g. ["DH", "EH", "R", "DH", "EH", "R"]), 
# find all the combinations of the words that can produce this sequence 
# (e.g. [["THEIR", "THEIR"], ["THEIR", "THERE"], ["THERE", "THEIR"], ["THERE", "THERE"]]).
# You can preprocess the dictionary into a different data structure if needed.
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

    # Iterate over the pronunciation dictionary in pairs (word, phoneme sequence)
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
        # If we reached the end of the input sequence, add the current path to the result
        if start == len(input_sequence):
            result.append(path.copy())
            return

        # Explore all possible combinations starting from the current position
        for i in range(start, len(input_sequence)):
            current_phoneme = tuple(input_sequence[start:i + 1])

            # Check if the current phoneme sequence exists in the dictionary
            if current_phoneme in phoneme_dict:
                # Try each word corresponding to the phoneme sequence
                for word in phoneme_dict[current_phoneme]:
                    path.append(word)
                    # Recursively explore the next phoneme sequence
                    backtrack(i + 1, path)
                    path.pop()  # Backtrack to try the next word

    result = []
    backtrack(0, [])
    return result

# Example:
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
