# -------------------------------------------------------------------------------
# Name:         Calc
# Version:      0.3
#
# Author:       Richter
#
# Created:      31/12/2013
#-------------------------------------------------------------------------------


from decimal import *
getcontext().prec = 4
import numpy.linalg as np
import sopromat_python.classes


def expandArray(a, b, n):
    j = float(a)
    temp = []
    while j < b:
        temp.append(round(j, 2))
        j = j + 1.0 / 10.0
    return temp


def getMTS(_beam):
    zk = [0, _beam.length]  #switch points
    for i in _beam.arraySec:
        if i != "not set":
            zk.append(i.length)
    for i in _beam.arrayM:
        if i != "not set":
            zk.append(i.point)
    for i in _beam.arraym:
        if i != "not set":
            zk.append(i.a)
            zk.append(i.b)
    zk = list(set(zk))
    nk = len(zk) - 1  #amount of intervals
    zk2 = []  #switch points
    heigth = []
    for i in _beam.arraySec:
        if i != "not set":
            zk2.append(i.length)
            zk2.append(i.length2)
            heigth.append(i.heigth)
            heigth.append(i.heigth2)

    zk2 = zk2  # sdelat shtobi v sectorah bilo 2 visoti na nachale i konve
    heigth = heigth

    M = []
    T = []
    z = []
    #ready to this point
    A = []  #плоади поперечного сечения
    for k in range(nk):
        z0 = expandArray(zk[k], zk[k + 1], 100)
        for i in range(len(z0)):
            if z0[i] in z:
                z0.remove(z0[i])
                break
        M0 = []
        T0 = []
        A0 = []

        for i in range(len(z0)):
            M0.append(0.0)
            T0.append(0.0)
            A0.append(0.0)
        if _beam.hasM():
            nM = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayM)):
                if _beam.arrayM[j].point < zk[k + 1]:
                    nM.append(j)
            for k1 in range(len(nM)):
                for j in range(len(M0)):
                    M0[j] = M0[j] + _beam.arrayM[nM[k1]].amount * (_beam.arrayM[nM[k1]].point)
        if _beam.hasm():
            nm1 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arraym)):
                if _beam.arraym[j].a < zk[k + 1]:
                    nm1.append(j)
            for k1 in range(len(nm1)):
                for j in range(len(M0)):
                    M0[j] = M0[j] + (_beam.arraym[nm1[k1]].qa) * (z0[j] - _beam.arraym[nm1[k1]].a) * _beam.arraym[
                        nm1[k1]].a
            nm2 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arraym)):
                if _beam.arraym[j].b < zk[k + 1]:
                    nm2.append(j)
            for k1 in range(len(nm2)):
                for j in range(len(M0)):
                    M0[j] = M0[j] - _beam.arraym[nm2[k1]].qa * (z0[j] - _beam.arraym[nm2[k1]].b) * _beam.arraym[
                        nm2[k1]].b
        z.extend(z0)
        M.extend(M0)
        T.extend(T0)
        A.extend(A0)

    #problema v sectorah, nado sdelat tam 4 param - nachalo i konec
    for i in range(0, len(z)):
        for k in range(len(zk2) - 1):
            if z[i] > zk2[k] and z[i] <= zk2[k + 1]:
                #print zk2[k]
                if heigth[k] != heigth[k + 1]:
                    A[i] = 3.1415 * abs(
                        (heigth[k + 1] - heigth[k]) * ((z[i] - zk2[k]) / (zk2[k + 1] - zk2[k])) + heigth[k]) ** 4 / 32.0
                else:
                    A[i] = (abs(3.1415 * (heigth[k] ** 4) / 32.0))
            if z[i] == zk2[k]:
                A[i] = (abs(3.1415 * (heigth[k] ** 4) / 32.0))

    for i in range(len(A)):
        T[i] = float((M[i] / A[i]) * (z[i]))  #ugli povorota
    return [z, M, T]


def getNLS(_beam):
    zk = [0, _beam.length]  #switch points
    for i in _beam.arraySec:
        if i != "not set":
            zk.append(i.length)
    for i in _beam.arrayP:
        if i != "not set":
            zk.append(i.point)
    for i in _beam.arrayQ:
        if i != "not set":
            zk.append(i.a)
            zk.append(i.b)
    zk = list(set(zk))
    nk = len(zk) - 1  #amount of intervals
    zk2 = []  #switch points
    heigth = []
    for i in _beam.arraySec:
        if i != "not set":
            zk2.append(i.length)
            zk2.append(i.length2)
            heigth.append(i.heigth)
            heigth.append(i.heigth2)
            #i
    zk2 = zk2  # sdelat shtobi v sectorah bilo 2 visoti na nachale i konve
    heigth = heigth

    N = []
    L = []
    S = []
    z = []
    #ready to this point
    A = []  #плоади поперечного сечения
    for k in range(nk):
        z0 = expandArray(zk[k], zk[k + 1], 100)
        for i in range(len(z0)):
            if z0[i] in z:
                z0.remove(z0[i])
                break
        N0 = []
        L0 = []
        S0 = []
        A0 = []

        for i in range(len(z0)):
            N0.append(0.0)
            L0.append(0.0)
            S0.append(0.0)
            A0.append(0.0)
        if _beam.hasP():
            nP = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayP)):
                if _beam.arrayP[j].point < zk[k + 1]:
                    nP.append(j)
            for k1 in range(len(nP)):
                for j in range(len(N0)):
                    N0[j] = N0[j] + _beam.arrayP[nP[k1]].amount * (_beam.arrayP[nP[k1]].point)
        if _beam.hasQ():
            nQ1 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayQ)):
                if _beam.arrayQ[j].a < zk[k + 1]:
                    nQ1.append(j)
            for k1 in range(len(nQ1)):
                for j in range(len(N0)):
                    N0[j] = N0[j] + (_beam.arrayQ[nQ1[k1]].qa) * (z0[j] - _beam.arrayQ[nQ1[k1]].a)
            nQ2 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayQ)):
                if _beam.arrayQ[j].b < zk[k + 1]:
                    nQ2.append(j)
            for k1 in range(len(nQ2)):
                for j in range(len(N0)):
                    N0[j] = N0[j] - _beam.arrayQ[nQ2[k1]].qa * (z0[j] - _beam.arrayQ[nQ2[k1]].b)
        z.extend(z0)
        N.extend(N0)
        S.extend(S0)
        L.extend(L0)
        A.extend(A0)

    #problema v sectorah, nado sdelat tam 4 param - nachalo i konec
    for i in range(0, len(z)):
        for k in range(len(zk2) - 1):
            if z[i] > zk2[k] and z[i] <= zk2[k + 1]:
                #print zk2[k]
                if heigth[k] != heigth[k + 1]:
                    A[i] = 3.1415 * abs(
                        (heigth[k + 1] - heigth[k]) * ((z[i] - zk2[k]) / (zk2[k + 1] - zk2[k])) + heigth[k]) ** 2 / 4.0
                else:
                    A[i] = (abs(3.1415 * (heigth[k] ** 2) / 4.0))
            if z[i] == zk2[k]:
                A[i] = (abs(3.1415 * (heigth[k] ** 2) / 4.0))

    for i in range(len(A)):
        S[i] = float(N[i] / A[i])
        L[i] = float((N[i] / A[i]) * (_beam.length - z[i]))

    return [z, N, L, S]


def getQMT(_beam):
    tmp = calc(_beam)
    S = tmp[0]
    zk = tmp[1]
    neq = tmp[2]
    nk = tmp[3]
    Q = []
    M = []
    T = []
    z = []
    for k in range(nk):
        z0 = expandArray(zk[k], zk[k + 1], 100)
        for i in range(len(z0)):
            if z0[i] in z:
                z0.remove(z0[i])
                break
        M0 = []
        for i in range(len(z0)):
            M0.append(S[2] + S[3] * z0[i])
        if _beam.hasOp():
            nR = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayOp)):
                if _beam.arrayOp[j] < zk[k + 1]:
                    nR.append(j)
            for k1 in range(len(nR)):
                for j in range(len(M0)):
                    M0[j] = M0[j] + S[nR[k1] + 4] * (z0[j] - _beam.arrayOp[nR[k1]])
        if _beam.hasM():
            nM = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayM)):
                if _beam.arrayM[j].point < zk[k + 1]:
                    nM.append(j)
            for k1 in range(len(nM)):
                for j in range(len(M0)):
                    M0[j] = M0[j] + _beam.arrayM[nM[k1]].amount
        if _beam.hasP():
            nP = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayP)):
                if _beam.arrayP[j].point < zk[k + 1]:
                    nP.append(j)
            for k1 in range(len(nP)):
                for j in range(len(M0)):
                    M0[j] = M0[j] + _beam.arrayP[nP[k1]].amount * (z0[j] - _beam.arrayP[nP[k1]].point)
        if _beam.hasQ():
            nQ1 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayQ)):
                if _beam.arrayQ[j].a < zk[k + 1]:
                    nQ1.append(j)
            for k1 in range(len(nQ1)):
                ck = ((_beam.arrayQ[nQ1[k1]].qb - _beam.arrayQ[nQ1[k1]].qa) / (
                    _beam.arrayQ[nQ1[k1]].b - _beam.arrayQ[nQ1[k1]].a))
                for j in range(len(M0)):
                    M0[j] = M0[j] + (_beam.arrayQ[nQ1[k1]].qa) * (z0[j] - _beam.arrayQ[nQ1[k1]].a) ** 2 / 2 + ck * (z0[
                                                                                                                        j] -
                                                                                                                    _beam.arrayQ[
                                                                                                                        nQ1[
                                                                                                                            k1]].a) ** 3 / 6 - ck * (
                                                                                                                                                        z0[
                                                                                                                                                            j] -
                                                                                                                                                        _beam.arrayQ[
                                                                                                                                                            nQ1[
                                                                                                                                                                k1]].b) ** 3 / 6
            nQ2 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayQ)):
                if _beam.arrayQ[j].b < zk[k + 1]:
                    nQ2.append(j)
            for k1 in range(len(nQ2)):
                for j in range(len(M0)):
                    M0[j] = M0[j] - _beam.arrayQ[nQ2[k1]].qb * (z0[j] - _beam.arrayQ[nQ2[k1]].b) ** 2 / 2
        z.extend(z0)
        M.extend(M0)
    z = []
    for k in range(nk):
        z0 = expandArray(zk[k], zk[k + 1], 100)
        for i in range(len(z0)):
            if z0[i] in z:
                z0.remove(z0[i])
                break
        Q0 = []
        for i in range(len(z0)):
            Q0.append(S[3])
        if _beam.hasOp():
            nR = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayOp)):
                if _beam.arrayOp[j] < zk[k + 1]:
                    nR.append(j)
            for k1 in range(len(nR)):
                for j in range(len(Q0)):
                    Q0[j] = Q0[j] + S[nR[k1] + 4]

        if _beam.hasP():
            nP = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayP)):
                if _beam.arrayP[j].point < zk[k + 1]:
                    nP.append(j)
            for k1 in range(len(nP)):
                for j in range(len(Q0)):
                    Q0[j] = Q0[j] + _beam.arrayP[nP[k1]].amount
        if _beam.hasQ():
            nQ1 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayQ)):
                if _beam.arrayQ[j].a < zk[k + 1]:
                    nQ1.append(j)
            for k1 in range(len(nQ1)):
                ck = ((_beam.arrayQ[nQ1[k1]].qb - _beam.arrayQ[nQ1[k1]].qa) / (
                    _beam.arrayQ[nQ1[k1]].b - _beam.arrayQ[nQ1[k1]].a))
                for j in range(len(Q0)):
                    Q0[j] = Q0[j] + _beam.arrayQ[nQ1[k1]].qa * (z0[j] - _beam.arrayQ[nQ1[k1]].a) + ck * (z0[j] -
                                                                                                         _beam.arrayQ[
                                                                                                             nQ1[
                                                                                                                 k1]].a) ** 2 / 2 - ck * (
                                                                                                                                             z0[
                                                                                                                                                 j] -
                                                                                                                                             _beam.arrayQ[
                                                                                                                                                 nQ1[
                                                                                                                                                     k1]].b) ** 2 / 2
            nQ2 = []  #promezhutochnie opori sleva ot k
            for j in range(len(_beam.arrayQ) - 1):
                if _beam.arrayQ[j].b < zk[k + 1]:
                    nQ2.append(_beam.arrayQ[j].b)
            for k1 in range(1, len(nQ2) - 1):
                for j in range(0, len(Q0) - 1):
                    Q0[j] = Q0[j] - _beam.arrayQ[nQ2[k1]].qb * (z0[j] - _beam.arrayQ[nQ2[k1]].b)
        Q.extend(Q0)
        z.extend(z0)
    return [z, Q, M, T]


def calc(_beam):
    zk = [0, _beam.length]  #switch points
    for i in _beam.arrayOp:
        if i != "not set":
            zk.append(i)
    for i in _beam.arrayP:
        if i != "not set":
            zk.append(i.point)
    for i in _beam.arrayQ:
        if i != "not set":
            zk.append(i.a)
            zk.append(i.b)
    for i in _beam.arrayM:
        if i != "not set":
            zk.append(i.point)
    zk = list(set(zk))
    nk = len(zk) - 1  #amount of intervals
    neq = 4 + len(_beam.arrayOp)  #amount of equations

    A = []  #000000000000000 neqXneq
    for i in range(0, neq):
        A.append([])
        for j in range(0, neq):
            A[i].append(0.0)
    B = []  #000000000000000000 neq
    for i in range(0, neq):
        B.append(0.0)
    #granichnie uslovia sleva
    if _beam.left == 1:
        A[0][0] = 1.0
        A[1][1] = 1.0
    elif _beam.left == 2:
        A[0][0] = 1.0
        A[1][2] = 1.0
    elif _beam.left == 3:
        A[0][2] = 1.0
        A[1][3] = 1.0

    #granichnie uslovia sprava
    if _beam.right == 1:
        A[2][0] = 1.0
        A[2][1] = _beam.length
        A[2][2] = _beam.length ** 2.0 / 2.0
        A[2][3] = _beam.length ** 3.0 / 6.0
        A[3][1] = 1.0
        A[3][2] = _beam.length
        A[3][3] = _beam.length ** 2.0 / 2.0
        if _beam.hasOp():
            for i in range(0, len(_beam.arrayOp)):
                A[2][4 + i] = (_beam.length - _beam.arrayOp[i]) ** 3.0 / 6.0
                A[3][4 + i] = (_beam.length - _beam.arrayOp[i]) ** 2.0 / 2.0
        if _beam.hasQ():
            for i in range(0, len(_beam.arrayQ)):
                B[2] = B[2] + _beam.arrayQ[i].qa * (_beam.length - _beam.arrayQ[i].a) ** 4.0 / 24.0 - _beam.arrayQ[
                                                                                                          i].qb * (
                                                                                                                      _beam.length -
                                                                                                                      _beam.arrayQ[
                                                                                                                          i].b) ** 4 / 24.0
                B[3] = B[3] + _beam.arrayQ[i].qa * (_beam.length - _beam.arrayQ[i].a) ** 3.0 / 6.0 - _beam.arrayQ[
                                                                                                         i].qb * (
                                                                                                                     _beam.length -
                                                                                                                     _beam.arrayQ[
                                                                                                                         i].b) ** 3 / 6.0
        if _beam.hasP():
            for i in range(0, len(_beam.arrayP)):
                B[2] = B[2] + _beam.arrayP[i].amount * (_beam.length - _beam.arrayP[i].point) ** 3.0 / 6.0
                B[3] = B[3] + _beam.arrayP[i].amount * (_beam.length - _beam.arrayP[i].point) ** 2.0 / 2.0
        if _beam.hasM():
            for i in range(0, len(_beam.arrayM)):
                B[2] = B[2] + _beam.arrayM[i].amount * (_beam.length - _beam.arrayM[i].point) ** 2.0 / 2.0
                B[3] = B[3] + _beam.arrayM[i].amount * (_beam.length - _beam.arrayM[i].point)
    elif _beam.right == 2:
        A[2][0] = 1.0
        A[2][1] = _beam.length
        A[2][2] = _beam.length ** 2 / 2.0
        A[2][3] = _beam.length ** 3 / 6.0
        A[3][2] = 1.0
        A[3][3] = _beam.length
        if _beam.hasOp():
            for i in range(0, len(_beam.arrayOp)):
                A[2][4 + i] = (_beam.length - _beam.arrayOp[i]) ** 3.0 / 6.0
                A[3][4 + i] = (_beam.length - _beam.arrayOp[i])
        if _beam.hasQ():
            for i in range(0, len(_beam.arrayQ)):
                B[2] = B[2] + _beam.arrayQ[i].qa * (_beam.length - _beam.arrayQ[i].a) ** 4.0 / 24.0 - _beam.arrayQ[
                                                                                                          i].qb * (
                                                                                                                      _beam.length -
                                                                                                                      _beam.arrayQ[
                                                                                                                          i].b) ** 4.0 / 24.0
                B[3] = B[3] + _beam.arrayQ[i].qa * (_beam.length - _beam.arrayQ[i].a) ** 2.0 / 2.0 - _beam.arrayQ[
                                                                                                         i].qb * (
                                                                                                                     _beam.length -
                                                                                                                     _beam.arrayQ[
                                                                                                                         i].b) ** 2.0 / 2.0
        if _beam.hasP():
            for i in range(0, len(_beam.arrayP)):
                B[2] = B[2] + _beam.arrayP[i].amount * (_beam.length - _beam.arrayP[i].point) ** 3.0 / 6.0
                B[3] = B[3] + _beam.arrayP[i].amount * (_beam.length - _beam.arrayP[i].point)
        if _beam.hasM():
            for i in range(0, len(_beam.arrayM)):
                B[2] = B[2] + _beam.arrayM[i].amount * (_beam.length - _beam.arrayM[i].point) ** 2.0 / 2.0
                B[3] = B[3] + _beam.arrayM[i].amount
    elif _beam.right == 3:
        A[2][2] = 1.0
        A[2][3] = _beam.length
        A[3][3] = 1.0
        if _beam.hasOp():
            for i in range(0, len(_beam.arrayOp)):
                A[2][4 + i] = (_beam.length - _beam.arrayOp[i])
                A[3][4 + i] = 1
        if _beam.hasQ():
            for i in range(0, len(_beam.arrayQ)):
                B[2] = B[2] + _beam.arrayQ[i].qa * (_beam.length - _beam.arrayQ[i].a) ** 2.0 / 2.0 - _beam.arrayQ[
                                                                                                         i].qb * (
                                                                                                                     _beam.length -
                                                                                                                     _beam.arrayQ[
                                                                                                                         i].b) ** 2.0 / 2.0
                B[3] = B[3] + _beam.arrayQ[i].qa * (_beam.length - _beam.arrayQ[i].a) - _beam.arrayQ[i].qb * (
                    _beam.length - _beam.arrayQ[i].b)
        if _beam.hasP():
            for i in range(0, len(_beam.arrayP)):
                B[2] = B[2] + _beam.arrayP[i].amount * (_beam.length - _beam.arrayP[i].point)
                B[3] = B[3] + _beam.arrayP[i].amount
        if _beam.hasM():
            for i in range(0, len(_beam.arrayM)):
                B[2] = B[2] + _beam.arrayM[i].amount

    #prohodim po oporam
    for i in range(0, len(_beam.arrayOp)):
        A[i + 4][0] = 1.0
        A[i + 4][1] = _beam.arrayOp[i]
        A[i + 4][2] = _beam.arrayOp[i] ** 2.0 / 2.0
        A[i + 4][3] = _beam.arrayOp[i] ** 3.0 / 6.0
        if i > 0:
            for j in range(0, i):
                A[i + 4][j + 4] = (_beam.arrayOp[i] - _beam.arrayOp[j]) ** 3.0 / 6.0
        if _beam.hasM():
            for j in range(0, len(_beam.arrayM)):
                if _beam.arrayM[j].point < _beam.arrayOp[i]:
                    B[i + 4] = B[i + 4] + _beam.arrayM[j].amount * (_beam.arrayOp[i] - _beam.arrayM[
                        j].point) ** 2.0 / 2.0
        if _beam.hasP():
            for j in range(0, len(_beam.arrayP)):
                if _beam.arrayP[j].point < _beam.arrayOp[i]:
                    B[i + 4] = B[i + 4] + _beam.arrayP[j].amount * (_beam.arrayOp[i] - _beam.arrayP[
                        j].point) ** 3.0 / 6.0
        if _beam.hasQ():
            for j in range(0, len(_beam.arrayQ)):
                if _beam.arrayQ[j].a < _beam.arrayOp[i]:
                    B[i + 4] = B[i + 4] + _beam.arrayQ[j].qa * (_beam.arrayOp[i] - _beam.arrayQ[j].a) ** 4.0 / 24.0
                if _beam.arrayQ[j].b < _beam.arrayOp[i]:
                    B[i + 4] = B[i + 4] - _beam.arrayQ[j].qb * (_beam.arrayOp[i] - _beam.arrayQ[j].b) ** 4.0 / 24.0
    #reshaem sistemu matrichnim sposobom X=A^-1*B

    x = np.solve(A, B)
    tmp = x.tolist()
    for i in range(len(tmp)):
        tmp[i] = tmp[i] * (-1)

    """print '---------------------'
    print 'equasion solved, solution:'
    print tmp
    print '---------------------'"""
    return [tmp, zk, neq, nk]
