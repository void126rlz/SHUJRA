import os # sys
import pandas  as pd

home = r'D:\tfp\project\新致软件\3岗位推荐算法\from新致\数据'

fileNamesCSV = os.listdir(home + r'\历史18天的数据') # \*.csv  
print(fileNamesCSV)

# !dir D:\tfp\project\新致软件\3岗位推荐算法\from新致\数据\utf8
fileNames = [s[0:-4] for s in fileNamesCSV]
print(fileNames)

# InvalidWorksheetName: Excel worksheet name 'ttyc_personel_educational_experience' must be <= 31 chars.
# print(len('ttyc_personel_educational_experience'))
# [len(f) for f in fileNamesCSV] # <34-3=31
# [18, 14, 18, 41, 24, 37, 34, 17, 23]
[len(f) for f in fileNames]


fileNames=[
#     'ttyc_candidate',
#  'ttyc_label',
#  'ttyc_personnel',
 'ttyc_personnel_educational_experience',
 'ttyc_personnel_label',
 'ttyc_personnel_project_experience',
 'ttyc_personnel_work_experience',
 'ttyc_position',
 'ttyc_position_label'
]

for f in fileNames:
    print(f)
    df= pd.read_csv(home + '\\历史18天的数据\\' + f + '.csv', error_bad_lines=False )
    df.to_excel(home + '\\excel18\\' + f + '.xlsx', sheet_name=f[5:36],index=False)

# f = 'ttyc_personnel'
df= pd.read_csv(home + '\\历史18天的数据\\ttyc_personnel-tfp.csv', error_bad_lines=False )
df.to_excel(home + '\\excel18\\ttyc_personnel-tfp.xlsx', sheet_name='ttyc_personnel',index=False)

# ;号分隔的cvs文件
fileNames2 = ['ttyc_position', 'ttyc_position_label']
for f in fileNames2:
    print(f)
    df= pd.read_csv(home + '\\utf8\\' + f + '.csv', sep=';') # quotechar='"',
    df.to_excel(home + '\\excel\\' + f + '.xlsx', sheet_name=f,index=False)
    
 f = 'ttyc_personnel_project_experienceT'
df= pd.read_csv(home + '\\utf8\\' + f + '.csv')
df.to_excel(home + '\\excel\\' + f + '.xlsx', sheet_name=f[5:36],index=False)

 