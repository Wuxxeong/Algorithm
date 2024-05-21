#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = 0;
    sort(dungeons.begin(), dungeons.end());

    do{
        int cnt = 0;
        int tmp = k;
        for(int i=0; i<dungeons.size(); i++){
            if(dungeons[i][0] <= tmp){
                cnt += 1;
                tmp -= dungeons[i][1];
            }
        }
        answer = max(answer, cnt);
    }
    while(next_permutation(dungeons.begin(), dungeons.end()));
    
    return answer;
}