parent(john,mary).
parent(john,tom).
parent(mary,alia).
parent(mary,bob).

male(john).
male(bob).
male(tom).
female(mary).
female(alia).

father(X,Y):-
    parent(X,Y),male(X).
mother(X,Y):-
    parent(X,Y),female(X).
grandparents(X,Y):-
    parent(X,Z),parent(Z,Y).
siblings(X,Y):-
    parent(Z,X),parent(Z,Y),X\=Y.
