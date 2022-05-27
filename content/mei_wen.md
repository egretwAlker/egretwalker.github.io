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

**Remarque**: 当 $f,g$ continues 的时候，取等条件等价于两函数 proportionnelles。

## Inégalité par la formule de Taylor avec reste intégral

### Type 1 (普通)

$$
\text{Soit } x \in ℝ,\\
\begin{aligned}
\ln(1+x) &= x + \int_0^x (x-t){1\over 1+x}dx\\
&\le x
\end{aligned}
$$

这适合那些积分 signe 一定的。这样的结论在 ℝ 下是一致的。

### Type 2 (Je suis épaté | 我好傻)

$\text{Soit}~x \in ℝ^+,$
$$
\begin{aligned}
\sin(x) &= x - {x^3\over 6} + \int_0^x{(x-t)^4\over 4!}cos(x)dx\\
&\le x - {x^3\over 6} + \int_0^x{(x-t)^4\over 4!}1dx\\
&= x - {x^3\over 6} + {x^5\over 5!}\\
\end{aligned}
$$

De même, $\forall x \in ℝ^+, \sin(x) \ge x - {x^3\over 6} - {x^5\over 5!}$

这是很妙啊，不过要注意 x 的符号。

## Développement Limité avec reste petit o

Au voisinage de x, $]x-\eta, x+\eta[$. 

Supposons que $F$ dérivable, de dérivée $f$, $f(x) = o((x-x_0)^n)$.  
Mq, $F(x) = F(x_0) + o((x-x_0)^{n+1})$  
sorry

Mq, $\forall$ $f$ dérivable $n$ fois,  
$f(x) = \sum_{k=0}^n {(x-x_0)^n\over n!}f^{(n)}(x_0)+o((x-x_0)^n)$

On démontre par récurrence.  

-   Initialisation, sorry  
-   Hérédité, supposons $f$ dérivable $n+1$ fois.  
    Par la hérédité, $f'(x) = \sum_{k=0}^n {(x-x_0)^n\over n!}f^{(n)}(x_0)+o((x-x_0)^n)$  
    sorry

## L'inégalité des accroissements finis - fonctions vectorielles

On pose $f: [a, b]\rightarrow \R^k$, continue sur $[a, b]$, dérivable sur $]a, b[$.

Mq. $\exist x\in]a, b[, |f(b)-f(a)|\le (b-a)|f'(x)|$

On pose $z = f(b)-f(a)$, $\phi(t)=z\cdot f(t)$.

Il existe $x\in]a, b[$ t.q. $\phi(b)-\phi(a) = \phi'(x)(b-a)$.

Alors, $|z|^2 = z\cdot z = (b-a)\cdot \phi'(x) = (b-a)(z\cdot f'(x)) \le (b-a)|z||f'(x)|$

Ainsi, si $|z|=0$...si $|z|\not=0$...