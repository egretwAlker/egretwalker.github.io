Title: 线性代数机械方法概要
Date: 2022-04-09
Status: draft

[TOC]

<del>（记住了，一个 $\deg P \le 3$ 的多项式有 4 项！）</del>

## Points de Vue

* Système Linéaire
* Représentation Matricielle
* Espace Vectoriel

### Pour obtenir Img et ker explicitement (dans un pivot de Gauss!)

$A \in M_{n, m}(𝕂)$

Pour obtenir l'image et le noyau dans un pivot de Gauss: 

On fait le pivot de Gauss sur les lignes, on obtient le $\text{rg}(A)$ $\dim \ker A$. 

- En posant repectivement les variables libres 1 (ou un autre valeur plus maline mais non-nulle), et réduisant les autres terms, on obtient $\ker A$

- En choisissant les colonnes de pivot dans A, on obtient $\text{Img} A$

#### Exemple

$$
\begin{pmatrix}
1 & -1 & 1 & 1\\
5 & 2 & -1 & -3\\
-3 & -4 & 3 & 2 \\
6 & 1 & 0 & -2
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & -1 & 1 & 1 \\
0 & 7 & -6 & -8 \\
0 & 0 & 0 & -3 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

$\text{Img} A = \text{Vect}(C1, C2, C3)$  
$\ker A = (-1, 6, 7, 0)$

- Mais on peut également résoudre cette question par système linéaire. 

$$
\begin{pmatrix}
1 & -1 & 1 & 1  &\bigm| & a\\
5 & 2 & -1 & -3 &\bigm| & b\\
-3 & -4 & 3 & 2 &\bigm| & c\\
6 & 1 & 0 & -2  &\bigm| & d
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & -1 & 1 & 1  &\bigm| & a\\
0 & 7 & -6 & -8 &\bigm| & b-5a\\
0 & 0 & 0 & -3  &\bigm| & -2a+b+c\\
0 & 0 & 0 & 0   &\bigm| & -a-b+d
\end{pmatrix}
$$

Donc $\text{Img}A = \{(a, b, c, d)|-a-b+d = 0\}$. Cela est encore une fois un noyau. Alors on pose respectivement b=1, c=1, d=1...

### Pour calculer $E \cap F$ ou $E + F$

首先，$E$ 与 $F$ 是如何被表示出来的呢？

1. $\text{Im}(f)$ 的形式（$\text{Vect}(u_1, ..., u_n)$）；
2. $\ker(f)$ 的形式；
3. système d'équations 的形式；

2 与 3 没有什么区别。所以我们只用讨论 1, 2 的情况就好了。

注意到 1 求 $+$ 比较容易，2 求 $\cap$ 比较容易，我们考虑要如何进行 1 与 2 之间的转换。

> 1 求 $+$，将 $\text{Vect}$ 中的元素放在一起就好了。  
> 2 求 $\cap$，要么将两个矩阵上下叠在一起，要么将 systèmes 联立，没有什么本质区别，但叠矩阵显然更有趣。

**1 -> 2**

可以用之前提到的方法：

$$
\begin{pmatrix}
1 & -1 & 1 & 1  &\bigm| & a\\
5 & 2 & -1 & -3 &\bigm| & b\\
-3 & -4 & 3 & 2 &\bigm| & c\\
6 & 1 & 0 & -2  &\bigm| & d
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & -1 & 1 & 1  &\bigm| & a\\
0 & 7 & -6 & -8 &\bigm| & b-5a\\
0 & 0 & 0 & -3  &\bigm| & -2a+b+c\\
0 & 0 & 0 & 0   &\bigm| & -a-b+d
\end{pmatrix}
$$

那么关心不存在 pivot 的行（也就是全 0 的行）:

$$
\ker
\begin{pmatrix}
-1 & -1 & 0 & 1
\end{pmatrix}
=\text{l'image}
$$

矩阵狂热分子也可以将上述过程写成这样：

$$
\begin{pmatrix}
1 & -1 & 1 & 1  &\bigm| & 1 & 0 & 0 & 0\\
5 & 2 & -1 & -3 &\bigm| & 0 & 1 & 0 & 0\\
-3 & -4 & 3 & 2 &\bigm| & 0 & 0 & 1 & 0\\
6 & 1 & 0 & -2  &\bigm| & 0 & 0 & 0 & 1
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & -1 & 1 & 1  &\bigm| & 1 & 0 & 0 & 0\\
0 & 7 & -6 & -8 &\bigm| & -5 & 1 & 0 & 0\\
0 & 0 & 0 & -3  &\bigm| & -2 & 1 & 1 & 0\\
0 & 0 & 0 & 0   &\bigm| & -1 & -1 & 0 & 1
\end{pmatrix}
$$

然后直接取得右下的子矩阵。

**2 -> 1**

想必大家已经很熟悉了：

$$
\begin{pmatrix}
1 & -1 & 1 & 1\\
5 & 2 & -1 & -3\\
-3 & -4 & 3 & 2\\
6 & 1 & 0 & -2
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & -1 & 1 & 1\\
0 & 7 & -6 & -8\\
0 & 0 & 0 & -3\\
0 & 0 & 0 & 0
\end{pmatrix}
$$

然后将遍历每个没有 pivot 的列，分别将其设为 1（或者其他好的非零数） 将其他自由的元设为 0，得到一组 base。在上面这个例子中

$$
\text{le noyau} = \text{Vect}\begin{pmatrix}-13 \\ -6 \\ 7 \\ 0\end{pmatrix}
$$

### misc

- 在用 tricky 方法做 diagonalisation 的时候可以先瞧瞧 noyau 也就是 valeur propre = 0 的 espace propre。