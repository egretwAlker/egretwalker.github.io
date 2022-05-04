Title: Experimental Maths（大雾）
Date: 2022-05-03
Status: draft
Category: Maths

## Intro

今天在 TD 里遇到了一道题：

> $X \sim ℬ(n_1, p), Y \sim ℬ(n_2, p)$ v.a. indépendantes.  
> Déterminer la loi de $X+Y$

在 le corrigé 里如此写道：

> Une manière intelligente de procéder est la suivante:  
> Considéron $n_1 + n_2$ variables aléatoires de loi $ℬ(p)$ indépendantes, $U_1, \dots, U_{n_1}, V_1,\dots,V_{n_2}$.  
> Puisqu'on ne s'intéresse qu'aux lois, on peut remplacer $X$ par $U_1+\dots+U_{n_1}$, $Y$ par $V_1+\dots+V_{n_2}$.  
> Comme toutes ces variables sont indépendantes, $X_1 + X_2$ a alors même loi que $U_1+\dots+U_{n_1}+V_1+\dots+V_{n_2}$, c'est-à-dire $ℬ(n_1+n_2, p)$. 

## Section 1: 讲好一个故事

我并不以为 le corrigé 是正确的。首先一个 $X \sim ℬ(n, p)$ 不一定就能被写成 $X = U_1+\dots+U_n$ 的形式。其次，就算 $X~et~Y$ indépendantes, $U_1,\dots,U_{n_1}$ indépendantes, $V_1,\dots,V_{n_2}$ indépendantes. $U_1,\dots,U_{n_1},V_1,\dots,V_{n_2}$ 也并不一定 indépendantes. 

所以 le corrigé 并不正确。

于是我们这样做：

$Soit~m\in \N,$  
$$
\begin{aligned}
ℙ(X+Y=m) &= ℙ(\bigsqcup_{k=0}^m(X=k\land Y=m-k))\\
&= \sum_{k=0}^m{n_1\choose k}p^k(1-p)^{n_1-k}{n_2\choose m-k}p^{m-k}(1-p)^{n_2-m+k}\\
&= p^m(1-p)^{n_1+n_2-m}\sum_{k=0}^m{n_1\choose k}{n_2\choose m-k} (\text{Vandermonde's Identity})\\
&= p^m(1-p)^{n_1+n_2-m}{n_1+n_2\choose m}
\end{aligned}
$$

于是有 $X+Y\sim ℬ(n_1+n_2, p)$. 

我们突然发现，其实我们根本不在乎 $\Omega$ 是什么样的。

## Section 2: 点题

由 Section 1，我们想要证明的不过是：

$$
\forall m\in\llbracket0, n_1+n_2\rrbracket, \sum_{k=0}^m{n_1\choose k}p^k(1-p)^{n_1-k}{n_2\choose m-k}p^{m-k}(1-p)^{n_2-m+k} = p^m(1-p)^{n_1+n_2-m}{n_1+n_2\choose m}
$$

对此，我们对 le corrigé 中提到的那样的变量进行“实验”：

On obtient $U_1,\dots,U_{n_1},V_1,\dots,V_{n_2} \sim ℬ(p)$ indépendantes, 

On pose $X' = U_1+\dots+U_{n_1}, Y' = V_1+\dots+V_{n_2}$, alors on a: 

1. $X', Y'$ indépendantes; 
2. $X'\sim ℬ(n_1, p), Y'\sim ℬ(n_2, p)$;
3. $X'+Y' = U_1+\dots+U_{n_1}+V_1+\dots+V_{n_2}\sim ℬ(n_1+n_2,p)$;

Par conséquent:

Soit $m\in\llbracket0, n_1+n_2\rrbracket$,

Par 1. 2. $ℙ(X'+Y'=m)=\sum_{k=0}^m{n_1\choose k}p^k(1-p)^{n_1-k}{n_2\choose m-k}p^{m-k}(1-p)^{n_2-m+k}$.  
Par 3. $ℙ(X'+Y'=m)=p^m(1-p)^{n_1+n_2-m}{n_1+n_2\choose m}$.  
Donc, $\sum_{k=0}^m{n_1\choose k}p^k(1-p)^{n_1-k}{n_2\choose m-k}p^{m-k}(1-p)^{n_2-m+k}=p^m(1-p)^{n_1+n_2-m}{n_1+n_2\choose m}.$.  
Donc, $ℙ(X+Y=m)=\sum_{k=0}^m{n_1\choose k}p^k(1-p)^{n_1-k}{n_2\choose m-k}p^{m-k}(1-p)^{n_2-m+k}=p^m(1-p)^{n_1+n_2-m}{n_1+n_2\choose m}$.

Donc, $X+Y\sim ℬ(n_1+n_2,p)$

也许，le corrigé 还是有一点擦边球的道理的。

## Section 3: Reread

<del>“一点擦边球的道理的”</del>

> «Puisqu'on ne s'intéresse qu'aux lois»

也许他注意到了、也就是说我在 Section 1 中的想法完全是臆想。但这句话究竟是什么意思呢？

对于此我有一些猜测。但猜测作者本来的意思并没有什么实际意义，作者的意思完全可以像是我在 Section 2 中表达的那样，落实到最后的和式上。重要的是这句话应该有什么意思。

Supposons $X\sim L_1, Y\sim L_2$ indépendantes, essayons de déterminer la loi de $F(X, Y)$.

On obtient $X'\sim L_1, Y'\sim L_2$ indépendantes, t.q. $F(X', Y')\sim L$.  
On note $F(X, Y)\sim L$ proposition p. 

这 p 应该是对的吧，我好想赶紧学测度论和 *A Probability Path* 啊。

## Section 4: Section 1

> «$(\text{Vandermonde's Identity})$»

这是什么，你在最后一个等于号那里干了什么？

但对于范德蒙德卷积，我确实不知道在生成函数与实际意义之外的证明。

虎头蛇尾了。挖坑了。