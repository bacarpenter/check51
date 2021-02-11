import check50

@check50.check()
def squareEachNumber():
    """squareEachNumber"""
    check50.run("cd bin && java testSquareEachNumber").stdin("1 2 3", prompt=False).stdout("{1.0, 4.0, 9.0}", regex=False).exit()
    check50.run("cd bin && java testSquareEachNumber").stdin("1.3 9 3.449", prompt=False).stdout("{1.6900000000000002, 81.0, 11.895601}", regex=False).exit()

@check50.check()
def divisibleBy7():
    """divisibleBy7"""
    check50.run("cd bin && java testDivisibleBy7").stdin("7 5 14", prompt=False).stdout("{true, false, true}", regex=False).exit()
    check50.run("cd bin && java testDivisibleBy7").stdin("41 12 56", prompt=False).stdout("{false, false, true}", regex=False).exit()