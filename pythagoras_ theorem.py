import math

straightSide1 = float(input("Enter first straight side length: "))
straightSide2 = float(input("Enter the second straight side length: "))


def calcSide(straightSide1, straightSide2):
    straightSide1Squared = straightSide1 * straightSide1
    straightSide2Squared = straightSide2 * straightSide2

    side3Squared = straightSide1Squared + straightSide2Squared

    side3 = math.sqrt(side3Squared)

    return print(f"The third side should be {side3} long")


calcSide(straightSide1, straightSide2)
