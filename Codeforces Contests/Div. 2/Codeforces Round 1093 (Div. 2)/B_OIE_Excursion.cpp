#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    long long m;
    cin >> n >> m;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int max_run = 1;
    int current_run = 1;
    
    // Find the longest contiguous subarray of identical elements
    for (int i = 1; i < n; i++) {
        if (a[i] == a[i - 1]) {
            current_run++;
        } else {
            current_run = 1;
        }
        max_run = max(max_run, current_run);
    }
    
    // If the maximum run of identical elements is >= m, he gets caught
    if (max_run >= m) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
    }
}

int main() {
    // Optimize standard I/O operations for performance
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    
    return 0;
}