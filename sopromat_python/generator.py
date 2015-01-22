# -------------------------------------------------------------------------------
# Name:         Generator
# Version:      0.1
#
# Author:       Richter
#
# Created:      5/1/2013
# -------------------------------------------------------------------------------


from decimal import *
getcontext().prec = 4

import random as rnd
import sopromat_python.classes
import decimal


def generateLocation(amount, length):
    print("generateLocation(", amount, ",", length, "): call")
    temp = []
    for i in range(amount):
        temp.append(rnd.randrange(1, length))
    while len(list(set(temp))) != len(temp):
        temp = list(set(temp))
        temp.append(rnd.randrange(1, length))
    return sorted(list(set(temp)))


def generateValue():
    temp = rnd.randrange(-50, 50)
    while temp == 0:
        temp = rnd.randrange(-50, 50)
    return temp


def generateQ():
    temp = rnd.randrange(-50, 50)
    while temp == 0:
        temp = rnd.randrange(-50, 50)
    temp2 = 0
    if temp > 0:
        temp2 = rnd.randrange(0, 50)
    if temp < 0:
        temp2 = rnd.randrange(-50, 0)
    return [temp, temp2]


def generateBeam():
    print("generateBeam(): call")
    beam = sopromat_python.classes.Beam(rnd.randrange(10, 20), rnd.randrange(1, 3), rnd.randrange(2, 4))
    print("generateBeam(): generated beam")
    print("generateBeam(): beam params: ")
    print("generateBeam(): length = ", str(beam.length))
    print("generateBeam(): left_type = ", str(beam.left))
    print("generateBeam(): right_type = ", str(beam.right))
    opam = rnd.randrange(1, 4)
    mam = rnd.randrange(1, 4)
    qam = rnd.randrange(1, 4)
    pam = rnd.randrange(1, 4)
    print("generateBeam(): generating beam params")
    if opam != 0:
        temp = generateLocation(opam, beam.length)
        for i in range(len(temp)):
            beam.addOp(temp[i])
    if mam != 0:
        temp = generateLocation(mam, beam.length)
        for i in range(len(temp)):
            beam.addM(sopromat_python.classes.M(temp[i], generateValue()))
    if pam != 0:
        temp = generateLocation(pam, beam.length)
        for i in range(len(temp)):
            beam.addP(sopromat_python.classes.P(temp[i], generateValue()))
    if qam != 0:
        temp = generateLocation(qam, beam.length - 1)
        val = generateQ()
        for i in range(len(temp)):
            beam.addQ(sopromat_python.classes.Q(temp[i], rnd.randrange(temp[i] + 1, beam.length), val[0], val[1]))
    print("generateBeam(): generated")
    return beam


def generateSector(amount, length):
    print("generateSector(): call")
    temp = []
    temp.append(
        sopromat_python.classes.Sector(0, rnd.randrange(1, length / amount), rnd.randrange(1, 10), rnd.randrange(1, 5)))
    for i in range(amount - 2):
        temp.append(
            sopromat_python.classes.Sector(temp[i].length2, rnd.randrange(temp[i].length2 + 1,
                                                                          (length - temp[i].length2) / (
                                                                              amount - i - 2)),
                                           rnd.randrange(1, 10), rnd.randrange(1, 5)))
    temp.append(
        sopromat_python.classes.Sector(temp[len(temp) - 1].length2, length, rnd.randrange(1, 10), rnd.randrange(1, 5)))
    return temp


def generateBeam2():
    print("generateBeam2(): call")
    beam = sopromat_python.classes.Beam2(rnd.randrange(10, 20))
    print("generateBeam2(): generated beam")
    print("generateBeam2(): beam params: ")
    print("generateBeam2(): length = ", str(beam.length))
    secam = rnd.randrange(1, 5)
    qam = rnd.randrange(1, 4)
    pam = rnd.randrange(1, 4)
    print("generateBeam2(): generating beam params")
    if secam != 0:
        beam.arraySec = generateSector(secam, beam.length)
    if pam != 0:
        temp = generateLocation(pam, beam.length)
        for i in range(len(temp)):
            beam.addP(sopromat_python.classes.P(temp[i], generateValue()))
    if qam != 0:
        temp = generateLocation(qam, beam.length - 1)
        for i in range(len(temp)):
            val = generateValue()
            beam.addQ(sopromat_python.classes.Q(temp[i], rnd.randrange(temp[i] + 1, beam.length), val, val))
    print("generateBeam2(): generated")
    return beam


def generateBeam3():
    print("generateBeam3(): call")
    beam = sopromat_python.classes.Beam3(rnd.randrange(10, 20))
    secam = rnd.randrange(1, 4)
    mam = rnd.randrange(1, 4)
    Mam = rnd.randrange(1, 4)

    if secam != 0:
        beam.arraySec = generateSector(secam, beam.length)
    if Mam != 0:
        temp = generateLocation(Mam, beam.length)
        for i in range(len(temp)):
            beam.addM(sopromat_python.classes.M(temp[i], generateValue()))
    if mam != 0:
        temp = generateLocation(mam, beam.length - 1)
        for i in range(len(temp)):
            val = generateValue()
            beam.addm(sopromat_python.classes.Q(temp[i], rnd.randrange(temp[i] + 1, beam.length), val, val))
    print(beam.getSec())
    return beam


def generateInertia():
    print("generateInertia(): call")
    data = {}
    data['type'] = rnd.randrange(1, 15)
    print("generateInertia(): data['type']=", data['type'])
    if data['type'] == 1:
        data['r'] = round((rnd.uniform(0.5, 5.0)), 2)
        data['answerx'] = 3.1415 * (data['r'] ** 4.0) / 4.0
        data['answery'] = 3.1415 * (data['r'] ** 4.0) / 4.0
        data['text'] = "<br/>Найти осевые моменты инерции для круга с радиусом r=" + str(
            data['r']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 2:
        data['r'] = round((rnd.uniform(0.5, 5.0)), 2)
        data['d'] = round((rnd.uniform(0.1, data['r'])), 2)
        data['answerx'] = 3.1415 * ((data['r'] * 2.0) ** 4.0 - data['d'] ** 4.0) / 64.0
        data['answery'] = 3.1415 * ((data['r'] * 2.0) ** 4.0 - data['d'] ** 4.0) / 64.0
        data['text'] = "<br/>Найти осевые моменты инерции для кольца с параметрами: r=" + str(
            data['r']) + ", d1=" + str(
            data['d']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 3:
        data['s'] = round((rnd.uniform(0.1, 1.0)), 2)
        data['d'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['answerx'] = (3.1415 * (data['d'] ** 3.0) * data['s']) / 8.0
        data['answery'] = (3.1415 * (data['d'] ** 3.0) * data['s']) / 8.0
        data['text'] = "<br/>Найти осевые моменты инерции для тонкостенного кольца с параметрами: d=" + str(
            data['d']) + ", s=" + str(data['s']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 4:
        data['d'] = round((rnd.uniform(0.1, 5.0)), 2)
        data['answerx'] = 0.00686 * (data['d']) ** 4.0
        data['answery'] = 3.1415 * (data['d'] ** 4.0) / 128.0
        data['text'] = "<br/>Найти осевые моменты инерции для полукруга с параметрами: d=" + str(
            data['d']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 5:
        data['a'] = round((rnd.uniform(0.1, 5.0)), 2)
        data['b'] = round((rnd.uniform(0.1, 5.0)), 2)
        data['answerx'] = (3.1415 * (data['b'] ** 3.0) * data['a']) / 4.0
        data['answery'] = (3.1415 * (data['a'] ** 3.0) * data['b']) / 4.0
        data['text'] = "<br/>Найти осевые моменты инерции для эллипса с параметрами: a=" + str(
            data['a']) + ", b=" + str(
            data['b']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 6:
        data['a'] = round((rnd.uniform(0.1, 5.0)), 2)
        data['answerx'] = (data['a'] ** 4.0) / 12.0
        data['answery'] = (data['a'] ** 4.0) / 12.0
        data['text'] = "<br/>Найти осевые моменты инерции для квадрата с параметрами: a=" + str(
            data['a']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 7:
        data['b1'] = round((rnd.uniform(0.1, 1.0)), 2)
        data['b'] = round((rnd.uniform(data['b1'], 5.0)), 2)
        data['answerx'] = ((data['b'] ** 4.0) - (data['b1'] ** 4.0)) / 12.0
        data['answery'] = ((data['b'] ** 4.0) - (data['b1'] ** 4.0)) / 12.0
        data['text'] = "<br/>Найти осевые моменты инерции для полого квадрата с параметрами: b=" + str(
            data['b']) + ", b1=" + str(data['b1']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 8:
        data['s'] = round((rnd.uniform(0.1, 1.0)), 2)
        data['b'] = round((rnd.uniform(3.0, 5.0)), 2)
        data['answerx'] = (2.0 / 3.0) * data['s'] * data['b'] ** 3.0
        data['answery'] = (2.0 / 3.0) * data['s'] * data['b'] ** 3.0
        data['text'] = "<br/>Найти осевые моменты инерции для полого тонкостенного квадрата с параметрами: b=" + str(
            data['b']) + ", s=" + str(data['s']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 9:
        data['a'] = round((rnd.uniform(0.1, 5.0)), 2)
        data['b'] = round((rnd.uniform(0.2, 5.0)), 2)
        data['answerx'] = ((data['a'] ** 3.0) * data['b']) / 12.0
        data['answery'] = ((data['b'] ** 3.0) * data['a']) / 12.0
        data['text'] = "<br/>Найти осевые моменты инерции для прямоугольника с параметрами: a=" + str(
            data['a']) + ", b=" + str(data['b']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 10:
        data['a'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['b'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['a1'] = round((rnd.uniform(0.1, data['a'])), 2)
        data['b1'] = round((rnd.uniform(0.1, data['b'])), 2)
        data['answerx'] = ((data['a'] ** 3.0) * data['b'] - (data['a1'] ** 3.0) * data['b1']) / 12.0
        data['answery'] = ((data['b'] ** 3.0) * data['a'] - (data['b1'] ** 3.0) * data['a1']) / 12.0
        data['text'] = "<br/>Найти осевые моменты инерции для полого прямоугольника с параметрами: a=" + str(
            data['a']) + ", b=" + str(data['b']) + ", a1=" + str(data['a1']) + ", b1=" + str(
            data['b1']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 11:
        data['b'] = round((rnd.uniform(0.5, 1.0)), 2)
        data['h'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['s'] = round((rnd.uniform(0.1, data['h'] - 0.1)), 2)
        data['answerx'] = (data['s'] * (data['h'] ** 3.0) / 6.0) * (3.0 * (data['b'] / data['h']) + 1.0)
        data['answery'] = (data['s'] * (data['b'] ** 3.0) / 6.0) * (3.0 * (data['h'] / data['b']) + 1.0)
        data[
            'text'] = "<br/>Найти осевые моменты инерции для полого тонкостенного прямоугольника с параметрами: b=" + str(
            data['b']) + ", h=" + str(data['h']) + ", s=" + str(
            data['s']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 12:
        data['b1'] = round((rnd.uniform(0.5, 1.0)), 2)
        data['h1'] = round((rnd.uniform(0.5, 1.0)), 2)
        data['h'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['b'] = round((rnd.uniform(1.0, 5.0)), 2)
        y = (data['b'] * data['h1'] ** 2 + data['b1'] * data['h'] * (2 * data['h1'] + data['h'])) / (
            2 * (data['b'] * data['h1'] + data['b1'] * data['h']))
        data['answerx'] = (data['b'] * data['h1'] ** 3 + 2 * data['b1'] * data['h'] ** 3) / 12.0 + data['b'] * data[
            'h1'] * (y - data['h1'] / 2.0) ** 2 + 2.0 * data['b1'] * data['h'] * (data['h'] / 2.0 + data['h1'] - y) ** 2
        data['answery'] = (data['h1'] * data['b'] ** 3 + data['h'] * data['b1'] ** 3) / 12.0
        data['text'] = "<br/>Найти осевые моменты инерции для тавра с параметрами: b=" + str(data['b']) + ", b1=" + str(
            data['b1']) + ", h=" + str(data['h']) + ", h1=" + str(
            data['h1']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 13:
        data['b1'] = round((rnd.uniform(0.5, 1.0)), 2)
        data['h1'] = round((rnd.uniform(0.5, 1.0)), 2)
        data['h'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['b'] = round((rnd.uniform(1.0, 5.0)), 2)
        y = (data['b'] * data['h1'] ** 2 + data['b1'] * data['h'] * (2 * data['h1'] + data['h'])) / (
            2 * (data['b'] * data['h1'] + data['b1'] * data['h']))
        data['answerx'] = (data['b'] * data['h1'] ** 3 + 2 * data['b1'] * data['h'] ** 3) / 12.0 + data['b'] * data[
            'h1'] * (y - data['h1'] / 2.0) ** 2 + 2.0 * data['b1'] * data['h'] * (data['h'] / 2.0 + data['h1'] - y) ** 2
        data['answery'] = ((data['h'] + data['h1']) * data['b'] ** 3 - data['h'] * (
            data['b'] - 2.0 * data['b1']) ** 3) / 12.0
        data['text'] = "<br/>Найти осевые моменты инерции корытного сечения с параметрами: b=" + str(
            data['b']) + ", b1=" + str(data['b1']) + ", h=" + str(data['h']) + ", h1=" + str(
            data['h1']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    elif data['type'] == 14:
        data['b1'] = round((rnd.uniform(0.5, 1.0)), 2)
        data['h1'] = round((rnd.uniform(0.5, 1.0)), 2)
        data['h'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['b'] = round((rnd.uniform(1.0, 5.0)), 2)
        data['answerx'] = (data['b1'] * data['h'] ** 3 + (data['b'] - data['b1']) * data['h'] ** 3) / 12.0
        data['answery'] = (data['h1'] * data['b'] ** 3 + (data['h'] - data['h1']) * data['b1'] ** 3) / 12.0
        data['text'] = "<br/>Найти осевые моменты инерции крестообразного сечения с параметрами: b=" + str(
            data['b']) + ", b1=" + str(data['b1']) + ", h=" + str(data['h']) + ", h1=" + str(
            data['h1']) + "<br/> Точность ответа: Eps=0.000001, ввиду погрешности измерения"
    print(type(data))
    return data












