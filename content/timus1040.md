Title: Timus 1040 Solution
Date: 2022-05-02
Category: Timus

[题面](https://timus.online/problem.aspx?space=1&num=1040)

题意：有一张无向简单联通图，n 点 m 边。请将 m 条边分配上 [1, m] 中的一个整数使得每一个点，如果有不止一条边，那么这些边的 gcd 为 1。

注意到 gcd(k, k+1) = 1。于是，如果我们将一条欧拉路径上的边依次分配上 a, a+1, ..., a+b，那么除了路径两端的点，路径上的点一定都已经“满足”了。

la question fameuse：如果从一个点开始尽可能走（并附上 a, a+1, ...），走一条边删一条边，会停在哪里呢？

1. 停在出发点——有点不妙；
2. 停在路径上之前走过的点——没什么问题；
3. 停在度数为 1 的点——没什么问题；

* 如果 a=1，那么就算停在出发点也没有什么问题。

于是我们觉得随意走，删除走过的点和边也许没什么问题；有意思的地方在于，如果删除一条路径上的点和边，剩下的图可能有一些边（我们称之为残疾边）是存在至少一端没有点的。对于这样的图，接下来我们证明一些东西：

1. 在一个联通块（这个联通块我们允许存在残疾边）中删除一条“尽可能路径”（路径可以是从边开始也可以是从点开始/结束）后留下的是一些联通块，每个联通块都有一条残疾边。
2. 从残疾边开始尽可能走，走完后路径上所有点一定是“满足”的
3. 存在残疾边的联通块可以从任意的 a 开始赋值并有解。


1 简单，2 简单（因为只有回到原点的情况开始走会有问题，然而这种情况下没有原点），3 用 récurrence 可以得出。

于是我们随便选一给点开始尽可能走，一开始的图没有残疾边，但就算回到原点也没有关系，因为从 1 开始标号。然后一直从残疾边开始走就好了，无论从几开始标号都没有关系。

代码这次写得还是挺漂亮的嘿嘿

```c
#include<stdio.h>
#include<string.h>

#define N 50
#define M (N*N)
#define elog(...) fprintf(stderr, __VA_ARGS__)

int n, m;
int fr[N], ne[M], to[M], ans[M], satisfied[N];
int cnt;

void dfs(int x) {
	for(int i=fr[x];~i;i=ne[i]) {
		if(!ans[i/2]) {
			if(satisfied[x]) {
				if(!satisfied[to[i]]) {
					ans[i/2] = ++cnt;
					dfs(to[i]);
				}
			} else {
				ans[i/2] = ++cnt;
				satisfied[x] = 1;
				if(!satisfied[to[i]])
					dfs(to[i]);
			}
		}
	}
}

int main(void) {
	printf("YES\n");
	memset(fr, -1, sizeof(fr));
	scanf("%d%d", &n, &m);
	for(int i=0, u, v;i<m;++i) {
		scanf("%d%d", &u, &v);
		--u;--v;
		ne[2*i] = fr[u];
		to[fr[u] = 2*i] = v;
		ne[2*i+1] = fr[v];
		to[fr[v] = 2*i+1] = u;
	}
	dfs(0);
	for(int i=0;i<m;++i) {
		if(!ans[i])
			ans[i] = ++cnt;
		printf("%d ", ans[i]);
	}
	return 0;
}
```

