# Question 3:[C] Find the n most frequent words in the TensorFlow Shakespeare dataset.
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
# Example: 
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
