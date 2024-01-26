import math

def zigzag_conversion(s, numRows):
        if numRows == 1:
            return s
        rows = [""] * numRows
        goingDown = True
        i = 0
        for ch in s:
            if i > numRows - 1:
                i = numRows - 2
                goingDown = False
            if i < 0:
                i = 1
                goingDown = True
            if goingDown:
                rows[i] += ch
                i += 1
            else:
                rows[i] += ch
                i -= 1
        return ''.join(rows)

test1 = "PAYPALISHIRING"
print(zigzag_conversion(test1, 3))
test2 = "A"
print(zigzag_conversion(test2, 1))

