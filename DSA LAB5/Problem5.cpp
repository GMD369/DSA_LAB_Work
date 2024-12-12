#include <iostream>
#include <vector>

using namespace std;
void printMatrix(vector<vector<int>> Matrix)
{
    for(int i=0;i<Matrix.size();i++)
    {
        for(int j=0;j<Matrix[i].size();j++)
        {
            cout<<Matrix[i][j]<<" ";
        }
        cout<<endl;
    }
}
void AddRow(vector<vector<int>>& Matrix, const vector<int>& Row)
{
    Matrix.push_back(Row);
}
void AddCol(vector<vector<int>>& Matrix, const vector<int>& Col){

    if(Matrix.empty() || Matrix.size() != Col.size()){
        cout<<"Error: Matrix is empty or column size does not match"<<endl;
    }
    else{
        for(int i=0;i<Matrix.size();i++){
        Matrix[i].push_back(Col[i]);
    }
    }
    
}
vector<vector<int>> transposeMatrix(vector<vector<int>>matrix) {
    if (matrix.empty()) return {};

    vector<vector<int>> transposed(matrix[0].size(), vector<int>(matrix.size()));

    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[0].size(); ++j) {
            transposed[j][i] = matrix[i][j];
        }
    }
    return transposed;
}

int main() {
    vector<vector<int>> Matrix={{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    // Original Matrix:
    cout << "Original Matrix:" << endl;
    printMatrix(Matrix);

    // Add a new row:
    vector<int> row={10, 11, 12};
    AddRow(Matrix, row);
    cout << "After add new row Matrix:" << endl;
    printMatrix(Matrix);

    // Add a column:
    vector<int> col={13, 14, 15,34};
    AddCol(Matrix,col);
    cout << "After add new column Matrix:" << endl;
    printMatrix(Matrix);

    // Transpose a Matrix:
    vector<vector<int>> TransposeMatrix= transposeMatrix(Matrix);
    cout << "Transposed Matrix:" << endl;
    printMatrix(TransposeMatrix);

    return 0;
}