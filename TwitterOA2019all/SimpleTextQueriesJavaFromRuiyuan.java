    static void textQueries(List<String> sentences, List<String> queries) {
        for (String query : queries) {
            String[] words = query.split(" ");
            StringBuilder match_list = new StringBuilder();
            int ind = 0;
            
            for (String s : sentences) {
                Map<String, Integer> d = new HashMap<>();
                for (String word : words) {
                    d.put(word, d.getOrDefault(word,0));
                }
                String[] s_words = s.split(" ");
                for (String s_w : s_words) {
                    if (d.containsKey(s_w)) {
                        int tempValue = d.get(s_w)+1;
                        d.put(s_w, tempValue);                
                    }
                }
                int minCount = Integer.MAX_VALUE;
                String minKey = "";
                for (String key : d.keySet()) {
                    if (d.get(key) < minCount) {
                        minCount = d.get(key);
                        minKey = key;
                    }
                }
                while (minCount > 0) {
                    match_list.append(ind).append(" ");
                    minCount--;
                }
                ind++;        
            }
            if (match_list.length() == 0) {
                System.out.println("-1");
            } else {
                System.out.println(match_list);
            }
        }
    }
