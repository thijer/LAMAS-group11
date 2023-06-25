from formula_extended import *
from mlsolver.formula import Not
import mlsolver.formula
from mlsolver.kripke import KripkeStructure, World
from converter import gc, convert_v3 as convert
from param import *
import json

def evaluate(desc, formula, ks, wtt):
    """ Print formula description and evaluation. """
    print(desc)
    print(formula, " = ", formula.semantic(ks, wtt))
    print()

def test_2x2():
    with open(DIR_NW_MODELS + "2x2" + ".json", 'r') as json_file:
        model = json.load(json_file)
    km = convert(model["networks"])
    world = "04_0"
    
    # At first, 04 does not know "p".
    evaluate(
        "At first, 04 does not know \"p\".",
        Not(Knows("04", Atom("p"))),
        km, world
    )

    evaluate(
        "At first, 01, 02, and 03 know \"p\", but 04 does not.",
        And(
            Knows("01", Atom("p")),
            Knows("02", Atom("p")),
            Knows("03", Atom("p")),
            Not(Knows("04", Atom("p")))
        ),
        km, "02_0"
    )
    
    evaluate(
        "At first, not everyone knows \"p\".",
        Not(E(Atom("p"))),
        km, world
    )

    evaluate(
        "After PA(2,3), Everyone knows \"p\" but \"p\" is not common knowledge.",
        PrA({"03", "04"}, Atom("p"), And(E(Atom("p")), Not(C(Atom("p"))))),
        km, world
    )

    evaluate(
        "After PA(1,2,3), 04 knows that 03 and 01 know \"p\", but not that 02 knows \"p\"",
        PrA({"03", "04", "01"}, Atom("p"), 
            And(
                Knows("04", K("03", Atom("p"))),
                Knows("03", K("04", Atom("p"))),
                Knows("04", K("01", Atom("p"))),
                Not(Knows("04", K("02", Atom("p"))))
            )
        ),
        km, world
    )

    evaluate(
        "After PA(1,3,4), the only agent not involved doesn't know anything about what the others know",
        PrA({"01", "03", "04"}, Atom("p"), 
            And(
                Not(Knows("02", K("03", Atom("p")))),
                Not(Knows("02", K("04", Atom("p")))),
                Not(Knows("02", K("01", Atom("p"))))
            )
        ),
        km, world
    )

def test_simple_3a():
    with open(DIR_NW_MODELS + "simple_3a" + ".json", 'r') as json_file:
        model = json.load(json_file)
    km = convert(model["networks"])
    world = "03_0"

    
    evaluate(
        "At first, 03 does not know that 02 knows \"p\".",
        Not(Knows("03", K("02", Atom("p")))),
        km, "03_0"
    )

    
    evaluate(
        "At first, 03 does not know \"p\".",
        Not(Knows("03", Atom("p"))),
        km, world
    )

    evaluate(
        "At first, 01 and 02 know \"p\", but 03 does not.",
        And(
            Knows("01", Atom("p")),
            Knows("02", Atom("p")),
            Not(Knows("03", Atom("p")))
        ),
        km, "02_0"
    )

    evaluate(
        "At first, 02 does not know that 01 knows \"p\".",
        Not(Knows("02", K("01", Atom("p")))),
        km, "02_0"
    )
    
    evaluate(
        "02 and 03 do not know that 01 knows \"p\".",
        And(Not(Knows("02", K("01", Atom("p")))), Not(Knows("03", K("01", Atom("p"))))),
        km, "02_0"
    )
    
    
    evaluate(
        "At first, not everyone knows \"p\".",
        Not(E(Atom("p"))),
        km, world
        )

    evaluate(
        "After PA(2,3), everyone knows \"p\"",
        PrA({"02", "03"}, Atom("p"), E(Atom("p"))),
        km, world
    )

    evaluate(
        "After PA(2,3), 3 does not know that 1 knows \"p\"",
        PrA({"02", "03"}, Atom("p"), Not(Knows("03", K("01", Atom("p"))))),
        km, world
    )
    
    evaluate(
        "After PA(2,3), Everyone knows \"p\" but \"p\" is not common knowledge.",
        PrA({"02", "03"}, Atom("p"), And(E(Atom("p")), Not(C(Atom("p"))))),
        km, world
    )

    evaluate(
        "After PA(1,2,3), Everyone knows \"p\" and \"p\" is common knowledge.", 
        PrA({"01", "02", "03"}, Atom("p"), And(E(Atom("p")), C(Atom("p")))),
        km, world
        )
    
    evaluate(
        "After PA(2,3), 02 knows that 03 knows \"p\" and vice versa, but 02 and 03 do not know that 01 knows \"p\".",
        PrA({"02", "03"}, Atom("p"), 
            And(
                Knows("02", K("03", Atom("p"))),
                Knows("03", K("02", Atom("p"))),
                Not(Knows("03", K("01", Atom("p")))),
                Not(Knows("02", K("01", Atom("p"))))
            )
        ),
        km, world
    )

    evaluate(
        "After PA(2,3) and PA(3,1), 02 is the only one that does not know that 01 knows \"p\".",
        PrA({"02", "03"}, Atom("p"), 
            PrA({"03", "01"}, Atom("p"), 
                And(
                    Knows("02", K("03", Atom("p"))),
                    Knows("03", K("02", Atom("p"))),
                    Knows("03", K("01", Atom("p"))),
                    Not(Knows("02", K("01", Atom("p"))))
                )
            )
        ),
        km, world
    )

    evaluate(
        "After PA(2,3), 02 knows that 03 knows \"p\" and vice versa, but 02 and 03 do not know that 01 knows \"p\".",
        PrA({"02", "03"}, Atom("p"), 
            PrA({"03", "01"}, Atom("p"), 
                PrA({"01", "02"}, Atom("p"), 
                    And(
                        Knows("02", K("03", Atom("p"))),
                        Knows("03", K("02", Atom("p"))),
                        Knows("03", K("01", Atom("p"))),
                        Knows("02", K("01", Atom("p")))
                    )
                )
            )
        ),
        km, world
    )

    evaluate(
        "After PA(2,3), PA(3,1), and PA(1,2), 02 finally knows that 01 knows \"p\", and thus \"p\" becomes common knowledge.",
        PrA({"02", "03"}, Atom("p"), 
            PrA({"03", "01"}, Atom("p"), 
                PrA({"01", "02"}, Atom("p"), 
                    C(Atom("p"))
                )
            )
        ),
        km, world
    )

if __name__ == "__main__":
    test_simple_3a()