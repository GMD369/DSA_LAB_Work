# include<iostream>
#include<conio.h>
# include<vector>
# include<string>
using namespace std;
void display(vector<string> strs)
{
    cout<<"current strings in the vector\n";
    for(int i=0; i<strs.size();i++)
    {
        cout<<strs[i]+" ";
    }
     cout << "\nSize: " << strs.size() << ", Capacity: " << strs.capacity() << endl;
}
main()
{
    vector<string> strs;
    int choice;
    while(true){
        cout << "Menu:\n";
        cout << "1. Add string\n";
        cout << "2. Remove string\n";
        cout << "3. Display vector size and capacity\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        if(choice==1)
        {
            string newstr;
            cout << "Enter a string: ";
            cin >> newstr;
            strs.push_back(newstr);
            display(strs);
            getch();
        }
        if(choice==2)
        {
            if(!strs.empty())
            {
                 strs.pop_back();
                 display(strs);
                 getch();
            }
            else{
                cout<<"vector is empty\n";
                  getch();
            }
           
        }
        if(choice==3)
        {
            if(!strs.empty())
            {
                 display(strs);
                 getch();
            }
            else{
                cout<<"vector is empty\n";
                  getch();
            }
            
        }
        if(choice==4){
            break;
        }
    }
}
