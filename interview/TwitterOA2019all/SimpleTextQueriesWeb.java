        // process the input sentences
        // store them into arraylist
        List<Map<String, Integer>> list = new ArrayList<>();
        for (String sts : sentences) {
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
        for (String str : queries) {
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

        //return res;
        
        for (String str : res) {
            System.out.println(str);
        }
        System.out.println("\n");

