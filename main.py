import Reports
print ("1. The summary report")
print ("2. View all exported goods of a category")
print ("3. View all goods of a cargo")
print ("4. View all imported goods ordered by recently first")
print ("5. View all goods of a category")
ch = int(input("Enter your choice:\n"))
report = Reports.Reports()

if ch == 1: #The Summary Report
    print ("Total number of Goods:")
    cg = report.countGoods('E:\\PythonPractice\\LC_CC_python\\Report_making\\goods.xml')
    print (cg)
    print ("Total number of Categories:")
    cc = report.countCategory("category.xml")
    print (cc)
    print ("Total number of Cargos:")
    cca = report.countCargos("cargo.xml")
    print (cca)


elif ch == 2: #View all exported goods of a category
    cid = (input("Enter category id:\n"))
    str1 = report.viewAllExportedGoodsOfCategory("log.xml", "category.xml", "goods.xml", cid)
    for i in range(len(str1)):
        print (str1[i])


elif ch == 3: #View all goods of a cargo
    cid = int(input("Enter cargo id:\n"))
    s = report.viewAllGoodsOfCargo("goods.xml", "log.xml", cid)
    for i in range(len(s)):
        print (s[i])

elif ch == 4: #View all imported goods
    ans = []
    ans = report.viewAllImportedGoods("log.xml", "goods.xml")
    for i in range(len(ans)):
        print (ans[i])

elif ch == 5: #View all goods of a category
    cid = int(input("Enter category id:\n"))
    str2 = report.viewAllGoodOfCategory("goods.xml", cid)
    for i in range(len(str2)):
        print (str2[i])