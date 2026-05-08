% Facts
food(burger).
food(sandwich).
food(pizza).

lunch(sandwich).
dinner(pizza).

% Rule
meal(X) :- food(X).

% Food that is both meal and lunch
meal_lunch(X) :-
    meal(X),
    lunch(X).
/////
% Facts
female(neha).
female(sneha).

male(riyaz).

parent(sneha, child1).
parent(riyaz, child1).

% Rule
mother(X, Y) :-
    female(X),
    parent(X, Y).
/////
fahrenheit(C, F) :-
    F is (C * 9/5) + 32.
freezing(C) :-
    C =< 0.


/////


symptom(fever).
symptom(cough).
symptom(headache).

disease(flu) :-
    symptom(fever),
    symptom(cough).

disease(migraine) :-
    symptom(headache).

diagnosis :-
    disease(X),
    write('Disease is: '),
    write(X).