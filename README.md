# Question 1:
[Python] The probability of rain on a given calendar day in Vancouver is p[i], where i is the day's index. For example, p[0] is the probability of rain on January 1st, and p[10] is the probability of precipitation on January 11th. Assume the year has 365 days (i.e. p has 365 elements). What is the chance it rains more than n (e.g. 100) days in Vancouver? Write a function that accepts p (probabilities of rain on a given calendar day) and n as input arguments and returns the possibility of raining at least n days.
def prob_rain_more_than_n(p: Sequence[float], n: int) -> float: 
pass
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
def find_word_combos_with_pronunciation(phonemes: Sequence[str]) -> Sequence[Sequence[str]]:
pass
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
# Question 3:
[C] Find the n most frequent words in the TensorFlow Shakespeare dataset.
char **find_frequent_words(const char *path, int32_t n) { // implementation
}

# Answer:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

// Define a structure for a key-value pair in the hash table
typedef struct {
    char *key;
    int count;
} KeyValuePair;

// Define a structure for the hash table
typedef struct {
    KeyValuePair *table;
    int size;
} HashTable;

// Define a structure for a heap node
typedef struct {
    char *word;
    int count;
} HeapNode;

// Define a structure for the priority queue (min heap)
typedef struct {
    HeapNode *heapArray;
    int capacity;
    int size;
} PriorityQueue;

// Function to initialize the hash table
void initializeHashTable(HashTable *hashTable, int size) {
    hashTable->size = size;
    hashTable->table = (KeyValuePair *)malloc(size * sizeof(KeyValuePair));
    for (int i = 0; i < size; i++) {
        hashTable->table[i].key = NULL;
        hashTable->table[i].count = 0;
    }
}

// Function to hash a string and return an index
int hashFunction(const char *key, int tableSize) {
    int hash = 0;
    for (int i = 0; key[i] != '\0'; i++) {
        hash = (hash * 31 + key[i]) % tableSize;
    }
    return hash;
}

// Function to insert a key-value pair into the hash table
void insertIntoHashTable(HashTable *hashTable, const char *key) {
    int index = hashFunction(key, hashTable->size);

    while (hashTable->table[index].key != NULL) {
        // Collision resolution (linear probing)
        index = (index + 1) % hashTable->size;
    }

    hashTable->table[index].key = strdup(key);
    hashTable->table[index].count++;
}

// Function to initialize the priority queue (min heap)
void initializePriorityQueue(PriorityQueue *pq, int capacity) {
    pq->capacity = capacity;
    pq->size = 0;
    pq->heapArray = (HeapNode *)malloc(capacity * sizeof(HeapNode));
}

// Function to swap two heap nodes
void swapHeapNodes(HeapNode *a, HeapNode *b) {
    HeapNode temp = *a;
    *a = *b;
    *b = temp;
}

// Function to heapify a subtree rooted at index i
void minHeapify(PriorityQueue *pq, int i) {
    int smallest = i;
    int leftChild = 2 * i + 1;
    int rightChild = 2 * i + 2;

    if (leftChild < pq->size && pq->heapArray[leftChild].count < pq->heapArray[smallest].count) {
        smallest = leftChild;
    }

    if (rightChild < pq->size && pq->heapArray[rightChild].count < pq->heapArray[smallest].count) {
        smallest = rightChild;
    }

    if (smallest != i) {
        swapHeapNodes(&pq->heapArray[i], &pq->heapArray[smallest]);
        minHeapify(pq, smallest);
    }
}

// Function to extract the minimum element from the priority queue
HeapNode extractMin(PriorityQueue *pq) {
    HeapNode minNode = pq->heapArray[0];
    pq->heapArray[0] = pq->heapArray[pq->size - 1];
    pq->size--;
    minHeapify(pq, 0);
    return minNode;
}

// Function to insert a new element into the priority queue
void insertIntoPriorityQueue(PriorityQueue *pq, const char *word, int count) {
    if (pq->size == pq->capacity) {
        // Priority queue is full, compare with the minimum element
        if (count > pq->heapArray[0].count) {
            pq->heapArray[0].count = count;
            pq->heapArray[0].word = strdup(word);
            minHeapify(pq, 0);
        }
    } else {
        // Priority queue is not full, insert a new element
        int i = pq->size;
        pq->size++;
        pq->heapArray[i].count = count;
        pq->heapArray[i].word = strdup(word);

        // Fix the min heap property
        while (i > 0 && pq->heapArray[(i - 1) / 2].count > pq->heapArray[i].count) {
            swapHeapNodes(&pq->heapArray[i], &pq->heapArray[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }
}

// Function to find the n most frequent words in the dataset
char **find_frequent_words(const char *path, int32_t n) {
    // Assuming path contains the file path to the TensorFlow Shakespeare dataset

    FILE *file = fopen(path, "r");
    if (!file) {
        perror("Error opening file");
        return NULL;
    }

    // Initialize hash table and priority queue
    HashTable hashTable;
    initializeHashTable(&hashTable, 10007);  // Choose a suitable prime number as the table size
    PriorityQueue pq;
    initializePriorityQueue(&pq, n);

    char buffer[256];
    while (fscanf(file, "%s", buffer) == 1) {
        // Convert the word to lowercase (assuming case-insensitive counting)
        for (int i = 0; buffer[i]; i++) {
            buffer[i] = tolower(buffer[i]);
        }

        // Insert the word into the hash table
        insertIntoHashTable(&hashTable, buffer);
    }

    // Insert the elements from the hash table into the priority queue
    for (int i = 0; i < hashTable.size; i++) {
        if (hashTable.table[i].key != NULL) {
            insertIntoPriorityQueue(&pq, hashTable.table[i].key, hashTable.table[i].count);
        }
    }

    // Create an array to store the result
    char **result = (char **)malloc(n * sizeof(char *));
    for (int i = n - 1; i >= 0; i--) {
        HeapNode minNode = extractMin(&pq);
        result[i] = minNode.word;
    }

    // Clean up memory
    for (int i = 0; i < hashTable.size; i++) {
        free(hashTable.table[i].key);
    }
    free(hashTable.table);

    for (int i = 0; i < n; i++) {
        free(pq.heapArray[i].word);
    }
    free(pq.heapArray);

    fclose(file);

    return result;
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
