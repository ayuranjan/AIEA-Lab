from pyswip import Prolog


prolog = Prolog()

prolog.consult("batmanKb.pl") 


enemies_batman = list(prolog.query("enemies(batman, X)"))
print("Enemies of Batman:")
for enemy in enemies_batman:
    print(enemy["X"])

batman_joker_nemesis = list(prolog.query("nemesis(batman, joker)"))
print("Are Batman and Joker nemeses?:", bool(batman_joker_nemesis))

batman_two_face_enemies = list(prolog.query("enemies(batman, two_face)"))
print("Are Batman and Two-Face enemies?:", bool(batman_two_face_enemies))


batman_two_face_nemesis = list(prolog.query("nemesis(batman, two_face)"))
print("Are Batman and Two-Face nemesis?:", bool(batman_two_face_nemesis))