#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

set<string> id_list;

bool check(string a, string b) {// 불량 사용자 판별
    if (a.length() != b.length()) return false;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] != b[i] && a[i] != '*') return false;
    }
    return true;
}

int solution(vector<string> user_id, vector<string> banned_id) {
    sort(user_id.begin(), user_id.end());// 순열 함수 쓰려면 정렬해야함
    vector<string> tmp;
    do {
        tmp.clear();
        string id = "";
        for (int i = 0; i < banned_id.size(); i++) {
            if (check(banned_id[i], user_id[i])) {
                tmp.push_back(user_id[i]);
            }
        }

        if (tmp.size() == banned_id.size()) {//조건에 부함한다면
            sort(tmp.begin(), tmp.end());
            for (auto& t : tmp) {
                id += t;
            }
            id_list.insert(id);
        }

    } while (next_permutation(user_id.begin(), user_id.end()));
    
    return id_list.size();
}