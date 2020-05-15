public class Blog {
	public static void main(String[] args) {
		//集合
		String[] ar = {"a","b","c"};

		//要素数
		int n = 3;

		//以下メイン処理
		for (int i=0; i<(1<<n); i++) {
      // System.out.println(i);
			String s = "-";
			for (int j=0; j<n; j++) {
          System.out.println(i+" "+j+" "+(i>>j)+" "+(1&i>>j));
          if ((1&i>>j) == 1) {
              s += ar[j];
          }
          // else {
            // System.out.println(ar[j]);
          // }
			}
			// System.out.println(s);
		}
		/*出力

		-
		-a
		-b
		-ab
		-c
		-ac
		-bc
		-abc

		*/
	}
}
