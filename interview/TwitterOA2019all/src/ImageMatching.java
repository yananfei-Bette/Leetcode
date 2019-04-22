import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class ImageMatching {
    private static int imageMatching(List<int[]> map1, List<int[]> map2) {
        // bfs traverse together
        // get the record
        int match = 0;

        for (int i = 0; i < map1.size(); i++) {
            for (int j = 0; j < map1.get(i).length; j++) {
                // change in place
                List<int[]> records1 = bfsMap(map1, i, j);
                List<int[]> records2 = bfsMap(map2, i, j);

                // compare the records
                if (isMatch(records1, records2)) {
                    match++;
                }
            }
        }
        return match;

    }

    private static List<int[]> bfsMap(List<int[]> map, int row, int col) {
        List<int[]> res = new ArrayList<>();

        if (map.get(row)[col] == 1) {
            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[]{row, col});
            while (!queue.isEmpty()) {
                int[] temp = queue.poll();
                int r = temp[0];
                int c = temp[1];
                map.get(r)[c] = 0;
                res.add(temp);
                // check the 4 directions
                if (r - 1 >= 0 && c < map.get(r - 1).length && map.get(r - 1)[c] == 1) {
                    queue.offer(new int[]{r - 1, c});
                }
                if (r + 1 < map.size() && c < map.get(r + 1).length && map.get(r + 1)[c] == 1) {
                    queue.offer(new int[]{r + 1, c});
                }
                if (c - 1 >= 0 && map.get(r)[c - 1] == 1) {
                    queue.offer(new int[]{r, c - 1});
                }
                if (c + 1 < map.get(r).length && map.get(r)[c + 1] == 1) {
                    queue.offer(new int[]{r, c + 1});
                }
            }
        }

        return res;
    }

    private static boolean isMatch(List<int[]> l1, List<int[]> l2) {
        if (l1.size() != l2.size()) return false;
        if (l1.size() == 0) return false;
        for (int i = 0; i < l1.size(); i++) {
            if (l1.get(i)[0] != l2.get(i)[0] || l1.get(i)[1] != l2.get(i)[1]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // testcase1
        List<int[]> map1a = new ArrayList<>();
        map1a.add(new int[]{0,0,1});
        map1a.add(new int[]{0,1,1,1});
        map1a.add(new int[]{1,0,1});

        List<int[]> map1b = new ArrayList<>();
        map1b.add(new int[]{0,0,1});
        map1b.add(new int[]{0,1,1,1});
        map1b.add(new int[]{0,0,1});
        System.out.println(imageMatching(map1a, map1b));
        // 1

        // testcase2
        List<int[]> map2a = new ArrayList<>();
        map2a.add(new int[]{0,0,1});
        map2a.add(new int[]{0,1,1,1});
        map2a.add(new int[]{1,0,1});

        List<int[]> map2b = new ArrayList<>();
        map2b.add(new int[]{0,0,1});
        map2b.add(new int[]{0,1,1,1});
        map2b.add(new int[]{0,1,1});
        System.out.println(imageMatching(map2a, map2b));
        // 0

        // testcase3
        List<int[]> map3a = new ArrayList<>();
        map3a.add(new int[]{0,1,0,0});
        map3a.add(new int[]{1,0,0,1});
        map3a.add(new int[]{0,0,1,1});
        map3a.add(new int[]{0,0,1,1});

        List<int[]> map3b = new ArrayList<>();
        map3b.add(new int[]{0,1,0,1});
        map3b.add(new int[]{1,0,0,1});
        map3b.add(new int[]{0,0,1,1});
        map3b.add(new int[]{0,0,1,1});
        System.out.println(imageMatching(map3a, map3b));
        // 2

        // testcase4
        List<int[]> map4a = new ArrayList<>();
        map4a.add(new int[]{0,0,1,0});
        map4a.add(new int[]{0,1,1,1});
        map4a.add(new int[]{0,1,0,0});
        map4a.add(new int[]{1,1,1,1});

        List<int[]> map4b = new ArrayList<>();
        map4b.add(new int[]{0,0,1,0});
        map4b.add(new int[]{0,1,1,1});
        map4b.add(new int[]{0,1,1,0});
        map4b.add(new int[]{1,1,1,1});
        System.out.println(imageMatching(map4a, map4b));
        // 0

    }
}
