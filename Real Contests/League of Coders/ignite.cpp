#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--)
    {
        int n,q;
        cin>>n>>q;
        vector<long long> capacity(n);
        map<long long ,long long > mymap;
        for (int i=0;i<n;i++)
        {
            cin>>capacity[i];
            mymap[capacity[i]]=0;
        }
        while(q--)
        {
            int c;
            cin>>c;
            if (c==1)
            {
                long long x,y;
                cin>>x>>y;
                while(x>0)
                {
                    if(mymap[capacity[y-1]]==capacity[y-1])
                    {
                        y++;
                    }
                    else if (x>capacity[y-1])
                    {
                        mymap[capacity[y-1]]=capacity[y-1];
                        x-=capacity[y-1]-mymap[capacity[y-1]];
                        y++;

                    }
                    else{
                        mymap[capacity[y-1]]+=x;
                    }
                }
            }
            if (c==2)
            {
                int p;
                cin>>p;
                cout<<mymap[capacity[p-1]]<<endl;
            }
        }


    }





}