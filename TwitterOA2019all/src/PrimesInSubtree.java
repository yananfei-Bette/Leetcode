public class PrimesInSubtree {
    private static int[] primeQuery(int number, int[] starts, int[] ends, int[] values, int[] queries) {
        int[] countDict = new int[number];
        int[] indexDict = new int[number];

        // initialize the count of primes
        for (int i = 0; i < values.length; i++) {
            countDict[i] = isPrime(values[i]) ? 1 : 0;
        }

        // initialize the index list
        for (int i = 0; i < indexDict.length; i++) {
            indexDict[i] = i;
        }
        for (int i = 0; i < starts.length; i++) {
            int idx = ends[i] - 1;
            int ptr = starts[i] - 1;
            indexDict[idx] = ptr;
        }

        // fill in the number of primes
        for (int i = 0; i < countDict.length; i++) {
            // loop and add
            int temp = i;
            while (indexDict[temp] != temp) {
                temp = indexDict[temp];
                countDict[temp] += countDict[i];
            }
        }

        // do the queries
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            res[i] = countDict[queries[i] - 1];
        }
        return res;

    }

    private static boolean isPrime(int n) {
        // from restritions, all the values >= 1
        if (n <= 3) return true;

        // if it is a even number
        if (n % 2 == 0) return false;

        // loop from 3
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }

        return true;
    }

    private static void printList(int[] list) {
        for (int i : list) {
            System.out.print(i + " ");
        }
    }

    public static void main(String[] args) {
        // testcase 1
        int n = 6;
        int[] startNodes = {1, 2, 2, 1, 3}; // 5 edges
        int[] endNodes = {2, 4, 5, 3, 6}; // size: 5
        int[] values = {2, 2, 6, 5, 4, 3}; // size: 6
        int[] queries = {1, 4, 5, 6, 2}; // size: 5
        printList(primeQuery(n, startNodes, endNodes, values, queries));
        // 4 1 0 1 2
    }
}
