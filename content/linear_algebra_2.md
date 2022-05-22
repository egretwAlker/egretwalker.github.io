Title: 线性代数奇思妙想
Date: 2022-05-07
Status: Draft

[TOC]

## Comment montrer si 2 matrices peuvent être pivotées à une même matrice?

Suppose A une matrice, A se pivote à deux matrices B, C échelonnées réduites. Montrons que B = C.

On démontre par l'absurde en supposant que B != C.

On constate que, quand A pivote, l'espace engendré de ses vecteurs de ligne ne change pas.

Or, il existe une ligne de C qui ne peux pas être combinaison linéaire des lignes de B.

Contradiction.

Cela étant dit, on a aussi démontré que, en effet, si 2 matrices peux se pivoter à une même matrice, leur matrice échelonnée réduite doit être identique.

Pour résumer, (sur les lignes et les colonnes) deux matrice ont un même image iff leur matrice échlonnée réduite est identique iff ils peuvent se pivoter à une même matrice.

## Pourraient 2 matrices (qui ont le même noyau) se pivotent à une même matrice?

Si! Car la matrice échelonnée réduite associée est déterminée par le noyau. 

Soit A une matrice,

A' la matrice échelonée réduite (de ligne) associée à A. Déjà on a une base de ker A qui forme une matrice échelonnée réduite. Or quand on fait 'poser les colonnes libres 1 resp. et obtenir une base de ker A', on obtient une base, si elle forme une matrice, échelonnée réduite. Donc les deux bases doivent être identique. Depuis les étapes pour déterminer la 2e base on déterimine A'.

On constate aussi que Im(At) (+) Ker(A) = E

Facile à prouver: Soit x dans Im(At) et Ker(A), alors on fait pivot la matrice tellement que x appraît, on voit que, si x != 0, A'x != 0, x n'est pas dans Ker(A).

写得好恶心。。