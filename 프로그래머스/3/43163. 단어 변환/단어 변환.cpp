#include <string>
#include <vector>
#include <queue>

using namespace std;
int count_diff(string previous, string later){
    int count = 0;
    for(int i=0; i<previous.size(); i++){
        if(previous[i] != later[i]){
            count += 1;
        }
    }
    return count;
}
int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    queue<pair<string,int>>q;
    q.push({begin, answer});
    while(!q.empty()){
        auto [previous, answer] = q.front();
        q.pop();
        if(previous == target) return answer;
        for(int i=0; i<words.size(); i++){
            if(count_diff(previous, words[i]) == 1){
                q.push({words[i], answer+1});
            }
        } 
        answer = 0;
    }
    
    return answer;
}