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

# Question 2:
[Python] A phoneme is a sound unit (similar to a character for text). We have an extensive pronunciation dictionary (think millions of words). Below is a snippet:
ABACUS BOOK THEIR THERE TOMATO TOMATO
AE B AH K AH S B UH K
DH EH R DH EH R
T AH M AA T OW T AH M EY T OW
Given a sequence of phonemes as input (e.g. ["DH", "EH", "R", "DH", "EH", "R"]), find all the combinations of the words that can produce this sequence (e.g. [["THEIR", "THEIR"], ["THEIR", "THERE"], ["THERE", "THEIR"], ["THERE", "THERE"]]). You can preprocess the dictionary into a different data structure if needed.
# Answer:
    from collections import defaultdict

    def preprocess_dictionary(pronunciation_dict):

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
# Question 3:
[C] Find the n most frequent words in the TensorFlow Shakespeare dataset.
# Answer:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAX_WORD_LENGTH 50
#define INITIAL_CAPACITY 100

// Structure to hold a word-frequency pair
typedef struct {
    char word[MAX_WORD_LENGTH];
    int frequency;
} WordFrequency;

// Function to compare two word-frequency pairs for sorting
int compare(const void *a, const void *b) {
    return ((WordFrequency *)b)->frequency - ((WordFrequency *)a)->frequency;
}

char **find_frequent_words(const char *path, int32_t n) {
    FILE *file = fopen(path, "r");
    if (file == NULL) {
        fprintf(stderr, "Error opening file\n");
        return NULL;
    }

    // Initialize dynamic array to store word-frequency pairs
    WordFrequency *wordFreq = (WordFrequency *)malloc(INITIAL_CAPACITY * sizeof(WordFrequency));
    if (wordFreq == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        fclose(file);
        return NULL;
    }

    int capacity = INITIAL_CAPACITY;
    int size = 0;

    // Read words from file and count their frequencies
    char word[MAX_WORD_LENGTH];
    while (fscanf(file, "%s", word) == 1) {
        // Check if word already exists
        int found = 0;
        for (int i = 0; i < size; i++) {
            if (strcmp(word, wordFreq[i].word) == 0) {
                wordFreq[i].frequency++;
                found = 1;
                break;
            }
        }
        // If word is not found, add it to the list
        if (!found) {
            if (size == capacity) {
                capacity *= 2;
                wordFreq = (WordFrequency *)realloc(wordFreq, capacity * sizeof(WordFrequency));
                if (wordFreq == NULL) {
                    fprintf(stderr, "Memory reallocation failed\n");
                    fclose(file);
                    return NULL;
                }
            }
            strcpy(wordFreq[size].word, word);
            wordFreq[size].frequency = 1;
            size++;
        }
    }

    fclose(file);

    // Sort the word-frequency pairs
    qsort(wordFreq, size, sizeof(WordFrequency), compare);

    // Extract top n frequent words
    char **result = (char **)malloc((n + 1) * sizeof(char *));
    if (result == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        free(wordFreq);
        return NULL;
    }

    for (int i = 0; i < n && i < size; i++) {
        result[i] = strdup(wordFreq[i].word);
        if (result[i] == NULL) {
            fprintf(stderr, "Memory allocation failed\n");
            for (int j = 0; j < i; j++)
                free(result[j]);
            free(result);
            free(wordFreq);
            return NULL;
        }
    }
    result[n] = NULL; // Terminate the array with NULL
    free(wordFreq);
    return result;
}
int main() {
    char **frequentWords = find_frequent_words("shakespeare.txt", 10);
    if (frequentWords != NULL) {
        printf("Top 10 frequent words:\n");
        for (int i = 0; frequentWords[i] != NULL; i++) {
            printf("%s\n", frequentWords[i]);
            free(frequentWords[i]);
        }
        free(frequentWords);
    }
    return 0;
}
# Example:
int main() {
    char **frequentWords = find_frequent_words("path/to/tf_shakespeare_dataset.txt", 5);
    if (frequentWords) {
        printf("The 5 most frequent words are:\n");
        for (int i = 0; i < 5; i++) {
            printf("%s\n", frequentWords[i]);
            free(frequentWords[i]);
        }
        free(frequentWords);
    }

    return 0;
}

# Question 4:
[Python] Implement CTC as described in this paper. Your implementation should support both forward and backward propagation operations.
# Answer: 
import numpy as np
from mindspore import nn, context

# Define the CTC forward-backward algorithm
class CTCForwardBackward(nn.Cell):
    def __init__(self, config):
        super(CTCForwardBackward, self).__init__()
        self.config = config
        self.net = CTCModel(input_size=config.feature_dim, batch_size=config.batch_size,
                            hidden_size=config.hidden_size, num_class=config.n_class, num_layers=config.n_layer)
        self.loss_fn = CTC_Loss(batch_size=config.batch_size, max_label_length=config.max_label_length)
        self.loss_net = WithCtcLossCell(self.net, self.loss_fn)

    def construct(self, log_probs, labels):
        T, V = log_probs.shape  # T: number of time steps, V: number of classes (including blank)
        L = len(labels) * 2 + 1  # Length of modified label sequence

        # Initialize forward variables
        alpha = np.zeros((T, L))
        alpha[0, 0] = log_probs[0, 0]  # Initialize with the first symbol of the first label

        # Initialize forward variables for modified label sequence
        alpha_bar = np.zeros((T, L))
        alpha_bar[0, 1] = log_probs[0, labels[0]]  # Initialize with the first symbol of the first label

        # Forward recursion
        for t in range(1, T):
            for s in range(L):
                alpha[t, s] = alpha[t - 1, s] + alpha_bar[t - 1, s]
                if s > 0:
                    alpha[t, s] += alpha_bar[t - 1, s - 1]
                if s < L - 1:
                    alpha_bar[t, s] = log_probs[t, labels[s // 2]] if labels[s // 2] == s // 2 else 0
                    alpha_bar[t, s] += alpha[t, s]

        # Initialize backward variables
        beta = np.zeros((T, L))
        beta[T - 1, L - 1] = log_probs[T - 1, 0]  # Initialize with the first symbol of the last label

        # Initialize backward variables for modified label sequence
        beta_bar = np.zeros((T, L))
        beta_bar[T - 1, L - 2] = log_probs[T - 1, labels[-1]]  # Initialize with the last symbol of the last label

        # Backward recursion
        for t in range(T - 2, -1, -1):
            for s in range(L - 1, -1, -1):
                beta[t, s] = beta[t + 1, s] + beta_bar[t + 1, s]
                if s < L - 1:
                    beta[t, s] += beta_bar[t + 1, s + 1]
                if s > 0:
                    beta_bar[t, s] = log_probs[t, labels[(s - 1) // 2]] if labels[(s - 1) // 2] == (s - 1) // 2 else 0
                    beta_bar[t, s] += beta[t, s]

        # Compute conditional probabilities p(l|x)
        conditional_probs = np.exp(alpha + beta - log_probs.sum(axis=1)[:, np.newaxis])

        return conditional_probs


# Example usage
config = {}  # Define your configuration
log_probs = np.random.rand(10, 4)  # Example log probabilities (time steps, num_classes)
labels = [1, 2, 1]  # Example label sequence

# Initialize MindSpore context
context.set_context(mode=context.GRAPH_MODE)

# Create CTC forward-backward algorithm
ctc_forward_backward = CTCForwardBackward(config)

# Perform forward-backward propagation
conditional_probs = ctc_forward_backward(log_probs, labels)
print("Conditional probabilities:", conditional_probs)
