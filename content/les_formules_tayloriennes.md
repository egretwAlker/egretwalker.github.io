Title: Les Formules Tayloriennes
Date: 2022-05-04
Status: draft
Category: maths

显然这世界上有好多个 Taylor，但其中一个泰勒与众不同，<del>她会唱歌</del>他的名字出现在了许多类似的公式中。

在 L1 的时候，我学习了大约四类泰勒公式，

1. 带 o 的；
2. 带 Reste Intégrale 的；
3. 带 O 的；
4. 带 $f^{(n)}(x_0)$ 的；

(1) 只是要求 n fois dérivable sur un point, (2) 则要求 Cn，而 (3)(4) 则算是 (2) 的 corollaire。（1）的证明比较巧妙，我应该已经在博客某处写过了，本身其一阶形式也十分有用。

而我今天在《baby rudin》上又发现了一个关于 (4) 的论述，对于条件的要求是更松了，十分欣喜。

$\text{On pose}~f:[a, b]\rightarrow\R, \text{t.q.}\\f~\text{de classe n-1 sur}~[a, b],\text{dérivable sur}~]a, b[.~ \alpha, \beta\in]a, b[$

On définit:

$$
P(t) = \sum_{k=0}^{n-1}{f^{(k)}(\alpha)(t-\alpha)^k\over k!}
$$

Mq. $\exist x\in]a, b[, f(\beta)=P(\beta)+{f^{(n)}(x)(\beta-\alpha)^n\over n!}$

Si $\alpha=\beta$, trivial...

法一：

On pose $g(t) = f(t)-P(t)-{M(t-\alpha)^n\over n!}$ avec $M$ t.q. $f(\beta)-P(\beta)-{M(\beta-\alpha)^n\over n!}=0$

$g(\alpha)=g(\beta)=0$, alors, il existe $x_1\in]\alpha, \beta[$ (ou $]\beta, \alpha[$) t.q. $g'(x_1)=0$. Or $g'(\alpha)=0$, il existe $x_2 \in ]\alpha, \beta[$ t.q. $g''(x_2)=0$ ... Il existe $x_n \in ]\alpha, \beta[$ t.q. $g^{(n)}(x_n)=0$

Or, $g^{(n)}(x_n)=f^{(n)}(x_n)-M$. Donc $f(\beta)=P(\beta)+{f^{(n)}(x)(\beta-\alpha)^n\over n!}$.

好妙啊。。
