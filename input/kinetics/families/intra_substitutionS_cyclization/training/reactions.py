#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CH3S2 <=> CH2S2 + H",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (5.42e+09, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (42.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S_Cs;SsJ;S-H
""",
)

entry(
    index = 1,
    label = "C2H5S <=> C2H4S + H",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (9.34e+10, 's^-1'),
        n = 0.6,
        alpha = 1,
        E0 = (35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S_Cs;CsJ-HH;S-H
""",
)

entry(
    index = 2,
    label = "CH3S2-2 <=> CH2S2-2 + H",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.04e+11, 's^-1'),
        n = 0.5,
        alpha = 2,
        E0 = (40.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S_Ss;CsJ-HH;S-H
""",
)

entry(
    index = 3,
    label = "HS3 <=> S3 + H",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (9.65e+11, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (33.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S_Ss;SsJ;S-H
""",
)

entry(
    index = 4,
    label = "C2H5S2 <=> CH2S2-2 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.76e+12, 's^-1'),
        n = 0.2,
        alpha = 0,
        E0 = (34.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S_Ss;CsJ-HH;S-Cs(HHH)
""",
)

entry(
    index = 5,
    label = "CH3S3 <=> CH2S2-2 + HS",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.65e+12, 's^-1'),
        n = 0.1,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S_Ss;CsJ-HH;S-Ss(H)
""",
)

entry(
    index = 6,
    label = "C6H13S <=> C5H10S + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (27000, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""AA Calc""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR5J_SSS_CsRCs;CsJ-CsH;S-Cs(NonDe)
""",
)

entry(
    index = 7,
    label = "C7H15S <=> C6H12S + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (270, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (6.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""AA Calc""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR6J_SSSS_CsRRCs;CsJ-CsH;S-Cs(NonDe)
""",
)

