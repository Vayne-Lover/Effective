# -*- coding: utf-8 -*-

a=[False]*21
a[0] = False
a[1] = True and True
a[2] = False and True
a[3] = 1 == 1 and 2 == 1
a[4] = "test" == "test"
a[5] = 1 == 1 or 2 != 1
a[6] = True and 1 == 1
a[7] = False and 0 != 0
a[8] = True or 1 == 1
a[9] = "test" == "testing"
a[10] = 1 != 0 and 2 == 1
a[11] = "test" != "testing"
a[12] = "test" == 1
a[13] = not (True and False)
a[14] = not (1 == 1 and 0 != 1)
a[15] = not (10 == 1 or 1000 == 1000)
a[16] = not (1 != 10 or 3 == 4)
a[17] = not ("testing" == "testing" and "Zed" == "Cool Guy")
a[18] = 1 == 1 and (not ("testing" == 1 or 1 == 0))
a[19] = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
a[20] = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

for i in range(21):
  print(a[i])
