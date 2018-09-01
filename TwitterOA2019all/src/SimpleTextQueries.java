import com.sun.tools.corba.se.idl.InterfaceGen;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SimpleTextQueries {
    private static List<String> textQueries(String[] sentence, String[] phrases) {
        // process the input sentences
        // store them into arraylist
        List<Map<String, Integer>> list = new ArrayList<>();
        for (String sts : sentence) {
            String[] words = sts.split(" ");
            Map<String, Integer> map = new HashMap<>();
            for (String word : words) {
                map.put(word, map.getOrDefault(word, 0) + 1);
            }
            list.add(map);
        }

        // initialize the res
        List<String> res = new ArrayList<>();

        // loop for the phrases
        for (String str : phrases) {
            String[] words = str.split(" ");
            StringBuilder sb = new StringBuilder();
            // loop for the list
            int idx = 0;
            for (Map<String, Integer> temp : list) {
                // for each sentence, loop for the words and get the min
                int minCount = Integer.MAX_VALUE;
                for (String word : words) {
                    if (temp.containsKey(word)) {
                        // if this sentence contains this word, get the number
                        int num = temp.get(word);
                        minCount = Math.min(minCount, num);
                    } else {
                        minCount = Integer.MAX_VALUE;
                        break;
                    }
                }
                while (minCount != Integer.MAX_VALUE && minCount > 0) {
                    sb.append(idx).append(" ");
                    minCount--;
                }
                idx++;
            }
            // check the stringbuilder
            if (sb.length() == 0) {
                sb.append("-1");
            }
            // add this result into res
            res.add(sb.toString().trim());
        }

        return res;

    }

    private static void printList(List<String> list) {
        for (String str : list) {
            System.out.println(str);
        }
        System.out.println("\n");
    }

    public static void main(String[] args) {
        // testcase 1
        String[] sentences1 = {"bob and alice like to text each other", "bob does not like to ski", "alice likes to ski"};
        String[] phrases1 = {"bob alice", "alice", "like"};
        printList(textQueries(sentences1, phrases1));
        // 0, 0 2, 0 1

        // testcase 2
        String[] sentences2 = {"jim likes mary", "kate likes tom", "tom does not like jim"};
        String[] phrases2 = {"jim tom", "likes"};
        printList(textQueries(sentences2, phrases2));
        // 2, 0 1

        // testcase 3
        String[] sentences3 = {"how it was done", "are you how", "it goes to", "goes done are it"};
        String[] phrases3 = {"done it", "it"};
        printList(textQueries(sentences3, phrases3));
        // 0 3, 0 2 3

        // testcase 4
        String[] sentences4 = {"it go will away", "go do it", "what to will east"};
        String[] phrases4 = {"it will", "go east will", "will"};
        printList(textQueries(sentences4, phrases4));
        // 0, -1, 0 2

        // testcase 5
        String[] sentences5 = {"bob alice bob alice bob alice"};
        String[] phrases5 = {"bob alice"};
        printList(textQueries(sentences5, phrases5));
        // 0 0 0

        // testcase 6
        String[] sentences6 = {"bob alice bob alice bob alice"};
        String[] phrases6 = {"bob alice bob alice"};
        //printList(textQueries(sentences6, phrases6));
    }
}
