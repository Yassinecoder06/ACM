#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    long long n;
    cin >> n; // Read the size of the sequence
    
    // Calculate the sum of the first n natural numbers
    long long s = n * (n + 1) / 2;

    // Subtract the entered numbers from the sum
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        s -= x;
    }

    // The remaining value in s is the missing number
    cout << s << endl;

    return 0;
}

