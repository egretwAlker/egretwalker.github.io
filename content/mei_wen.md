Title: 美文荟萃
Date: 2022-03-19
Status: draft

[TOC]

[LEAN: 如果...我将能够解决哥德巴赫猜想：不（难）可（以）计算的函数](https://xenaproject.wordpress.com/2019/06/11/the-inverse-of-a-bijection/)

# 一些美妙的证明

## L'inégalité de Cauchy-Schwarz

$$
\int_a^b (xf(t)+g(t))^2 dt = x^2\int_a^b f^2+x(2\int_a^b fg)+\int_a^b g^2 \ge 0
$$

Donc

$$
\Delta = 4((\int_a^b fg)^2-(\int_a^b f^2)(\int_a^b g^2)) \le 0
$$

$$
(\int_a^b fg)^2 \le (\int_a^b f^2)(\int_a^b g^2)
$$

$\int$ 完全可以被替换成 $\sum$。只可惜只能在实数域下。但这还是一个超级漂亮的证明。对我来说。

**Remarque**: 当 $f,g$ continues 的是否，取等条件等价于两函数 proportionnelles。

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

## Décomposition - loi binomiale 通用度：3

Si $X ~ B(n, p)$, alors $X = X_1 + X_2 + ... + X_n$ où $\forall k, X_k ~ B(p)$ et ils sont mutullement indépendants. 

有时 loi de Poission 相关的也可以这样子来思考（但能不能这样子证明呢。。？）

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