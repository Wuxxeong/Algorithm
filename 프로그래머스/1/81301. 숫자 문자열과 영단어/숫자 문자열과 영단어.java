class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] num = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        
        for (int l = 0; l < s.length();l++){
            for (int i = 0; i < 10; i++){
                s = s.replace(num[i], Integer.toString(i));
            }
        }
        answer = Integer.parseInt(s);
            
        return answer;
    }
}