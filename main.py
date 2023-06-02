import pandas as pd


def note_wrong(num: int):
    with open('wrong.txt', 'a+') as f:
        f.write(f"第{num + 2}题，题型：{data['题型'][num]}\n")


num = 0
daoyan = 0
charpter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 共10章
data = pd.read_excel(r'tiku.xlsx', sheet_name=1)
for i in data['目录']:
    if '导言' in i:
        daoyan += 1
    if '第一章' in i:
        charpter[0] += 1
    if '第二章' in i:
        charpter[1] += 1
    if '第三章' in i:
        charpter[2] += 1
    if '第四章' in i:
        charpter[3] += 1
    if '第五章' in i:
        charpter[4] += 1
    if '第六章' in i:
        charpter[5] += 1
    if '第七章' in i:
        charpter[6] += 1
    if '第八章' in i:
        charpter[7] += 1
    if '第九章' in i:
        charpter[8] += 1
    if '第十章' in i:
        charpter[9] += 1
# 开始
timu = charpter[2]
print('共有{}道题'.format(timu))
# 上次的末尾
num = daoyan+charpter[0]+charpter[1]
for i in range(num,num+timu):
    print(f"第{num + 2}题，题型：{data['题型'][i]}")
    print(data['题干'][num])
    print(f"A: {data['A'][num]}  B: {data['B'][num]} \nC: {data['C'][num]}  D: {data['D'][num]}")
    choice = input('请输入你的答案：')
    if choice.upper() == data['正确答案'][num]:
        print('\033[0;32;40m回答正确\033[0m', end='\n\n')
    else:
        print(f"\033[0;31;40m回答错误，正确答案为：{data['正确答案'][num]}\033[0m", end='\n\n')
        note_wrong(num)
    num += 1

pass
