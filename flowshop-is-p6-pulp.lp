\* flowshop-is-p6 *\
Minimize
OBJ: s_(5,_3)
Subject To
_C1: x_(1,_1) + x_(2,_1) + x_(3,_1) + x_(4,_1) + x_(5,_1) = 1
_C10: x_(5,_1) + x_(5,_2) + x_(5,_3) + x_(5,_4) + x_(5,_5) = 1
_C11: s_(0,_1) = 0
_C12: s_(0,_2) = 0
_C13: s_(0,_3) = 0
_C14: s_(1,_0) = 0
_C15: s_(2,_0) = 0
_C16: s_(3,_0) = 0
_C17: s_(4,_0) = 0
_C18: s_(5,_0) = 0
_C19: - s_(1,_0) + s_(1,_1) - 6 x_(1,_1) - 2 x_(2,_1) - 6 x_(3,_1)
 - 4 x_(4,_1) - 5 x_(5,_1) >= 0
_C2: x_(1,_2) + x_(2,_2) + x_(3,_2) + x_(4,_2) + x_(5,_2) = 1
_C20: - s_(0,_1) + s_(1,_1) - 6 x_(1,_1) - 2 x_(2,_1) - 6 x_(3,_1)
 - 4 x_(4,_1) - 5 x_(5,_1) >= 0
_C21: - s_(2,_0) + s_(2,_1) - 6 x_(1,_2) - 2 x_(2,_2) - 6 x_(3,_2)
 - 4 x_(4,_2) - 5 x_(5,_2) >= 0
_C22: - s_(1,_1) + s_(2,_1) - 6 x_(1,_2) - 2 x_(2,_2) - 6 x_(3,_2)
 - 4 x_(4,_2) - 5 x_(5,_2) >= 0
_C23: - s_(3,_0) + s_(3,_1) - 6 x_(1,_3) - 2 x_(2,_3) - 6 x_(3,_3)
 - 4 x_(4,_3) - 5 x_(5,_3) >= 0
_C24: - s_(2,_1) + s_(3,_1) - 6 x_(1,_3) - 2 x_(2,_3) - 6 x_(3,_3)
 - 4 x_(4,_3) - 5 x_(5,_3) >= 0
_C25: - s_(4,_0) + s_(4,_1) - 6 x_(1,_4) - 2 x_(2,_4) - 6 x_(3,_4)
 - 4 x_(4,_4) - 5 x_(5,_4) >= 0
_C26: - s_(3,_1) + s_(4,_1) - 6 x_(1,_4) - 2 x_(2,_4) - 6 x_(3,_4)
 - 4 x_(4,_4) - 5 x_(5,_4) >= 0
_C27: - s_(5,_0) + s_(5,_1) - 6 x_(1,_5) - 2 x_(2,_5) - 6 x_(3,_5)
 - 4 x_(4,_5) - 5 x_(5,_5) >= 0
_C28: - s_(4,_1) + s_(5,_1) - 6 x_(1,_5) - 2 x_(2,_5) - 6 x_(3,_5)
 - 4 x_(4,_5) - 5 x_(5,_5) >= 0
_C29: - s_(1,_1) + s_(1,_2) - 10 x_(1,_1) - 8 x_(2,_1) - 4 x_(3,_1)
 - 2 x_(4,_1) - 3 x_(5,_1) >= 0
_C3: x_(1,_3) + x_(2,_3) + x_(3,_3) + x_(4,_3) + x_(5,_3) = 1
_C30: - s_(0,_2) + s_(1,_2) - 10 x_(1,_1) - 8 x_(2,_1) - 4 x_(3,_1)
 - 2 x_(4,_1) - 3 x_(5,_1) >= 0
_C31: - s_(2,_1) + s_(2,_2) - 10 x_(1,_2) - 8 x_(2,_2) - 4 x_(3,_2)
 - 2 x_(4,_2) - 3 x_(5,_2) >= 0
_C32: - s_(1,_2) + s_(2,_2) - 10 x_(1,_2) - 8 x_(2,_2) - 4 x_(3,_2)
 - 2 x_(4,_2) - 3 x_(5,_2) >= 0
_C33: - s_(3,_1) + s_(3,_2) - 10 x_(1,_3) - 8 x_(2,_3) - 4 x_(3,_3)
 - 2 x_(4,_3) - 3 x_(5,_3) >= 0
_C34: - s_(2,_2) + s_(3,_2) - 10 x_(1,_3) - 8 x_(2,_3) - 4 x_(3,_3)
 - 2 x_(4,_3) - 3 x_(5,_3) >= 0
_C35: - s_(4,_1) + s_(4,_2) - 10 x_(1,_4) - 8 x_(2,_4) - 4 x_(3,_4)
 - 2 x_(4,_4) - 3 x_(5,_4) >= 0
_C36: - s_(3,_2) + s_(4,_2) - 10 x_(1,_4) - 8 x_(2,_4) - 4 x_(3,_4)
 - 2 x_(4,_4) - 3 x_(5,_4) >= 0
_C37: - s_(5,_1) + s_(5,_2) - 10 x_(1,_5) - 8 x_(2,_5) - 4 x_(3,_5)
 - 2 x_(4,_5) - 3 x_(5,_5) >= 0
_C38: - s_(4,_2) + s_(5,_2) - 10 x_(1,_5) - 8 x_(2,_5) - 4 x_(3,_5)
 - 2 x_(4,_5) - 3 x_(5,_5) >= 0
_C39: - s_(1,_2) + s_(1,_3) - 4 x_(1,_1) - 3 x_(2,_1) - 5 x_(3,_1)
 - 7 x_(4,_1) - 4 x_(5,_1) >= 0
_C4: x_(1,_4) + x_(2,_4) + x_(3,_4) + x_(4,_4) + x_(5,_4) = 1
_C40: - s_(0,_3) + s_(1,_3) - 4 x_(1,_1) - 3 x_(2,_1) - 5 x_(3,_1)
 - 7 x_(4,_1) - 4 x_(5,_1) >= 0
_C41: - s_(2,_2) + s_(2,_3) - 4 x_(1,_2) - 3 x_(2,_2) - 5 x_(3,_2)
 - 7 x_(4,_2) - 4 x_(5,_2) >= 0
_C42: - s_(1,_3) + s_(2,_3) - 4 x_(1,_2) - 3 x_(2,_2) - 5 x_(3,_2)
 - 7 x_(4,_2) - 4 x_(5,_2) >= 0
_C43: - s_(3,_2) + s_(3,_3) - 4 x_(1,_3) - 3 x_(2,_3) - 5 x_(3,_3)
 - 7 x_(4,_3) - 4 x_(5,_3) >= 0
_C44: - s_(2,_3) + s_(3,_3) - 4 x_(1,_3) - 3 x_(2,_3) - 5 x_(3,_3)
 - 7 x_(4,_3) - 4 x_(5,_3) >= 0
_C45: - s_(4,_2) + s_(4,_3) - 4 x_(1,_4) - 3 x_(2,_4) - 5 x_(3,_4)
 - 7 x_(4,_4) - 4 x_(5,_4) >= 0
_C46: - s_(3,_3) + s_(4,_3) - 4 x_(1,_4) - 3 x_(2,_4) - 5 x_(3,_4)
 - 7 x_(4,_4) - 4 x_(5,_4) >= 0
_C47: - s_(5,_2) + s_(5,_3) - 4 x_(1,_5) - 3 x_(2,_5) - 5 x_(3,_5)
 - 7 x_(4,_5) - 4 x_(5,_5) >= 0
_C48: - s_(4,_3) + s_(5,_3) - 4 x_(1,_5) - 3 x_(2,_5) - 5 x_(3,_5)
 - 7 x_(4,_5) - 4 x_(5,_5) >= 0
_C5: x_(1,_5) + x_(2,_5) + x_(3,_5) + x_(4,_5) + x_(5,_5) = 1
_C6: x_(1,_1) + x_(1,_2) + x_(1,_3) + x_(1,_4) + x_(1,_5) = 1
_C7: x_(2,_1) + x_(2,_2) + x_(2,_3) + x_(2,_4) + x_(2,_5) = 1
_C8: x_(3,_1) + x_(3,_2) + x_(3,_3) + x_(3,_4) + x_(3,_5) = 1
_C9: x_(4,_1) + x_(4,_2) + x_(4,_3) + x_(4,_4) + x_(4,_5) = 1
Binaries
x_(1,_1)
x_(1,_2)
x_(1,_3)
x_(1,_4)
x_(1,_5)
x_(2,_1)
x_(2,_2)
x_(2,_3)
x_(2,_4)
x_(2,_5)
x_(3,_1)
x_(3,_2)
x_(3,_3)
x_(3,_4)
x_(3,_5)
x_(4,_1)
x_(4,_2)
x_(4,_3)
x_(4,_4)
x_(4,_5)
x_(5,_1)
x_(5,_2)
x_(5,_3)
x_(5,_4)
x_(5,_5)
End
