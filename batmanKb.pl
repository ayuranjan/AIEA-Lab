
% Facts
hero(batman).
hero(robin).
hero(batgirl).
villain(joker).
villain(riddler).
villain(penguin).
villain(two_face).
villain(poison_ivy).
fights(batman, joker).
fights(joker, batman). 
fights(batman, penguin).
fights(robin, riddler).
fights(batman, two_face).
fights(batgirl, poison_ivy).

% Rules
% Rule 1: Enemies are those who fight each other.
enemies(X, Y) :- fights(X, Y).
enemies(X, Y) :- fights(Y, X).

% Rule 2: A character is a nemesis if they fight each other 
nemesis(X, Y) :- fights(X, Y), fights(Y, X).
