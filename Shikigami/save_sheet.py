# Writing Shikigami to an excel sheet using Python 
from shikigami import Shikigami

import xlwt 
from xlwt import Workbook
# OR: workbook = xlwt.Workbook()

# Workbook is created 
wb = Workbook() 
  
# add_sheet() is used to create sheet. 
sheet = wb.add_sheet('Shikigami info')
# sheet.write(row,column,'word',style) is used to write in the sheet
sheet.write(0,0,'SHIKIGAMI',xlwt.easyxf('font:bold 1,color pink;'))

# Applying multiple styles
title = xlwt.easyxf('font:bold 1,color blue;')

# Writing on the 1st column which is column 0 in the sheet
# list all the shikigami names in coloumn 0
name = list(Shikigami.keys())
shi_number = len(name)
for column0_row in range(1,shi_number+1):
    sheet.write(column0_row,0,name[column0_row-1],title)

# list all the characteristics in row 0
sheet.write(0,1,'Attribute',title)
sheet.write(0,2,'Age',title)
sheet.write(0,3,'Level',title)
sheet.write(0,4,'Skill',title)

# read the info
attribute = []
for name in Shikigami.keys():
    attribute.append(Shikigami[name]["attribute"])
age = []
for name in Shikigami.keys():
    age.append(Shikigami[name]["age"])
lev = []
for name in Shikigami.keys():
    lev.append(Shikigami[name]["lev"])
skill = []
for name in Shikigami.keys():
    skill.append(Shikigami[name]["skill"])

# Write info in the sheet
for column1_row in range(1,shi_number+1):
    sheet.write(column1_row,1,attribute[column1_row-1])
for column2_row in range(1,shi_number+1):
    sheet.write(column2_row,2,age[column2_row-1])
for column3_row in range(1,shi_number+1):
    if lev[column3_row-1] == "SSR":
        sheet.write(column3_row,3,lev[column3_row-1],xlwt.easyxf('font:color gold;'))
    else:
        sheet.write(column3_row,3,lev[column3_row-1])
for column4_row in range(1,shi_number+1):
    sheet.write(column4_row,4,skill[column4_row-1])
    
# save()
wb.save('xlwt_shikigami.xls') 

