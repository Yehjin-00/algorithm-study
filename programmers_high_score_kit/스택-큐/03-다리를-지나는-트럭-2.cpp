// Title: 다리를 지나는 트럭
// Level: 2
// Date: 2022.02.13

#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int main() {

    int bridge_length = 2;
    int weight = 10;
    vector<int> truck_weights = {7, 4, 5, 6}; 

    int answer = 0;
    queue<int> bridge;
    queue<int> wait;
    
    for (int i=0; i<truck_weights.size(); i++){
        wait.push(truck_weights[i]);
    }
    
    for (int i=0; i<bridge_length; i++){
        bridge.push(0);
    }

    int bridge_now_weight = 0;
    int bridge_now_num = 0;
    int next_truck = 0;
    int out_truck = 0;
    
    while (wait.size()>0){   

        // 트럭 넣기
        next_truck = wait.front();
        // cout << bridge_now_weight << " " <<next_truck << " " << bridge_now_num << " " << bridge_length << "\n";
        if (bridge_now_weight+next_truck < weight && bridge_now_num+1 < bridge_length) {
            cout << "HI";
            wait.pop();
            bridge_now_weight += next_truck;
            bridge_now_num += 1;
            bridge.push(next_truck);
        }
        else {
            bridge.push(0);
        }

        // 빼기
        out_truck = bridge.front();
        if (out_truck != 0){
            bridge_now_num -= 1;
        }
        bridge_now_weight -= out_truck;
        bridge.pop();

        answer += 1;
    }
    
    cout << answer;
    return 0;
}

// int main(){
//     vector<int> vec = {7, 4, 5, 6};
//     int sol =  solution(2, 10, vec);
//     cout << sol;
// }