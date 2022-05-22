Title: 技巧
Date: 2022-03-19
Status: draft

# Tricks Subset

## L'extrêmité en valeur absolue 通用度：4

$$
\max(a, b) = (a+b+|a-b|)/2
$$

$$
\min(a, b) = (a+b-|a-b|)/2
$$

## L'extrêmité des ensembles 通用度：2

On note $(O_i)$ la famille de tous les sous-ensembles ouverts de $E$. Alors $\mathring E = \text{le maximum de }(O_i) = \bigcup_i O_i$. 

On note $(F_i)$ la famille de tous les sur-ensembles fermés de $E$. Alors $\bar E = \text{le minimum de }(F_i) = \bigcap_i F_i$. 

Donc ${\mathring E}^c = \bigcap_i {O_i}^c = \bar {E^c}$

- 稍微有同样感觉的一个题：

> $p : E \rightarrow F$ une projection. Alors $E = \text{Im}(p)\bigoplus\ker(p)$.  
> Mq $\ker(p) = \text{Im}(Id-f)$:  
> $\ker(p) = \{x_2 | x \in E, x = x_1 + x_2 (x_1 \in \text{Im}(p), x_2 \in \ker(p))\} = \{x - x_1 | x \in E, x = x_1 + x_2 (x_1 \in \text{Im}(p), x_2 \in \ker(p))\} = \text{Im}(Id-f)$

## Fonction - bijectivité 通用度：3.5

$Id = f\circ g$ $\implies$ $f$ surjective, $g$ injective. 

Si $f$ bijective et $Id = f\circ g$; Alors $g = f^{-1}$:  
$f^{-1}\circ Id = f^{-1}\circ f \circ g$, donc $f^{-1} = g$. 

- 一些典型的事情可以用这个来做

> $I = AB$; Alors $A$ inversible et $A^{-1} = B$:  
> $\text{Im}(A)=\R^n$ donc, $\text{rg}(A) = n$, $A$ inversible...  
> 又或者 application linéaire (dimension finie) 也是差不多的思路。

## Analyse - Synthèse 通用度：5

例子：

> $E$ ev et $s \in L(E)$. $s\circ s = Id_E$  
> Mq les seules valeurs propores possibles de $s$ sont $1$ et $-1$:  
> ...  
> Soit $x \in E$. Mq $\exist x_+,x_-\text{ t.q. }x = x_+ + x_-,et,s(x_\pm)=\pm x_\pm$:  
> **Analyse**  
> Soit $x_+,x_-\text{ t.q. }x = x_+ + x_-,et,s(x_\pm)=\pm x_\pm$.  
> Alors $s(x) = s(x_+ + x_-) = x_+ - x_-$  
> De plus $x = x_+ + x_-$.  
> Donc $x_+ = {(x + s(x))\over 2}, x_- = {(x - s(x))\over 2}$.  
> **Synthèse**  
> Mq $x_+ = {(x + s(x))\over 2}, x_- = {(x - s(x))\over 2}$ convient...

这是很妙的啊。在 existe 那一步，我们想要提供一组解，但是没什么想法。于是我们通过 Analyse 来考虑解的必要形式。虽然说最终过程去掉 Analyse 也是说得通的。

## sin sous forme exponentielle 通用度：4

$$
\begin{aligned}
\sin(x) &= {\exp(xi)-\exp(-xi)\over 2i} \\
\cos(x) &= {\exp(xi)+\exp(-xi)\over 2}
\end{aligned}
$$

例题：

> Calculer $\int_0^\pi \sin^3$  
> $$
> \begin{aligned}
> \int_0^\pi \sin(x)^3dx &= \int_0^\pi ({e^{ix}-e^{-ix}\over 2i})^3dx\\
> &= \int_0^\pi {e^{3ix}-3e^{ix}+3e^{-ix}-e^{-3ix}\over -8i}dx\\
> &= -{1\over 4}\int_0^\pi (sin(3x)-3sin(x))dx\\
> &= {4\over 3}
> \end{aligned}
> $$ 

这叫做 linéariser。

## Décomposition - loi binomiale 通用度：3 (dft)

(以下内容是错误的。关于此有一个讨论，在另一片文章中《Experimental Maths（大雾）》)

Si $X ~ B(n, p)$, alors $X = X_1 + X_2 + ... + X_n$ où $\forall k, X_k ~ B(p)$ et ils sont mutullement indépendants. 

有时 loi de Poission 相关的也可以这样子来思考（但能不能这样子证明呢。。？）

## Changement de Variable - Probabilité 通用度：unkonwn (dft)

$X \sim \mathcal{N}(h, \sigma^2)$

Soit $b\in \mathbb{R}$,

$$
\begin{aligned}
\mathbb{P}(X\le b) &= \int_{-\infty}^{b}{1\over \sqrt{2\pi\sigma^2}}e^{(x-h)^2\over -2\sigma^2}dx\\
(CDV: y={x-h\over \sigma})&= \int_{-\infty}^{b-h\over \sigma}{1\over \sqrt{2\pi}}e^{y^2}dy\\
&= \mathbb{P}(Y\le {b-h\over \sigma})
\end{aligned}
$$

où, a posteriori, $Y\sim\mathcal{N}(1, 0)$ et $Y={X-h\over \sigma}$.

## Faire apparaître exp 通用度：3

比如可以用于求解微分方程。

## L'inégalité par binôme de Newton 通用度：3

$$
1+nx \le (1+x)^n~(x\ge 0, n \in \mathbb{N}, n > 1)
$$

Ou similairement. 

> **Example**  
> Mq $\lim (n^{1\over n}) = 1$  
> On pose $x_n = n^{1\over n} - 1$  
> $n = (1+x_n)^n \ge {n(n-1)\over 2}{x_n}^2$  
> $0 \le x_n \le \sqrt{2\over n-1}$  
> Théorème des gerdarmes...

## Comparaison des bornes supérieures et inféreures (ou même 2 nombres...) 通用度：4

$$
Mq~a\le l
$$

- Montrer que $\forall d>0, a\le l+d$ (1)

$$
Mq~\sup H \le l
$$

- Montrer que $\forall t\in H, t \le l$ (2)
- Combiner (1) et (2), on pourrait montrer que $\forall d>0, \forall t\in H, t \le l+d$

> Example  
> Soit $(a_n)$ une suite des réels strictement positives.  
> Mq $\lim \sup (\sqrt[n]{a_n}) \le \lim \sup ({a_{n+1}\over a_{n}})$  
> On note $\alpha=\lim \sup ({a_{n+1}\over a_{n}})$.  
> Si $\alpha = +\infty$, rien à prouver.  Si $\alpha \not= +\infty$
> Soit $\beta > \alpha$, il existe $N$, $\forall n \ge N,{a_n+1\over a_n}\le \beta$.  
> Donc par récurrence simple, $\forall n \ge N, a_n \le \beta^{n-N}a_N$. Donc $\forall n \ge N, \sqrt[n]{a_n} \le \sqrt[n]{\beta^{-N}a_N}\beta$.  
> Or $\lim \sqrt[n]{\beta^{-N}a_N}\beta = \beta$, $\lim \sup (\sqrt[n]{a_n}) \le \beta$  
> On vient de prouver que $\forall \beta > \alpha, \lim \sup (\sqrt[n]{a_n}) \le \beta$  
> On conclut que $\lim \sup (\sqrt[n]{a_n}) \le \alpha = \lim \sup ({a_{n+1}\over a_{n}})$

## Inégalités qui viennent du vide 通用度：4

> Example  
> $\sum a_n$ à termes positifs converge  
> Mq $\sum {\sqrt{a_n}\over n}$ converge  
> Soit $n \in \mathbb{N}$,  
> $(\sqrt{a_n}-{1\over n})^2 \ge 0$  
> d'où $a_n+{1\over n^2} \ge {2\sqrt{a_n}\over n}$.  
> Voilà...

En fait, penser au binôme de Newton.


## Warning SILLY mE

- $\dim \mathbb{R}_n[X] = n+1$ in lieu of $n$
- $\lim_{\pm\infty}\arctan = \pm{\pi\over 2}$ in lieu of $\pm 1$