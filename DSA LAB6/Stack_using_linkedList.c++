#include <iostream>
using namespace std;

// Node Class:
class Node{
    public:
    int data;
    Node* next;
};

// Stack Class:
class Stack{
    Node* Top;
    public:
    Stack(){
        Top = nullptr;
    }
    void push(int x);
    int pop();
    int peek();
    bool isEmpty();
};

// Stack's Method:
void Stack::push(int x){
    Node* newNode = new Node(); 
    newNode->data=x;
    newNode->next = Top;
    Top = newNode;
    cout<<newNode->data<<"->";
}

bool Stack::isEmpty(){
    return Top == nullptr;
}

int Stack::peek(){
    if (isEmpty()) {
        cout << "Stack is empty" << endl;
        return -1;
    }
    else{
        return Top->data;
    }
}

int Stack::pop()
{
    if (isEmpty())
    {
        cout << "Stack is empty" << endl;
        return -1;
    }
    else{
        int popped = Top->data;
        Node* temp = Top;
        Top=Top->next;
        delete temp;
        return popped;
    }
}
int main()
{
    Stack s;
    s.push(1);
    s.push(2);
    s.push(4);
    cout <<"\n"<< s.pop() << endl;

}