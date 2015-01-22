# -------------------------------------------------------------------------------
# Name:         Beam
# Version:      0.4
#
# Author:       Richter
#
# Created:      31/12/2013
# python 2.7 numpy 1.8
#-------------------------------------------------------------------------------

from decimal import *
getcontext().prec = 4
import random
import numpy as np
from PIL import Image, ImageDraw
#coding=utf-8
class Drawing:
    def drawOp(self, drawer, p, num):
        print("Drawing.drawOp(): call")
        drawer.text((p + 10, 111), str(num), fill="black")
        drawer.line((p, 110, p + 10, 100), fill="black")
        drawer.line((p + 10, 100, p + 20, 110), fill="black")
        drawer.line((p + 20, 110, p, 110), fill="black")

    def drawP(self, drawer, p, mom, num):
        print("Drawing.drawP(): call")
        m = 0
        if mom < 0:
            m = 4
        else:
            m = 4
        drawer.line((p + 10, 100, p + 10, 100 - m * 10), fill="green")
        drawer.text((p + 15, 95 - m * 10), "P_" + str(num), fill="black")

        if mom < 0:
            drawer.line((p + 10, 100, p + 5, 100 - 5), fill="green")
            drawer.line((p + 10, 100, p + 15, 100 - 5), fill="green")
        else:
            drawer.line((p + 10, 100 - m * 10, p + 5, 100 - m * 10 + 5), fill="green")
            drawer.line((p + 10, 100 - m * 10, p + 15, 100 - m * 10 + 5), fill="green")

    def drawM(self, drawer, p, mom, num):
        print("Drawing.drawM(): call")
        m = 0
        if mom > 0:
            m = 5
        else:
            m = -5
        drawer.line((p + 10, 100 + m * 10, p + 10, 100 - m * 10), fill="red")
        if m > 0:
            drawer.text((p, 80 - m * 10), "M_" + str(num), fill="black")
        else:
            drawer.text((p, 80 + m * 10), "M_" + str(num), fill="black")
        if m < 0:
            drawer.line((p, 100 + m * 10, p + 10, 100 + m * 10), fill="red")
            drawer.line((p + 5, 105 + m * 10, p, 100 + m * 10), fill="red")
            drawer.line((p + 5, 95 + m * 10, p, 100 + m * 10), fill="red")
            drawer.line((p + 10, 100 - m * 10, p + 20, 100 - m * 10), fill="red")
            drawer.line((p + 20, 100 - m * 10, p + 15, 105 - m * 10), fill="red")
            drawer.line((p + 20, 100 - m * 10, p + 15, 95 - m * 10), fill="red")
        else:
            drawer.line((p + 10, 100 - m * 10, p + 20, 100 - m * 10), fill="red")
            drawer.line((p + 20, 100 - m * 10, p + 15, 95 - m * 10), fill="red")
            drawer.line((p + 20, 100 - m * 10, p + 15, 105 - m * 10), fill="red")
            drawer.line((p + 10, 100 + m * 10, p, 100 + m * 10), fill="red")
            drawer.line((p, 100 + m * 10, p + 5, 95 + m * 10), fill="red")
            drawer.line((p, 100 + m * 10, p + 5, 105 + m * 10), fill="red")

    def drawQ(self, drawer, p1, p2, qq1, qq2, num):
        print("Drawing.drawQ(): call")
        q1 = 0
        q2 = 0
        if np.fabs(qq1) > 10:
            q1 = qq1 / 10.0
        if np.fabs(qq2) > 10:
            q2 = qq2 / 10.0
        drawer.line((p1 + 10, 100, p1 + 10, 100 + q1 * 10), fill="blue")
        if q1 > 0 or q2 > 0:
            drawer.line((p1 + 10, 100, p1 + 5, 105), fill="blue")
            drawer.line((p1 + 10, 100, p1 + 15, 105), fill="blue")
            drawer.line((p2 + 10, 100, p2 + 15, 105), fill="blue")
            drawer.line((p2 + 10, 100, p2 + 5, 105), fill="blue")
        if q1 < 0 or q2 < 0:
            drawer.line((p1 + 10, 100, p1 + 5, 95), fill="blue")
            drawer.line((p1 + 10, 100, p1 + 15, 95), fill="blue")
            drawer.line((p2 + 10, 100, p2 + 15, 95), fill="blue")
            drawer.line((p2 + 10, 100, p2 + 5, 95), fill="blue")
        drawer.line((p2 + 10, 100, p2 + 10, 100 + q2 * 10), fill="blue")
        drawer.line((p1 + 10, 100 + q1 * 10, p2 + 10, 100 + q2 * 10), fill="blue")

        if q2 > q1:
            if q2 < 0:
                drawer.text((p2 + 30, 100 + q2 * 10), "q_" + str(num), fill="black")
            else:
                drawer.text((p2 + 30, 100 + q2 * 10), "q_" + str(num), fill="black")
        else:
            if q1 < 0:
                drawer.text((p1 - 10, 100 + q1 * 10), "q_" + str(num), fill="black")
            else:
                drawer.text((p1 - 10, 100 + q1 * 10), "q_" + str(num), fill="black")

    def drawBeam(self, beam, taskid):
        print("Drawing.drawBeam(): call")
        temp = Image.new("RGB", (500, 250), "white")
        drawer = ImageDraw.Draw(temp)
        #draw  balka
        if beam.left == 1:
            drawer.line((10, 50, 10, 150), fill="black", width=2)
        else:
            drawer.line((0, 110, 10, 100), fill="black")
            drawer.line((10, 100, 20, 110), fill="black")
            drawer.line((20, 110, 0, 110), fill="black")
        if beam.right == 2:
            drawer.line((390, 110, 400, 100), fill="black")
            drawer.line((400, 100, 410, 110), fill="black")
            drawer.line((410, 110, 390, 110), fill="black")
        drawer.line((10, 100, 400, 100), fill="black", width=2)
        for i in range(len(beam.arrayM)):
            if beam.arrayM[0] == 'not set':
                return
            self.drawM(drawer, beam.arrayM[i].point * 400 / beam.length, beam.arrayM[i].amount, i + 1)
            for i in range(len(list(set(beam.arrayOp)))):
                if beam.arrayOp[0] == 'not set':
                    return
                self.drawOp(drawer, beam.arrayOp[i] * 400 / beam.length, i + 1)
            for i in range(len(beam.arrayP)):
                if beam.arrayP[0] == 'not set':
                    return
                self.drawP(drawer, beam.arrayP[i].point * 400 / beam.length, beam.arrayP[i].amount, i + 1)
            for i in range(len(beam.arrayQ)):
                if beam.arrayQ[0] == 'not set':
                    return
                self.drawQ(drawer, beam.arrayQ[i].a * 400 / beam.length, beam.arrayQ[i].b * 400 / beam.length,
                beam.arrayQ[i].qa, beam.arrayQ[i].qb, i + 1)
        del drawer
        return temp


    def drawBeam2(self, beam, taskid):
        print("Drawing.drawBeam2(): call")
        temp = Image.new("RGB", (500, 250), "white")
        drawer = ImageDraw.Draw(temp)
        #draw  balka
        drawer.line((10, 50, 10, 150), fill="black", width=2)
        drawer.line((10, 100, 450, 100), fill="black", width=2)
        drawer.line((450, 100, 440, 90), fill="black", width=2)
        drawer.line((450, 100, 440, 110), fill="black", width=2)
        drawer.line((10, 100 - 10 * beam.arraySec[0].heigth, 10, 100 + 10 * beam.arraySec[0].heigth), fill="black")
        drawer.line((10, 100 - 10 * beam.arraySec[0].heigth, 10 + beam.arraySec[0].length2 * 400 / beam.length,
                     100 - 10 * beam.arraySec[0].heigth2), fill="black")
        drawer.line((10, 100 + 10 * beam.arraySec[0].heigth, 10 + beam.arraySec[0].length2 * 400 / beam.length,
                     100 + 10 * beam.arraySec[0].heigth2), fill="black")
        drawer.line((10 + beam.arraySec[0].length2 * 400 / beam.length, 100 - 10 * beam.arraySec[0].heigth2,
                     10 + beam.arraySec[0].length2 * 400 / beam.length, 100 + 10 * beam.arraySec[0].heigth2), fill="black")
        drawer.text((10 + beam.arraySec[0].length2 * 400 / beam.length, 20), "" + str(1), fill="black")
        for i in range(1, len(beam.arraySec)):
            drawer.line((10 + beam.arraySec[i].length * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth,
                         10 + beam.arraySec[i].length * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth), fill="black")
            drawer.line((10 + beam.arraySec[i].length * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth,
                 10 + beam.arraySec[i].length2 * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth2), fill="black")
            drawer.line((10 + beam.arraySec[i].length * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth,
                 10 + beam.arraySec[i].length2 * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth2), fill="black")
            drawer.line((10 + beam.arraySec[i].length2 * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth2,
                 10 + beam.arraySec[i].length2 * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth2), fill="black")
            drawer.text((10 + beam.arraySec[i].length2 * 400 / beam.length, 20), "" + str(i + 1), fill="black")
        for i in range(len(beam.arrayP)):
            if beam.arrayP[0] == 'not set':
                return
            if beam.arrayP[i].amount > 0:
                drawer.line((10 + beam.arrayP[i].point * 400 / beam.length, 100,
                 10 + beam.arrayP[i].point * 400 / beam.length + beam.arrayP[i].amount, 100), width=2, fill="red")
                drawer.text((10 + beam.arrayP[i].point * 400 / beam.length + beam.arrayP[i].amount, 75), "P_" + str(i + 1),
                fill="black")
                drawer.line((10 + beam.arrayP[i].point * 400 / beam.length + beam.arrayP[i].amount, 100,
                 beam.arrayP[i].point * 400 / beam.length + beam.arrayP[i].amount, 90), width=2, fill="red")
                drawer.line((10 + beam.arrayP[i].point * 400 / beam.length + beam.arrayP[i].amount, 100,
                 beam.arrayP[i].point * 400 / beam.length + beam.arrayP[i].amount, 110), width=2, fill="red")
            if beam.arrayP[i].amount < 0:
                drawer.line((10 + beam.arrayP[i].point * 400 / beam.length, 100,
                 10 + beam.arrayP[i].point * 400 / beam.length - beam.arrayP[i].amount, 100), width=2, fill="red")
                drawer.text((10 + beam.arrayP[i].point * 400 / beam.length - beam.arrayP[i].amount, 75), "P_" + str(i + 1),
                fill="black")
                drawer.line((10 + beam.arrayP[i].point * 400 / beam.length, 100, 20 + beam.arrayP[i].point * 400 / beam.length, 90),
                width=2, fill="red")
                drawer.line(
                    (10 + beam.arrayP[i].point * 400 / beam.length, 100, 20 + beam.arrayP[i].point * 400 / beam.length, 110),
                        width=2, fill="red")
        for i in range(len(beam.arrayQ)):
            if beam.arrayQ[0] == 'not set':
                return
            if beam.arrayQ[i].qa > 0:
                drawer.line((10 + beam.arrayQ[i].a * 400 / beam.length, 100,
                    10 + beam.arrayQ[i].b * 400 / beam.length + beam.arrayQ[i].qa, 100), fill="blue")
                drawer.text((beam.arrayQ[i].b * 400 / beam.length + beam.arrayQ[i].qa, 115), "Q_" + str(i + 1), fill="black")
                drawer.line((10 + beam.arrayQ[i].b * 400 / beam.length + beam.arrayQ[i].qa, 100,
                    beam.arrayQ[i].b * 400 / beam.length + beam.arrayQ[i].qa, 90), fill="blue")
                drawer.line((10 + beam.arrayQ[i].b * 400 / beam.length + beam.arrayQ[i].qa, 100,
                        beam.arrayQ[i].b * 400 / beam.length + beam.arrayQ[i].qa, 110), fill="blue")
            if beam.arrayQ[i].qa < 0:
                drawer.line((10 + beam.arrayQ[i].a * 400 / beam.length, 100,
                         10 + beam.arrayQ[i].b * 400 / beam.length - beam.arrayQ[i].qa, 100), fill="blue")
                drawer.text((beam.arrayQ[i].b * 400 / beam.length + beam.arrayQ[i].qa, 115), "Q_" + str(i + 1), fill="black")
                drawer.line((10 + beam.arrayQ[i].a * 400 / beam.length, 100, 20 + beam.arrayQ[i].a * 400 / beam.length, 90),
                        fill="blue")
                drawer.line((10 + beam.arrayQ[i].a * 400 / beam.length, 100, 20 + beam.arrayQ[i].a * 400 / beam.length, 110),
                        fill="blue")
        del drawer
        return temp


    def drawBeam3(self, beam, taskid):
        print("Drawing.drawBeam3(): call")
        temp = Image.new("RGB", (500, 250), "white")
        drawer = ImageDraw.Draw(temp)
        #draw  balka
        drawer.line((10, 50, 10, 150), fill="black", width=2)
        drawer.line((10, 100, 450, 100), fill="black", width=2)
        drawer.line((450, 100, 440, 90), fill="black", width=2)
        drawer.line((450, 100, 440, 110), fill="black", width=2)
        drawer.line((10, 100 - 10 * beam.arraySec[0].heigth, 10, 100 + 10 * beam.arraySec[0].heigth), fill="black")
        drawer.line((10, 100 - 10 * beam.arraySec[0].heigth, 10 + beam.arraySec[0].length2 * 400 / beam.length,
                     100 - 10 * beam.arraySec[0].heigth2), fill="black")
        drawer.line((10, 100 + 10 * beam.arraySec[0].heigth, 10 + beam.arraySec[0].length2 * 400 / beam.length,
                     100 + 10 * beam.arraySec[0].heigth2), fill="black")
        drawer.line((10 + beam.arraySec[0].length2 * 400 / beam.length, 100 - 10 * beam.arraySec[0].heigth2,
                     10 + beam.arraySec[0].length2 * 400 / beam.length, 100 + 10 * beam.arraySec[0].heigth2), fill="black")
        drawer.text((10 + beam.arraySec[0].length2 * 400 / beam.length, 20), "" + str(1), fill="black")
        for i in range(1, len(beam.arraySec)):
            drawer.line((10 + beam.arraySec[i].length * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth,
                         10 + beam.arraySec[i].length * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth), fill="black")
            drawer.line((10 + beam.arraySec[i].length * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth,
                         10 + beam.arraySec[i].length2 * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth2), fill="black")
            drawer.line((10 + beam.arraySec[i].length * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth,
                         10 + beam.arraySec[i].length2 * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth2), fill="black")
            drawer.line((10 + beam.arraySec[i].length2 * 400 / beam.length, 100 - 10 * beam.arraySec[i].heigth2,
                         10 + beam.arraySec[i].length2 * 400 / beam.length, 100 + 10 * beam.arraySec[i].heigth2), fill="black")
            drawer.text((10 + beam.arraySec[i].length2 * 400 / beam.length, 20), "" + str(i + 1), fill="black")
        heigth = []
        zk2 = []
        for i in beam.arraySec:
            if i != "not set":
                heigth.append(i.heigth)
                heigth.append(i.heigth2)
                zk2.append(i.length)
                zk2.append(i.length2)
        for i in range(len(beam.arrayM)):
            if beam.arrayM[0] == 'not set':
                return
        d = 0
        for j in range(len(heigth) - 1):
            if beam.arrayM[i].point > zk2[j] and beam.arrayM[i].point < zk2[j + 1] and zk2[j + 1] != zk2[j]:
                d = (heigth[j + 1] - heigth[j]) * ((beam.arrayM[i].point - zk2[j]) / (zk2[j + 1] - zk2[j])) + heigth[j]
                break
            if beam.arrayM[i].point > zk2[j] and beam.arrayM[i].point < zk2[j + 1] and zk2[j + 1] == zk2[j]:
                d = heigth[j] ** 2 / 4.0
                break
            if beam.arrayM[i].point == zk2[j]:
                d = heigth[j] ** 2 / 4.0
                break
            if beam.arrayM[i].point == zk2[j + 1]:
                d = heigth[j + 1] ** 2 / 4.0
                break
            if beam.arrayM[i].amount < 0:
                drawer.ellipse((5 + beam.arrayM[i].point * 400 / beam.length, 105 - d * 10,
                    15 + beam.arrayM[i].point * 400 / beam.length, 95 - d * 10), fill="blue")
                drawer.text((10 + beam.arrayM[i].point * 400 / beam.length, 105 + d * 10 + 2), "M_" + str(i + 1), fill="black")
                drawer.line((5 + beam.arrayM[i].point * 400 / beam.length, 100 - d * 10, 15 + beam.arrayM[i].point * 400 / beam.length,
                    100 - d * 10), width=2, fill="blue")
                drawer.line((10 + beam.arrayM[i].point * 400 / beam.length, 105 - d * 10, 10 + beam.arrayM[i].point * 400 / beam.length,
                    95 - d * 10), width=2, fill="blue")
                drawer.ellipse((
                    5 + beam.arrayM[i].point * 400 / beam.length, 95 + d * 10, 15 + beam.arrayM[i].point * 400 / beam.length,
                        105 + d * 10), fill="blue")
                drawer.point((10 + beam.arrayM[i].point * 400 / beam.length, 100 + d * 10), fill="blue")
            if beam.arrayM[i].amount > 0:
                drawer.ellipse((5 + beam.arrayM[i].point * 400 / beam.length, 105 + d * 10,
                    15 + beam.arrayM[i].point * 400 / beam.length, 95 + d * 10), fill="blue")
                drawer.text((5 + beam.arrayM[i].point * 400 / beam.length, 105 + d * 10 + 2), "M_" + str(i + 1), fill="black")
                drawer.line((5 + beam.arrayM[i].point * 400 / beam.length, 100 + d * 10,
                     15 + beam.arrayM[i].point * 400 / beam.length, 100 + d * 10), width=2, fill="blue")
                drawer.line((10 + beam.arrayM[i].point * 400 / beam.length, 105 + d * 10,
                     10 + beam.arrayM[i].point * 400 / beam.length, 95 + d * 10), width=2, fill="blue")
                drawer.ellipse((5 + beam.arrayM[i].point * 400 / beam.length, 95 - d * 10,
                        15 + beam.arrayM[i].point * 400 / beam.length, 105 - d * 10), fill="blue")
                drawer.point((10 + beam.arrayM[i].point * 400 / beam.length, 100 - d * 10), fill="blue")
        for i in range(len(beam.arraym)):
            if beam.arraym[0] == 'not set':
                return
        d1 = 0
        for j in range(len(heigth) - 1):
            if beam.arraym[i].a > zk2[j] and beam.arraym[i].a < zk2[j + 1] and zk2[j + 1] != zk2[j]:
                d1 = (heigth[j + 1] - heigth[j]) * ((beam.arraym[i].a - zk2[j]) / (zk2[j + 1] - zk2[j])) + heigth[j]
                break
            if beam.arraym[i].a > zk2[j] and beam.arraym[i].a < zk2[j + 1] and zk2[j + 1] == zk2[j]:
                d1 = heigth[j] ** 2 / 4.0
                break
            if beam.arraym[i].a == zk2[j]:
                d1 = heigth[j] ** 2 / 4.0
                break
            if beam.arraym[i].a == zk2[j + 1]:
                d1 = heigth[j + 1] ** 2 / 4.0
                break
        p = []
        h = []

        for j in range(5):
            p.append(beam.arraym[i].a + (beam.arraym[i].b - beam.arraym[i].a) * j / 5.0)
            h.append(d1 - 10)
            if beam.arraym[i].qa < 0:
                drawer.ellipse((5 + p[j] * 400 / beam.length, 105 - 10 * h[j], 15 + p[j] * 400 / beam.length, 95 - 10 * h[j]),
                       fill="red")
                drawer.line((5 + p[j] * 400 / beam.length, 100 - 10 * h[j], 15 + p[j] * 400 / beam.length, 100 - 10 * h[j]),
                    width=2, fill="red")
                drawer.line((10 + p[j] * 400 / beam.length, 105 - 10 * h[j], 10 + p[j] * 400 / beam.length, 95 - 10 * h[j]),
                    width=2, fill="red")
                drawer.ellipse((5 + p[j] * 400 / beam.length, 95 + 10 * h[j], 15 + p[j] * 400 / beam.length, 105 + 10 * h[j]),
                   fill="red")
                drawer.point((10 + p[j] * 400 / beam.length, 100 + 10 * h[j]), fill="red")
            if beam.arraym[i].qa > 0:
                drawer.ellipse((5 + p[j] * 400 / beam.length, 105 + 10 * h[j], 15 + p[j] * 400 / beam.length, 95 + 10 * h[j]),
                       fill="red")
                drawer.line((5 + p[j] * 400 / beam.length, 100 + 10 * h[j], 15 + p[j] * 400 / beam.length, 100 + 10 * h[j]),
                    width=2, fill="red")
                drawer.line((10 + p[j] * 400 / beam.length, 105 + 10 * h[j], 10 + p[j] * 400 / beam.length, 95 + 10 * h[j]),
                    width=2, fill="red")
                drawer.ellipse((5 + p[j] * 400 / beam.length, 95 - 10 * h[j], 15 + p[j] * 400 / beam.length, 105 - 10 * h[j]),
                       fill="red")
                drawer.point((10 + p[j] * 400 / beam.length, 100 - 10 * h[j]), fill="red")
                drawer.text((10 + p[0] * 400 / beam.length, 95 - 10 * abs(h[0]) - 10), "m_" + str(i + 1), fill="black")
        del drawer
        return temp

from .generator import generateBeam,generateInertia,generateBeam2,generateBeam3
from .maths import getQMT,getNLS,getMTS
class BeamTask:  # this class is specifically for trac plugin
    def __init__(self):
        print("BeamTask.__init__(): call")
        self.beam = None
        self.answerQ = 0
        self.answerM = 0
        self.text = "none so far"

    def generate(self):
        print("BeamTask.generate(): call")
        self.beam = generateBeam()
        print("generate():ok")
        left = ""
        right = ""
        if self.beam.left == 1:
            left = "жесткая заделка"
        elif self.beam.left == 2:
            left = "шарнир"
        if self.beam.right == 2:
            right = "шарнир"
        else:
            right = "свободный край"
        self.text = "<br/>Параметры балки:<br/>Длина = " + str(
            self.beam.length) + " м., слева: " + left + ", справа: " + right + "<br/>Ось Oy направлена вверх.<br/>" + "<br/>" + self.beam.getP() + "<br/>" + self.beam.getQ() + "<br/>" + self.beam.getM() + "<br/>" + self.beam.getOp()

    def solve(self):
        print("BeamTask.solve(): call")
        solution = getQMT(self.beam)
        x = solution[0]
        Qx = solution[1]
        Mx = solution[2]
        rnd = random.randrange(len(x))
        self.answerM = round(Mx[rnd], 2)
        self.answerQ = round(Qx[rnd], 2)
        self.text = self.text + "<br/>Найти Qx и Mx в точке: " + str(
            round(x[rnd], 2)) + "<br/> Точность ответа: Eps=0.01, ввиду погрешностей округления и погрешностей методов"
        print("solve(): solved")
        print("solve(): answeQ=",self.answerQ,", answerM=",self.answerM)




class InertiaTask:  # this class is specifically for trac plugin
    def __init__(self):
        print("InertiaTask.__init__(): call")
        self.data = []
        self.answerX= 0
        self.answerY= 0
        self.text = "none so far"


    def generate(self):
        print("InertiaTask.generate(): call")
        self.data = generateInertia()
        print("InertiaTask.generate(): da")
        self.answerX=self.data['answerx']
        self.answerY=self.data['answery']
        self.text=self.data['text']


class StretchTask:  # this class is specifically for trac plugin
    def __init__(self):
        print("StretchTask.__init__(): call")
        self.beam = None
        self.answerN = 0
        self.answerL = 0
        self.answerS = 0
        self.text = "none so far"

    def generate(self):
        print("StretchTask.generate(): call")
        self.beam = generateBeam2()
        self.text = "<br/>Параметры стержня:<br/>Слева - жесткая заделка.<br/>Длина = " + str(
        self.beam.length) + " м.<br/>" + str(
        self.beam.getSec()) + "<br/>Ось Ox направлена вправо.<br/>" + "<br/>" + self.beam.getP() + "<br/>" + self.beam.getQ() + "<br/>"

    def solve(self):
        print("StretchTask.solve(): call")
        from .maths import getNLS
        solution = getNLS(self.beam)
        x = solution[0]
        N = solution[1]
        L = solution[2]
        S = solution[3]
        rnd = random.randrange(len(x))
        self.answerN = N[rnd]
        self.answerL = L[rnd]
        self.answerS = S[rnd]
        self.text = self.text + "<br/>Найти нормальные силы, напряжения и перемещения стержня круглого поперечного сечения в точке: " + str(
            round(x[rnd],
                  2)) + "<br/>Модуль упругости считать постоянным. Точность ответа: Eps=0.01, ввиду погрешностей округления и погрешностей методов"
        print("StretchTask.solve(): solved")
        print("StretchTask.solve(): answerN=",self.answerN,", answerL=",self.answerL,", answerS=",self.answerS)


class TwistTask:  # this class is specifically for trac plugin
    def __init__(self):
        print("TwistTask.__init__(): call")
        self.beam = None
        self.answerM = 0
        self.answerT = 0
        self.text = "none so far"

    def generate(self):
        print("TwistTask.generate(): call")
        self.beam = generateBeam3()
        self.text = "<br/>Параметры стержня:<br/>Слева - жесткая заделка.<br/>Длина = " + str(
        self.beam.length) + " м.<br/>" + str(
        self.beam.getSec()) + "<br/>Ось Ox направлена вправо.<br/>" + "<br/>" + self.beam.getM() + "<br/>" + self.beam.getm() + "<br/>"

    def solve(self):
        print("TwistTask.solve(): call")
        solution = getMTS(self.beam)
        x = solution[0]
        M = solution[1]
        T = solution[2]
        rnd = random.randrange(len(x))
        self.answerM = M[rnd]
        self.answerT = T[rnd]
        self.text = self.text + "<br/>Найти крутящий момент, угол поворота стержня круглого поперечного сечения в точке: " + str(
            round(x[rnd],
              2)) + "<br/>Модуль упругости считать постоянным. Точность ответа: Eps=0.01, ввиду погрешностей округления и погрешностей методов"

class Beam2:
    def __init__(self, _length):
        print("Beam2.__init__(): call")
        self.length = _length
        self.arrayQ = ["not set"]
        self.arrayP = ["not set"]
        self.arraySec = ["not set"]

    def addQ(self, _q):
        if self.hasQ() == False:
            del self.arrayQ[0]
        self.arrayQ.append(_q)

    def addP(self, _p):
        if self.hasP() == False:
            del self.arrayP[0]
        self.arrayP.append(_p)

    def addSec(self, _a, _b, _c):
        if self.hasSec() == False:
            del self.arraySec[0]
        self.arraySec.append(Sector(_a, _b, _c))

    def hasQ(self):
        if self.arrayQ[0] == 'not set':
            return False
        else:
            return True

    def hasSec(self):
        if self.arraySec[0] == 'not set':
            return False
        else:
            return True

    def hasP(self):
        if self.arrayP[0] == 'not set':
            return False
        else:
            return True

    def getQ(self):
        temp = "Распределенные нагрузки(на рисунке синим):<br/>"
        for q in range(len(self.arrayQ)):
            if self.arrayQ[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Распределенная нагрузка q_" + str(q + 1) + " приложена на отрезке [" + str(
                self.arrayQ[q].a) + " м. , " + str(self.arrayQ[q].b) + " м.], интенсивность равна: " + str(
                self.arrayQ[q].qa) + " кН/м<br/>"
        return temp

    def getP(self):
        temp = "Сосредоточенные силы(на рисунке красным):<br/>"
        for q in range(len(self.arrayP)):
            if self.arrayP[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Сосредоточенная сила Р_" + str(q + 1) + " приложена на расстоянии " + str(
                self.arrayP[q].point) + " м. от левого конца стержня, ее величина равна " + str(
                self.arrayP[q].amount) + " кН.<br/>"
        return temp

    def getSec(self):
        temp = "Сектора:<br/>"
        for q in range(len(self.arraySec)):
            if self.arraySec[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Сектор " + str(q + 1) + " находится на отрезке [" + str(
                self.arraySec[q].length) + "," + str(
                self.arraySec[q].length2) + "] м. от левого конца стержня, диаметры на концах: [" + str(
                self.arraySec[q].heigth) + "," + str(self.arraySec[q].heigth2) + "] мм.<br/>"
        return temp


class Beam3:
    def __init__(self, _length):
        self.length = _length
        self.arraym = ["not set"]
        self.arrayM = ["not set"]
        self.arraySec = ["not set"]

    def addm(self, _q):
        if self.hasm() == False:
            del self.arraym[0]
        self.arraym.append(_q)

    def addM(self, _p):
        if self.hasM() == False:
            del self.arrayM[0]
        self.arrayM.append(_p)

    def addSec(self, _a, _b, _c):
        if self.hasSec() == False:
            del self.arraySec[0]
        self.arraySec.append(Sector(_a, _b, _c))

    def hasm(self):
        if self.arraym[0] == 'not set':
            return False
        else:
            return True

    def hasSec(self):
        if self.arraySec[0] == 'not set':
            return False
        else:
            return True

    def hasM(self):
        if self.arrayM[0] == 'not set':
            return False
        else:
            return True

    def getm(self):
        temp = "Распределенные моменты(на рисунке синим):<br/>"
        for q in range(len(self.arraym)):
            if self.arraym[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Распределенныи момент m_" + str(q + 1) + " приложен на отрезке [" + str(
                self.arraym[q].a) + " м. , " + str(self.arraym[q].b) + " м.], интенсивность равна: " + str(
                self.arraym[q].qa) + " кН/м<br/>"
        return temp

    def getM(self):
        temp = "Сосредоточенные моменты(на рисунке красным):<br/>"
        for q in range(len(self.arrayM)):
            if self.arrayM[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Сосредоточенныи момент M_" + str(q + 1) + " приложен на расстоянии " + str(
                self.arrayM[q].point) + " м. от левого конца стержня, его величина равна " + str(
                self.arrayM[q].amount) + " кН/м.<br/>"
        return temp

    def getSec(self):
        temp = "Сектора:<br/>"
        for q in range(len(self.arraySec)):
            if self.arraySec[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Сектор " + str(q + 1) + " находится на отрезке [" + str(
                self.arraySec[q].length) + "," + str(
                self.arraySec[q].length2) + "] м. от левого конца стержня, диаметры на концах: [" + str(
                self.arraySec[q].heigth) + "," + str(self.arraySec[q].heigth2) + "] мм.<br/>"
        return temp


class Beam:
    def __init__(self, length, left_type, right_type):
        print("Beam.__init__(): new beam object created")
        self.length = length
        self.left = left_type
        self.right = right_type
        self.arrayQ = ["not set"]
        self.arrayM = ["not set"]
        self.arrayP = ["not set"]
        self.arrayOp = ["not set"]

    def addQ(self, _q):
        print("Beam.addQ(): adding new Q = ", str(_q))
        if self.hasQ() == False:
            del self.arrayQ[0]
        self.arrayQ.append(_q)
        print("Beam.addQ(): added new Q = ", str(_q))

    def addM(self, _m):
        print("Beam.addM(): adding new M = ", str(_m))
        if self.hasM() == False:
            del self.arrayM[0]
        self.arrayM.append(_m)
        print("Beam.addM(): added new M = ", str(_m))

    def addP(self, _p):
        print("Beam.addP(): adding new P = ", str(_p))
        if self.hasP() == False:
            del self.arrayP[0]
        self.arrayP.append(_p)
        print("Beam.addP(): added new P = ", str(_p))

    def addOp(self, _op):
        print("Beam.addOp(): adding new OP = ", str(_op))
        if self.hasOp() == False:
            del self.arrayOp[0]
        self.arrayOp.append(_op)
        print("Beam.addOp(): added new OP = ", str(_op))

    def hasQ(self):
        if self.arrayQ[0] == 'not set':
            return False
        else:
            return True

    def hasM(self):
        if self.arrayM[0] == 'not set':
            return False
        else:
            return True

    def hasP(self):
        if self.arrayP[0] == 'not set':
            return False
        else:
            return True

    def hasOp(self):
        if self.arrayOp[0] == 'not set':
            return False
        else:
            return True

    def printQ(self):
        print("printing Q")
        for q in range(len(self.arrayQ)):
            if self.arrayQ[0] == 'not set':
                print('not set\n')
                return
            print("a=" + str(self.arrayQ[q].a) + " b=" + str(self.arrayQ[q].b) + " q.a=" + str(
                self.arrayQ[q].qa) + " q.b=" + str(self.arrayQ[q].qb) + "\n")

    def getQ(self):
        temp = "Распределенные нагрузки:<br/>"
        for q in range(len(self.arrayQ)):
            if self.arrayQ[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Распределенная нагрузка q_" + str(q + 1) + " приложена на отрезке [" + str(
                self.arrayQ[q].a) + " м. , " + str(
                self.arrayQ[q].b) + " м.], интенсивность на правом конце равна: " + str(
                self.arrayQ[q].qa) + " кН/м, на левом конце: " + str(self.arrayQ[q].qb) + " кН/м<br/>"
        return temp

    def printM(self):
        print("Сосредоточенные оменты M:<br/>")
        for q in range(len(self.arrayM)):
            if self.arrayM[0] == 'not set':
                print('нет<br/>')
                return
            print("a=" + str(self.arrayM[q].point) + " m=" + str(self.arrayM[q].amount) + "\n")

    def getM(self):
        temp = "Сосредоточенные моменты:<br/>"
        for q in range(len(self.arrayM)):
            if self.arrayM[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Момент M_" + str(q + 1) + " приложен на расстоянии " + str(
                self.arrayM[q].point) + " м. от левого края балки, его величина составляет " + str(
                self.arrayM[q].amount) + " Т*м<br/>"
        return temp

    def printP(self):
        print("printing P")
        for q in range(len(self.arrayP)):
            if self.arrayP[0] == 'not set':
                print('not set\n')
                return
            print("a=" + str(self.arrayP[q].point) + " p=" + str(self.arrayP[q].amount) + "\n")

    def getP(self):
        temp = "Сосредоточенные силы:<br/>"
        for q in range(len(self.arrayP)):
            if self.arrayP[0] == 'not set':
                temp = temp + 'нет<br/>'
                return temp
            temp = temp + str(q + 1) + ". Сосредоточенная сила Р_" + str(q + 1) + " приложена на расстоянии " + str(
                self.arrayP[q].point) + " м. от левого конца балки, ее величина равна " + str(
                self.arrayP[q].amount) + " кН.<br/>"
        return temp

    def printOp(self):
        print("printing Op")
        for q in range(len(self.arrayOp)):
            print("a=" + str(self.arrayOp[q]) + "\n")

    def getOp(self):
        temp = "Опоры:<br/>"
        for q in range(len(self.arrayOp)):
            temp = temp + str(q + 1) + ". Опора " + str(q + 1) + " находится на расстоянии " + str(
                self.arrayOp[q]) + " м. от левого конца балки<br/>"
        return temp


class Sector:
    def __init__(self, _a, _b, _c, _d):
        self.length = _a
        self.length2 = _b
        self.heigth = _c
        self.heigth2 = _d


class P:
    def __init__(self, _point, _amount):
        self.point = _point
        self.amount = _amount


class Q:
    def __init__(self, _a, _b, _amountA, _amountB):
        self.a = _a
        self.b = _b
        self.qa = _amountA
        self.qb = _amountB


class M:
    def __init__(self, _point, _amount):
        self.point = _point
        self.amount = _amount
