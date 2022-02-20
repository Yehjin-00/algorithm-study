// Title: K번째수
// Level: 1
// Date: 2022.02.20

#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for (int i=0; i<commands.size(); i++){
        priority_queue<int> pq;
        vector<int> com = commands[i];
        for (int j=com[0]-1; j<com[1]; j++){
            pq.push(-array[j]);
        }
        
        int ans;
        for (int j=0; j<com[2]; j++){
            ans = pq.top();
            pq.pop();
        }
        answer.push_back(-ans);
    }
    
    return answer;
}