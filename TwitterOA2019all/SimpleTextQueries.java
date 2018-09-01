private static List<String> textQueries(String[] sentence, String[] phrases) {
	for (String query : queries) {
		String[] words = query.split(" ");
		StringBuilder match_list = new StringBuilder();
		int ind = 0;
		for (String s : sentence) {
			Map<String, Integer> d = new HashMap<>();
			for (String word : words) {
				d.put(word, d.getOrDefault(word,0)+1);
			}
			String[] s_words = s.split(" ");
			for (String s_w : s_words) {
				if (d.conotainsKey(s_w)) {
					int tempValue = d.get(s_w)+1;
					d.put(s_w, tempValue);				
				}
			}
			int minCount = Integer.Max_VALUE;
			String minKey = "";
			for (String key : d.keySet()) {
				if (d.get(key) < minCount) {
					minCount = d.get(key);
					minKey = key;
				}
			}
			while (minCount > 0) {
				match_list.append(str(ind)).append(" ");
				minCount--;
			}
			ind++;		
		}
		if (matdch_list.length == 0) {
			system.out.println("-1");
		} else {
			system.out.println(match_list);
		}
	}

