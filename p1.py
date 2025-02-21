score = int (input ("请输入一个分数：") )
while (score > 100) or (score < 0) :
    print("输入错误，请输入正确分数：")
    score = int (input ("请输入一个分数：") )


# v1版本：需要对每一个条件分支进行判断，如98分，判断为为A后，还要判断后面的
'''
if 100 >= score >= 90 :
    degree = "A"

if 90 > score >= 80 :
    degree = "B"

if 80 > score >= 70 :
    degree = "C"

if 70 > score >= 60 :
    degree = "D"

if score < 60 :
    degree = "F"
'''

# v2版本：只要符合条件了，后面的就不需要判断了，如98只判断一次就输出了
'''
if 100 >= score >= 90 :
    degree = "A"
else :
    if 90 > score >= 80 :
        degree = "B"
    else :
        if 80 > score >= 70 :
            degree = "C"
        else :
            if 70 > score >= 60 :
                degree = "D"
            else :
                if score < 60 :
                    degree = "F"
'''

# v3版本：简洁写法
if 100 >= score >= 90 :
    degree = "A"
elif 90 > score >= 80 :
    degree = "B"
elif 80 > score >= 70 :
    degree = "C"
elif 70 > score >= 60 :
    degree = "D"
else :
    degree = "F"




print("等级为：" + degree)
