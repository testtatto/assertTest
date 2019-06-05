import unittest

class assertTest(unittest.TestCase):

    def kaijo(self, x):

        # 整数値のチェック
        if type(x) != int:
            raise TypeError("半角数字の整数値を入れてください")

        # 正の値のチェック
        if x < 0:
            raise ValueError("0以上の整数値を入れてください")

        # 0の場合の階乗は別処理
        if x == 0:
            return 1

        # 階乗計算処理
        for i in range(1, x):
            x *= i
        return x

    def testType(self):
        with self.assertRaises(TypeError):
            test = self.kaijo("abc#$%AVあいう１２３134")
            print(test)

    def testMinus(self):
        with self.assertRaises(ValueError):
            test = self.kaijo(-1)
            print(test)

    def testZero(self):
        test = self.kaijo(0)
        print(test)
        assert test, 1

    def testDecimal(self):
        with self.assertRaises(TypeError):
            test = self.kaijo(1.5)
            print(test)

    def testNormal(self):
        test = self.kaijo(5)
        print(test)
        assert test, 120


if __name__ == "__main__":
    unittest.main()

