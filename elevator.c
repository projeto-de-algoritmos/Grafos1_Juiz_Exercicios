/* 
    Com o intuito de resolver esse desafio, foi utilizado o 
    algoritmo de DFS (Busca em profundidade) para calcular a
    distância dos andares.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int floor;
    struct Node* next;
} Node;

Node* createNode(int floor) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->floor = floor;
    newNode->next = NULL;
    return newNode;
}

int DFS(Node* current) {
    if (current == NULL || current->next == NULL) {
        return 0;
    }

    int distance = abs(current->floor - current->next->floor);

    int restDistance = DFS(current->next);

    return distance + restDistance;
}

int main() {
    Node* head = NULL;
    char input[100];
    char *token;

    printf("Enter a list of floors: ");
    fgets(input, sizeof(input), stdin);

    token = strtok(input, ",");
    while (token != NULL) {
        int floor = atoi(token);
        Node* newNode = createNode(floor);

        if (head == NULL) {
            head = newNode;
        } else {
            Node* current = head;
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = newNode;
        }

        token = strtok(NULL, ",");
    }

    int totalDistance = DFS(head);

    printf("Total distance traveled: %d\n", totalDistance);
    Node* current = head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }

    return 0;
}
