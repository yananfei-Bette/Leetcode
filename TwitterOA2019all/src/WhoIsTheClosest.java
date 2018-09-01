import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class WhoIsTheClosest {
    private static int[] closest(String s, int[] indexes) {
        // use two hashmap
        // first store index O(n) and process at the same time
        Map<Character, List<Integer>> charToList = new HashMap<>();
        int[] indexDict = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            // add the index to the store
            if (charToList.containsKey(c)) {
                // get the list
                List<Integer> list = charToList.get(c);
                list.add(i);
                charToList.put(c, list);
                // after adding, check if the size is larger or equal to 3
                int tempIdx = list.size() - 1;
                if (tempIdx >= 2) {
                    int beforeDiff = list.get(tempIdx - 1) - list.get(tempIdx - 2);
                    int afterDiff = list.get(tempIdx) - list.get(tempIdx - 1);
                    // update the index map
                    if (afterDiff < beforeDiff) {
                        indexDict[list.get(tempIdx - 1)] = tempIdx;
                    }
                } else if (tempIdx == 1) {
                    // update the first
                    indexDict[list.get(tempIdx - 1)] = tempIdx;
                }
                // add the before by default
                indexDict[i] = tempIdx - 1;
            } else {
                List<Integer> list = new ArrayList<>();
                list.add(i);
                charToList.put(c, list);
                // since it is the very first, index start with itself
                indexDict[i] = 0;
            }
        }

        // process the indexes
        int[] res = new int[indexes.length];
        for (int i = 0; i < indexes.length; i++) {
            int idx = indexes[i];
            int mapIndex = charToList.get(s.charAt(idx)).get(indexDict[idx]);
            res[i] = mapIndex == idx ? -1 : mapIndex;
        }

        return res;


    }

    private static void printArray(int[] array) {
        for (int i : array) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        // testcase 1
        String test1 = "babab";
        int[] index1 = {2};
        printArray(closest(test1, index1));
        // 0

        // testcase 2
        String test2 = "hackerrank";
        int[] index2 = {4, 1, 6, 8};
        printArray(closest(test2, index2));
        // -1 7 5 -1

    }
}
