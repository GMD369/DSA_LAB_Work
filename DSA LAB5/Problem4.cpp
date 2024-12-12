#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
void printVec(vector<int> vec)
{
    for(int i=0;i<vec.size();i++){
        cout<<vec[i]<<" ";
    }
}

int main() {
    vector<int> vec={5,6,7,4,3,44,5,6,7,23,78,90,7,8,23,45,65};
    // Original Vector:
    cout<<"Original Vector: ";
    printVec(vec);

    // sort the vector:
    sort(vec.begin(),vec.end());
    cout<<"\n\nSorted Vector: ";
    printVec(vec);

    // Reversed Vector:
    reverse(vec.begin(),vec.end());
    cout<<"\n\nReversed Vector: ";
    printVec(vec);

    // Remove Duplicaties:
     auto last = unique(vec.begin(), vec.end());
    vec.erase(last,vec.end());
    cout<<"\n\nAfter Removing duplicates: ";
    printVec(vec);



    return 0;
}