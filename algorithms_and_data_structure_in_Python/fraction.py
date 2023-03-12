from math import gcd

class Fraction:
    """
    fraction class
    """
    def __init__(self, top:int, bottom:int = 1) -> None:
        if bottom == 0:
            raise ZeroDivisionError("Error: DENOMINATOR CAN NOT BE ZERO")
        else:
            if isinstance(top, int) and isinstance(bottom, int):
                top = (-1) * top if bottom < 0 else top
                bottom = abs(bottom)
                common = gcd(top, bottom)
                self.num = top // common
                self.den = bottom // common
            else:
                raise RuntimeError("Error: NUMERATOR OR DENOMINATOR IS NOT INTERGER")
    
    def getNum(self) -> int:
        return self.num
    
    def getDen(self) -> int:
        return self.den
    
    def __str__(self) -> str:
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self, other:"Fraction") -> "Fraction":
        newNum = self.num * other.den + self.den * other.num
        newDen = self.den * other.den
        # Fraction constructor ensures that the new fraction is irreducible
        return Fraction(newNum , newDen)
    
    def __sub__(self, other:"Fraction") -> "Fraction":
        newNum = self.num * other.den - self.den * other.num
        newDen = self.den * other.den
        return Fraction(newNum , newDen)
    
    def __mul__(self, other:"Fraction") -> "Fraction":
        newNum = self.num * other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)
    
    def __truediv__(self, other:"Fraction") -> "Fraction":
        newNum = self.num * other.den
        newDen = self.den * other.num
        return Fraction(newNum, newDen)
    
    def __eq__(self, other:"Fraction") -> bool:
        return (self.num * other.den) == (other.num * self.den)
    
    def __le__(self, other:"Fraction") -> bool:
        return (self.num * other.den) <= (other.num * self.den)
    
    def __ge__(self, other:"Fraction") -> bool:
        return (self.num * other.den) >= (other.num * self.den)
    
    def __lt__(self, other:"Fraction") -> bool:
        return not self.__ge__(other)

    def __gt__(self, other:"Fraction") -> bool:
        return not self.__le__(other)
    
    def __ne__(self, other:"Fraction") -> bool:
        return not self.__eq__(other)


if __name__ == "__main__":
    f1 = Fraction(3, 7)
    f2 = Fraction(2, 4)
    print(f1 <= f2)