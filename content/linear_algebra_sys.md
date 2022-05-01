Title: 线性代数机械方法概要
Date: 2022-04-09
Status: draft

（记住了，一个 $\deg P \le 3$ 的多项式有 4 项！）

## Points de Vue

* Système Linéaire
* Représentation Matricielle
* Espace Vectoriel

### Pour obtenir Img et ker explicitement...

#### Méthode

$A \in M_{n, m}(𝕂)$

Pour obtenir l'image et le noyau dans un pivot de Gauss: 

On fait le pivot de Gauss sur les lignes, on obtient le $\text{rg}(A)$ $\dim \ker A$. 

- En posant repectivement les variables libres 1, et réduisant les autres terms, on obtient $\ker A$

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

<!-- Why \\\\ you might ask! Oh the stupid python-markdown. I will fix it one day (seems a little difficult for me though) -->

$\text{Img} A = \text{Vect}(C1, C2, C3)$  
$\ker A = (-1, 6, 7, 0)$

- Mais on peut également résoudre cette question par système linéaire. 

$$
\begin{pmatrix}
1 & -1 & 1 & 1  & a\\
5 & 2 & -1 & -3 & b\\
-3 & -4 & 3 & 2 & c\\
6 & 1 & 0 & -2  & d
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & -1 & 1 & 1  & a\\
0 & 7 & -6 & -8 & b-5a\\
0 & 0 & 0 & -3  & -2a+b+c\\
0 & 0 & 0 & 0   & -a-b+d
\end{pmatrix}
$$

Donc $\text{Img}A = \{(a, b, c, d)|-a-b+d = 0\}$. Cela est encore une fois un noyau. Alors on pose respectivement b=1, c=1, d=1...