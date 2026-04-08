#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        deque<long long > strength;
        for (int i=0;i<n;i++)
        {
            long long x;
            cin>>x;
            strength.push_back(x);
        }
        
        vector<long long> team;
        if (strength[n-1]>strength[0])
        {
            team.push_back(strength[0]);
            strength.pop_front();
            
        }
        else{
            team.push_back(strength[n-1]);
            strength.pop_back();
            

        }


        while(strength.size()!=0 )
        {
            if (strength[strength.size()-1]< team.back() && strength[0]< team.back())
            {
                if(strength.size()==1)
                {
                   strength.pop_back(); 
                   break;
                }
                else{
                strength.pop_back();
                strength.pop_front();}
            }
            else if(strength[0]<strength[strength.size()-1])
            {
                if (strength[0]>= team.back())
                {team.push_back(strength[0]);
                strength.pop_front();}
                else if (strength[strength.size()-1]>=team.back())
                {team.push_back(strength[strength.size()-1]);
                strength.pop_back();}
                
            }
            else if (strength[0]>=strength[strength.size()-1] )
            {
                if (strength[strength.size()-1]>=team.back())
                {team.push_back(strength[strength.size()-1]);
                strength.pop_back();}
                else if (strength[0]>=team.back())
                {team.push_back(strength[0]);
                strength.pop_front();}
            }
            

        }
        cout << team.size()<<endl;
        for (int i=0;i<team.size();i++)
        {
            cout<<team[i]<<" ";
        }
        cout<<"\n";
    }   
    
    
}