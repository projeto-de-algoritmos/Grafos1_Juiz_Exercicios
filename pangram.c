/* 
    Com o intuito de resolver esse desafio, foi utilizado o 
    algoritmo de BFS (Busca em largura), onde crio uma lista
    encadeada e adiciono e retiro os nós a fila, para a adição
    das aresta eu usei uma matriz de adjacência e por fim
    verifico se a frase passada é um pangrama.
*/
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_CHARS 26

typedef struct Node {
    char data;
    struct Node* next;
} Node;

typedef struct Queue {
    Node* front;
    Node* rear;
} Queue;

Queue* createQueue() {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    if (queue) {
        queue->front = queue->rear = NULL;
    }
    return queue;
}

bool isEmpty(Queue* queue) {
    return (queue->front == NULL);
}

void enqueue(Queue* queue, char data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode) {
        newNode->data = data;
        newNode->next = NULL;
        if (isEmpty(queue)) {
            queue->front = queue->rear = newNode;
        } else {
            queue->rear->next = newNode;
            queue->rear = newNode;
        }
    }
}

char dequeue(Queue* queue) {
    if (!isEmpty(queue)) {
        Node* temp = queue->front;
        char data = temp->data;
        queue->front = queue->front->next;
        free(temp);
        return data;
    }
    return '\0';
}

void addEdge(int graph[MAX_CHARS][MAX_CHARS], char src, char dest) {
    graph[src - 'a'][dest - 'a'] = 1;
    graph[dest - 'a'][src - 'a'] = 1;
}

bool isPangram(char* sentence) {
    int graph[MAX_CHARS][MAX_CHARS] = {0};
    Queue* queue = createQueue();
    
    int len = strlen(sentence);
    for (int i = 0; i < len; i++) {
        char c = tolower(sentence[i]);
        if (isalpha(c)) {
            enqueue(queue, c);
        }
    }
    
    if (isEmpty(queue)) {
        free(queue);
        return false;
    }
    
    char start = dequeue(queue);
    
    while (!isEmpty(queue)) {
        char current = dequeue(queue);
        addEdge(graph, start, current);
        start = current;
    }
    
    bool visited[MAX_CHARS] = {false};
    enqueue(queue, start);
    visited[start - 'a'] = true;
    
    while (!isEmpty(queue)) {
        char current = dequeue(queue);
        for (int i = 0; i < MAX_CHARS; i++) {
            if (graph[current - 'a'][i] && !visited[i]) {
                enqueue(queue, i + 'a');
                visited[i] = true;
            }
        }
    }
    
    free(queue);
    
    for (int i = 0; i < MAX_CHARS; i++) {
        if (!visited[i]) {
            return false;
        }
    }
    
    return true;
}

int main() {
    char sentence[1000];
    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);
    
    bool result = isPangram(sentence);
    
    if (result) {
        printf("The sentence is a pangram.\n");
    } else {
        printf("The sentence is not a pangram.\n");
    }
    
    return 0;
}
