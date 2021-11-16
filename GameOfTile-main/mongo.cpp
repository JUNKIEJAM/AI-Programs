#include <bits/stdc++.h>
using namespace std;
 
/* For a given array arr[],
   returns the maximum j – i such
   that arr[j] > arr[i] */
int maxIndexDiff(vector<int> &arr, int n)
{
    int maxDiff = -1;
    int i, j;
 
    for (i = 0; i < n; ++i) {
        for (j = n - 1; j > i; --j) {
            if (arr[j] > arr[i] && maxDiff < (j - i))
                maxDiff = j - i;
        }
    }
 
    return maxDiff;
}
 
int main()
{
    int n;
    cin>>n;

    vector<int> v;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        v.push_back(x);
    }
    int maxDiff = maxIndexDiff(v, n);
    cout << "\n" << maxDiff;
    return 0;
}