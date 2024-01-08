import java.util.List;
import java.util.ArrayList;

class Solution {
    List<OilPoint> oilPoints = new ArrayList<>();
    boolean[][] visit;
    int[][] map;
    public int solution(int[][] land) {
        int x = land.length;
        int y = land[0].length;

        this.map = land;
        this.visit = new boolean[land.length][land[0].length];
        extract(x,y);

        int answer = optimizer();

        return answer;
    }

    public void extract(int depth, int width) {
        for(int i = 0 ; i < depth ; i++){
            for(int j = 0 ; j < width ; j++){
                if(map[i][j] == 1 && !visit[i][j]) {
                    OilPoint currentOilPoint = new OilPoint();
                    check(currentOilPoint, i, j);
                    oilPoints.add(currentOilPoint);
                }
            }
        }
    }


    public void check(OilPoint oilPoint, int depth, int width){
        visit[depth][width] = true;
        //refresh variable
        oilPoint.startIdx = Math.min(oilPoint.startIdx, width);
        oilPoint.endIdx = Math.max(oilPoint.endIdx, width);
        oilPoint.amount += 1;


        if(depth+1 < visit.length && !visit[depth+1][width]
           && map[depth+1][width] == 1){
            check(oilPoint, depth+1, width);
        }
        if(depth-1 >= 0 && !visit[depth-1][width]
          && map[depth-1][width] == 1){
            check(oilPoint, depth-1, width);
        }
        if(width+1 < visit[0].length && !visit[depth][width+1]
          && map[depth][width+1] == 1){
            check(oilPoint, depth, width+1);
        }
        if(width-1 >= 0 && !visit[depth][width-1]
          && map[depth][width-1] == 1){
            check(oilPoint, depth, width-1);
        }

    }

    public int optimizer(){
        int answer = 0;
        for(int i = 0 ; i < map[0].length ; i++){
            int temp = 0;
            for(int j = 0 ; j < oilPoints.size() ; j++){
                OilPoint curr = oilPoints.get(j);
                if(curr.startIdx <= i && curr.endIdx >= i){
                    temp += curr.amount;
                }
            }
            answer = Math.max(answer, temp);
        }
        return answer;
    }

    //oil point
    class OilPoint {
        int startIdx;
        int endIdx;
        int amount;

        public OilPoint() {
            startIdx = 500;
            endIdx = 0;
        }

        @Override
        public String toString(){
            return "startIdx:" + startIdx + "  endIdx:" + endIdx + "  amount:" + amount + "\n";
        }
    }   
}