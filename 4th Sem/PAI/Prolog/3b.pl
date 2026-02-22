symptom(joe, fever).
symptom(joe, cough).

symptom(mary, headache).
symptom(mary, sore_throat).

symptom(kevin, fever).

has_flu(Patient) :-
    symptom(Patient, fever),
    symptom(Patient, cough).

has_cold(Patient) :-
    symptom(Patient, headache),
    symptom(Patient, sore_throat).

diagnose(Patient, flu) :-
    has_flu(Patient).

diagnose(Patient, cold) :-
    has_cold(Patient).

diagnose(_, unknown) :-
    fail.
