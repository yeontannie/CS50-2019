// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 1985

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

unsigned long hash(char *str);

// Represents a hash table
node *hashtable[N];
int counter = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int lenth = strlen(word);
    char aray[lenth + 1];
    aray[lenth] = '\0';

    for(int i = 0; i < lenth; i++)
    {
        aray[i] = tolower(word[i]);
    }

    int index = hash(aray) % N;

    node *head = hashtable[index];

    if(head != NULL)
    {
        node *cursor = head;

        while(cursor != NULL)
        {
            if(strcmp(aray, cursor->word) == 0)
            {
                return true;
            }

            cursor = cursor->next;
        }
    }

    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char buffer[LENGTH + 1];
    int n = LENGTH + 2;

    // Insert words into hash table
    while (fgets(buffer, n, file) != NULL)
    {
        buffer[strlen(buffer) - 1] = '\0';
        int index = hash(buffer) % N;
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return false;
        }

        strcpy(new_node->word, buffer);
        new_node->next = hashtable[index];
        hashtable[index] = new_node;
        counter++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for(int i = 0; i < N; i++)
    {
        node *cursor = hashtable[i];

        while(cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }

    return true;
}

unsigned long hash(char *str)
{
    unsigned long hash = 5381;
    int j;

    while((j = *str++))
    {
        hash = ((hash << 5) + hash) + j;
    }

    return hash;
}
