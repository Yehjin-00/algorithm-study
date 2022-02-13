// Title: 프린터
// Level: 2
// Date: 2022.02.13

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    // initialize
    priority_queue<int> pq;
    queue<vector<int>> q;
    
    for (int i=0; i<priorities.size(); i++){
        vector<int> temp = {i, priorities[i]};
        q.push(temp);
        pq.push(priorities[i]);
    }
    
    // use 1 queue and 1 prioritiy queue
    while (true) {
        vector<int> front = q.front();
        if (front[1] == pq.top()){
            pq.pop();
            q.pop();
            answer += 1;
            if (front[0] == location){
                return answer;
            }
        }
        else {
            q.pop();
            q.push(front);
        }
    }
    
    return 0;
}