#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec;
    
    for (int i = 0; i < 100; ++i) {
        vec.push_back(i);  // Insert integer i
        cout << "Inserting: " << i << " | Size: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
    }

    return 0;
}