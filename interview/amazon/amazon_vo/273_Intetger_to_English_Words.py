# 273 Intetger to English Words
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # https://leetcode.com/problems/integer-to-english-words/solution/

        # constants
        BILLIONUNIT = 1000000000
        MILLIONUNIT = 1000000
        THOUSANDUNIT = 1000
        HUNDREDUNIT = 100
        TENNERUNIT = 10

        ######################################################
        def one(num):
            dic = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine"
            }
            return dic[num]

        def twoLess20(num):
            dic = {
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen"
            }
            return dic[num]

        def ten(num):
            dic = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety"
            }
            return dic[num]

        def two(num):
            if not num:
                return
            elif num < 10:
                return one(num)
            elif num < 20:
                return twoLess20(num)
            else:
                tenner = num // TENNERUNIT
                rest = num - tenner * TENNERUNIT
                return (ten(tenner) + " " + one(rest)) if rest else ten(tenner) 

        def three(num):
            hundred = num // HUNDREDUNIT
            rest = num - hundred * HUNDREDUNIT

            if hundred and rest:
                return one(hundred) + " Hundred " + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + " Hundred"

        ##################################################################
        # corner case
        if not num:
            return "Zero"

        # get num
        billion = num // BILLIONUNIT
        million = (num - billion * BILLIONUNIT) // MILLIONUNIT
        thousand = (num - billion * BILLIONUNIT - million * MILLIONUNIT) // THOUSANDUNIT
        rest = num - billion * BILLIONUNIT - million * MILLIONUNIT - thousand * THOUSANDUNIT

        result = ""
        if billion:
            result += three(billion) + " Billion"
        if million:
            result += " " if result else ""
            result += three(million) + " Million"
        if thousand:
            result += " " if result else ""
            result += three(thousand) + " Thousand"
        if rest:
            result += " " if result else ""
            result += three(rest)
        return result

