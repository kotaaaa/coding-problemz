'''
参考: https://uchidama.hatenablog.com/entry/2021/07/19/011732

[問題]
https://atcoder.jp/contests/abc210/tasks/abc210_d
[解説]
https://youtu.be/_mhHn_o6b3Y?t=3093　
　基本、snukeさんのこのコードをPythonコンバート
https://atcoder.jp/contests/abc210/editorial/2298
https://kanpurin.hatenablog.com/entry/2021/07/17/232213
https://blog.hamayanhamayan.com/entry/2021/07/17/233152
　なんか難しいやなー。
[参考]
https://atcoder.jp/contests/abc210/submissions/24334817?lang=ja
　このコードの書き方もすごいな
[結果]
PyPy3(7.3.0) AC 378ms
Python(3.8.2) TLE
'''

INF = 2 ** 63 - 1

H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = INF
for l in range(2):

    # dp初期化。このdpはdp[i][j]に駅を建設するときに最小となる、もう一点の駅と線路のコストが入る
    dp = [[INF] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            # dp[i][j]に隣の点からコストを引っ張ってくる。
            # dp[i][j]には、もう一点の駅と線路の最小コストが入るので、引っ張ってくる
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            # このi, jの地点に２つ目の駅を建設して最終的なコストを出す。これが最小か？
            ans = min(ans, A[i][j]+C*(i+j) + dp[i][j])
            # dpには展開式からの、その点のコストが最小なら入れる
            dp[i][j] = min(dp[i][j], A[i][j]-C*(i+j))

    # 条件が i' <= i , j' <= jなので反転したバージョンも計算する必要がある
    A.reverse()

print(ans)