// Title: 기능개발
// Level: 2
// Date: 2022.02.13

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int size = progresses.size(); // 총 작업 개수
    int idx = 0; // 확인하는 index
    int result = 0; // 한번에 배포되는 작업 개수
    while (idx < size){
        // 배포하기
        result = 0;
        
        while (progresses[idx]>=100 && idx<size){
            result += 1;
            idx += 1;
        }
        
        if (result != 0){
            answer.push_back(result);
        }
        
        // 작업 실행
        for (int i = idx; i<size; i++){
            progresses[i] += speeds[i];
        }
    }
    
    return answer;
}