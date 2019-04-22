import java.util.HashMap;
import java.util.Map;

public class HuffmanDecoder {
    private static String huffmanDecoder(String[] dict, String input) {
        // check
        if (input == null || input.length() == 0) return null;

        // read in the dict into hashmap
        Map<String, String> map = new HashMap<>();
        for (int i = 0; i < dict.length; i++) {
            String[] full = dict[i].split(" ");
            if (full[0].equals("newline")) {
                map.put(full[1], "\n");
            } else {
                map.put(full[1], full[0]);
            }

        }

        // initialize the result
        StringBuilder sb = new StringBuilder();

        // loop the input
        int start = 0;
        int end = 1;
        while (start < input.length() && end <= input.length()) {
            String subString = input.substring(start, end);
            if (map.containsKey(subString)) {
                // in the hashmap
                sb.append(map.get(subString));
                start = end;
                end = start + 1;
            } else {
                end++;
            }
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        String[] dict = {"a 100100", "b 100101", "c 110001", "d 100000", "newline 1111111", "p 111110", "q 000001"};
        String input = "1111100000011001001111111100101110001100000";
        System.out.print(huffmanDecoder(dict, input));
    }
}
