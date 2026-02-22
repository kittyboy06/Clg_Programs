start :-
    write('Enter Celsius: '),
    read(C),
    convert(C).

convert(C) :-
    F is (C * 9 / 5) + 32,
    write('Fahrenheit value: '),
    write(F), nl,
    ( C =< 32 ->
        write('Freezing point')
    ;
        write('Above freezing point')
    ).
