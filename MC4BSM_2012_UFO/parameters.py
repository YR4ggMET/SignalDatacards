# This file was automatically created by FeynRules $Revision: 915 $
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 27 Feb 2012 20:15:51



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MM1 = Parameter(name = 'MM1',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{MM1}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

MM2 = Parameter(name = 'MM2',
                nature = 'external',
                type = 'real',
                value = 300,
                texname = '\\text{MM2}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

MM12 = Parameter(name = 'MM12',
                 nature = 'external',
                 type = 'real',
                 value = 50,
                 texname = '\\text{MM12}',
                 lhablock = 'FRBlock',
                 lhacode = [ 3 ])

lam1 = Parameter(name = 'lam1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{lam1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 4 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{lam2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 5 ])

lam1p = Parameter(name = 'lam1p',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{lam1p}',
                  lhablock = 'FRBlock',
                  lhacode = [ 6 ])

lam2p = Parameter(name = 'lam2p',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{lam2p}',
                  lhablock = 'FRBlock',
                  lhacode = [ 7 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 120,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

Muv = Parameter(name = 'Muv',
                nature = 'external',
                type = 'real',
                value = 500,
                texname = '\\text{Muv}',
                lhablock = 'MASS',
                lhacode = [ 9000008 ])

Mev = Parameter(name = 'Mev',
                nature = 'external',
                type = 'real',
                value = 250,
                texname = '\\text{Mev}',
                lhablock = 'MASS',
                lhacode = [ 9000009 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

Wpe1 = Parameter(name = 'Wpe1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wpe1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

Wpe2 = Parameter(name = 'Wpe2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wpe2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000007 ])

Wuv = Parameter(name = 'Wuv',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wuv}',
                lhablock = 'DECAY',
                lhacode = [ 9000008 ])

Wev = Parameter(name = 'Wev',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wev}',
                lhablock = 'DECAY',
                lhacode = [ 9000009 ])

MPe1 = Parameter(name = 'MPe1',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(MM1**2 + MM2**2 - cmath.sqrt(MM1**4 + 4*MM12**4 - 2*MM1**2*MM2**2 + MM2**4))/cmath.sqrt(2)',
                 texname = '\\text{MPe1}')

MPe2 = Parameter(name = 'MPe2',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(MM1**2 + MM2**2 + cmath.sqrt(MM1**4 + 4*MM12**4 - 2*MM1**2*MM2**2 + MM2**4))/cmath.sqrt(2)',
                 texname = '\\text{MPe2}')

th = Parameter(name = 'th',
               nature = 'internal',
               type = 'real',
               value = 'cmath.acos(1/cmath.sqrt(1 + (-MM1**2 + MM2**2 + cmath.sqrt(4*MM12**4 + (MM1**2 - MM2**2)**2))**2/(4.*MM12**4)))',
               texname = '\\text{th}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '(2*MW*sw)/ee',
              texname = 'v')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*v**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*v**2)',
                texname = '\\mu')

