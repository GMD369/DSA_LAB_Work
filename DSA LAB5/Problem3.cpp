#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};  
    int searchValue;
    
    cout << "Enter an integer to search for: ";
    cin >> searchValue;
    
    bool found = false;
    for (int i = 0; i < vec.size(); ++i) {
        if (vec[i] == searchValue) {
            cout << "Integer " << searchValue << " found at index " << i << "." << endl;
            found = true;
            break;
        }
    }
    if (!found) {
        cout << "Integer " << searchValue << " is not present in the vector." << endl;
    }
    return 0;
}
