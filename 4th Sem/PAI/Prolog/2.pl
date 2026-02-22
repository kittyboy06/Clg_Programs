likes(ram,mango).
likes(bill,candy).

girl(seema).

color(rose,red).

owns(john,gold).

likes_item(X,Y):- likes(X,Y).
is_girl(X):- girl(X).
is_owns(X,Y):- owns(X,Y).
likes_sweets(X):- likes(X,candy).
likes_fruits(X):- likes(X,mango).
