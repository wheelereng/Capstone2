# Capstone3
<<<<<<< HEAD
Coin sorting web application for the IN4.0 group Capstone project.
=======
Background research:
assuming that the project will consist of us being given an amount and
then finding the possible combinations of coins to make that amount or
some equivalent type of problem.

Essentially this is called the subset sum problem, which is an open problem in
mathematics and it is NP-complete, meaning there's no guaranteed algorithm for
doing it better than brute force. However, we still have the following results.

We can know for sure if it's possible to sum to the given value with a given 
set of coins by just checking the greatest common divisor, like so:

given a bag of 50ps and a bag of 20ps and a bag of £1, can I make £22.40 with them? YES, first we multiply the pennies by 100 to make everything integral (an integer), now we just want to know if we can find X1,X2,X3 such that 
X1 x 20 + X2 x 50 + X3 x 100 = 2240 which is true if (AND ONLY IF) greatest common divisor of 20, 50, 100 divides 2240, which it does as gcd(20, 50, 100)=10 and 2240/10= 224 which is an integer.

in general:

let D1, D2 ... Dn be denominations and T is the required total then 
X1 x D1 + X2 x D2 + ... Xi x Di + ... Xn x Dn = T has integer solutions if (AND ONLY IF) gcd(D1, D2, ... Dn) divides T.

why? Because we can factor out the gcd and we then have (as in the case above)
gcd(10, 20, 100)(X1 x 5 + X2 x 2 + X3 x 10)=2240 which is saying a number times another number on the left hand side equals a single whole number on the right hand side, which can only be the case if both numbers on the LHS divdes the number on the RHS ... i.e gcd divides T

This can be used as a very quick check to see if we can actually get solutions before wasting time finding them all.


Case for only two denominations can be solved using the extended euclidean 
algorithm, but eh, too much, maybe a neat brute force method as we'll have to use brute force for more than two denominations anyway. I'll have a better look.
>>>>>>> da7c934554200d4090d7f2cd5a2d7060d04ea60b
