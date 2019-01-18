10.0 MeV photons in room temp water
100   1    -1.0       -10         imp:n=1
101   1    -1.0       -11 10      imp:n=1
102   1    -1.0       -12 11      imp:n=1
103   1    -1.0       -13 12      imp:n=1
104   1    -1.0       -14 13      imp:n=1
105   1    -1.0       -15 14      imp:n=1
999   0               +15         imp:n=0

10   so    10.0
11   so    20.0
12   so    30.0
13   so    40.0
14   so    50.0
15   so    10000.0

mode p
nps    1e8
sdef   pos = 0 0 0   erg = 0.1
c
m1     1000.12p   1.0
c
f02:p  10 11 12 13 14
e0     1e-3 988i 0.0999 9i 0.1
ft2 INC
fu2 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 &
    21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 &
    40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 &
    51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 &
    70 71 72 73 74 75 76 77 78 79 80
c
phys:p j  1  0 0  1
prdmp  j  1e7  1   1
