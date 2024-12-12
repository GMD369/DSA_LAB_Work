#include <iostream>
using namespace std;

// Node Class:
class Node{
    public:
    int data;
    Node* next;
};

// Queue CLass:
class Queue{
    Node* front;
    Node* rear;
    public:
    Queue(){
        front = rear = nullptr;
    }
    void enqueue(int x);
    int dequeue();
    bool isEmpty();
    int Peek();
};

// Queue's Method:
int Queue::Peek(){
    if (isEmpty()) {
        cout << "Queue is empty" << endl;
        return -1;
    }
    else{
        return front->data;
    }
}

void Queue::enqueue(int x){
    Node* temp = new Node();
    temp->data = x;
    temp->next=nullptr;
    if(isEmpty()){
        front = rear = temp;
        cout<<temp->data<<"->";
    }
    else{
        rear->next = temp;
        rear=temp;
        cout<<temp->data<<"->";
    }

}

int Queue::dequeue()
{
    if (isEmpty()) {
        cout << "Queue is empty" << endl;
        return -1;
    }
    
    
        int value=front->data;
        Node* temp=front;
        front=front->next;
        delete temp;
        return value;
}


bool Queue::isEmpty() {
    return (front == nullptr);
}

// Main Body:
int main()
{
    Queue q;
    q.enqueue(23);
    q.enqueue(44);
    q.enqueue(20);
    q.enqueue(30);
    cout << "\nDequeued item is " << q.dequeue() << endl;

}