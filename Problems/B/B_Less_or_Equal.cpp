#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    vector<long long>arr(n);
    for (int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    if (k==0) cout<<"-1"<<endl;
    else if (k==n)
    {
        cout<<arr[k-1]+1<<endl;
    }
    else{
    sort(arr.begin(),arr.end());
    if(arr[k]==arr[k-1] || arr[k]==arr[k+1]) cout<<"-1"<<endl;
    else{
        cout<<arr[k-1]+1<<endl;
    }}
    /*int idx=lower_bound(arr.begin(),arr.end(),k)-arr.begin();
    if (idx<k) cout<<"-1"<<endl;
    else{
    cout<<arr[idx-1]+1<<endl;}*/

}