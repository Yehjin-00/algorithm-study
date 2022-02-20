// Title: 주식가격
// Level: 2
// Date: 2022.02.20

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    
    for (int i=0; i<prices.size(); i++){
        int ans = 0;
        for (int j=i+1; j<prices.size(); j++){
            if (prices[i] > prices[j]){
                ans += 1;
                break;
            }
            else{
                ans += 1;
            }
        }
        answer.push_back(ans);
    }
    
    return answer;
}