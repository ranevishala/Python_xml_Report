from xml.dom import minidom
import xml.etree.ElementTree as ET
import csv
import operator
from datetime import datetime
from collections import OrderedDict
import time

class Reports:
    def countGoods(self, goodsFile): #count goods items.
    #-- -Fill your code here-- -- -- -#
        tree1 = ET.parse(goodsFile)
        root1 = tree1.getroot()
        n1 = 0
        for g1 in root1.findall("goods"):
            n1 += 1
        return n1

    def countCategory(self, categoryFile): #count Category items.
    #-- -Fill your code here-- -- -- -#
        tree2 = ET.parse(categoryFile)
        root2 = tree2.getroot()
        n2 = 0
        for g2 in root2.findall("category"):
            n2 += 1
        return n2

    def countCargos(self, cargoFile): #count number of cargos.
    #-- -Fill your code here-- -- -- -#
        tree3 = ET.parse(cargoFile)
        root3 = tree3.getroot()
        n3 = 0
        for g3 in root3.findall("cargo"):
            n3 += 1
        return n3

    ## Option 2

    def viewAllExportedGoodsOfCategory(self, logFile, categoryFileName, goodsFile, categoryId):
        #-- -Fill your code here-- -- -- -#
        tree4 = ET.parse(logFile)
        root4 = tree4.getroot()
        tree2 = ET.parse(categoryFileName)
        root2 = tree2.getroot()
        tree1 = ET.parse(goodsFile)
        root1 = tree1.getroot()
        flag = 0
        str1 = []
        gn = []
        gid = []
        goodsId = 0
        gname = ''
        for g1 in root2.findall("category"):
            cid = g1.find("id").text
            if int(cid) == categoryId:
                flag = 1
                break
        if flag == 0:
            print("Category ID does not exist")
            return str1
        else :
            for r1 in root1.findall("goods"):
                cid1 = r1.find("categoryId").text
                if int(cid1) == categoryId:
                    gid1 = r1.find("number").text
                    gname = r1.find("name").text
                    gn.append(gname)
                    gid.append(int(gid1))
        for g2 in root4.findall("log"):
            act = g2.find("action").text
            goodsId = g2.find("goodsId").text
            for i in range(len(gid)):
                if int(goodsId) == gid[i] and act == "Exported":
                    gid.append(int(goodsId))
                    strele = str(gid[i]) + " - " + str(gn[i])
                    str1.append(strele)
        return str1
        ## Option 3

    def viewAllGoodsOfCargo(self, goodsFile, logFile, cid):
        #-- -Fill your code here-- -- -- -#
        tree4 = ET.parse(logFile)
        root4 = tree4.getroot()
        tree1 = ET.parse(goodsFile)
        root1 = tree1.getroot()
        flag = 0
        gid = ''
        gn = ''
        rec = ''
        s = []
        gid1 = []
        gn1 = []
        for gc in root4.findall("log"):
            cid1 = gc.find("cargoId").text
            if int(cid1) == cid:
                goodid = gc.find("goodsId").text
                gid1.append(int(goodid))
                flag = 1
                break
        if flag == 0:
            print("Cargo ID does not exist")
        else :
            j = 0
            for gc1 in root1.findall("goods"):
                cid2 = gc1.find("number").text
                if gid1[j] == int(cid2):
                    gid = gc1.find("number").text
                    gn = gc1.find("name").text
                    rec = gid + " - " + gn
                    s.append(rec)
            j += 1
        return s

    def viewAllImportedGoods(self, logFile, goodsFile):
        #-- -Fill your code here-- -- -- -#
        tree4 = ET.parse(logFile)
        root4 = tree4.getroot()
        tree1 = ET.parse(goodsFile)
        root1 = tree1.getroot()
        ans = []
        dat = []
        date1 = []
        gid1 = ''
        gn1 = ''
        rec = ''
        j = 0
        gid = []
        gn = []
        gn2 = []
        d = {}
        d1 = {}
        for gi in root4.findall("log"):
            act = gi.find("action").text
            if act == "Imported":
                gid1 = gi.find("goodsId").text
                dat1 = gi.find("date").text
                d[gid1] = dat1
        values = list(d.values())
        values.sort()
        for i in range(len(d1)):
            print([value for gid1, value in dat1])

        for gi1 in root1.findall("goods"):
            j = 0
            n = gi1.find("number").text
            for key in d.keys():
                if int(key) == int(n):
                    gn1 = gi1.find("name").text
                    rec = str(n) + " - " + gn1
                    ans.append(rec)
        ans.reverse()
        return ans
        ## Option 5.

    def viewAllGoodOfCategory(self, goodsFile, cid):
        #-- -Fill your code here-- -- -- -#
        tree1 = ET.parse(goodsFile)
        root1 = tree1.getroot()
        flag = 0
        gid = ''
        gn = ''
        rec = ''
        str2 = []
        for c1 in root1.findall("goods"):
            cid1 = c1.find("categoryId").text
            if int(cid1) == cid:
                gid = c1.find("number").text
                gn = c1.find("name").text
                rec = gid + " - " + gn
                str2.append(rec)
        return str2
