import java.util.ArrayList;
import java.util.List;

public class MissingWords {
    private static List<String> missingWords(String a, String b) {
        // store the two lists
        String[] alist = a.split(" ");
        String[] blist = b.split(" ");

        // initialize the res
        List<String> res = new ArrayList<>();

        int aptr = 0;
        int bptr = 0;

        while (bptr < blist.length) {
            String btemp = blist[bptr];
            while (aptr < alist.length) {
                String atemp = alist[aptr];
                if (atemp.equals(btemp)) {
                    // if the two are the same, both add 1
                    aptr++;
                    bptr++;
                    break;
                } else {
                    res.add(atemp);
                    aptr++;
                }
            }
        }

        // to check if there is still missing
        while (aptr < alist.length) {
            res.add(alist[aptr]);
            aptr++;
        }

        return res;

    }

    public static void main(String[] args) {
        String str1 = "I am using HackerRank to improve programming";
        String str2 = "am HackerRank to improve";
        for (String str : missingWords(str1, str2)) {
            System.out.println(str);
        }
    }
}
