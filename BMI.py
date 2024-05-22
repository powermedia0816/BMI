# 0522 def 函式練習:計算BMI
# BMI 計算機(先以if..elif...else寫出)
# BMI < 18 「體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！
# 18 <= BMI < 24 恭喜！「健康體重」，要繼續保持！
# 24 <= BMI < 27 「體重過重」了，要小心囉，趕快力行「健康體重管理」！
# 27 <= BMI 啊～「肥胖」，需要立刻力行「健康體重管理」囉！

def BMI(weight,height):
    return weight/height*height
weight = int(input('請輸入體重(公斤):'))
height = float(input('請輸入身高(公尺):'))
bmi = BMI(weight, height)

if bmi < 18:
    print('BMI為:',bmi,'你的「體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！')
elif bmi < 24:
    print('BMI為:',bmi,'恭喜！「健康體重」，要繼續保持！')
elif bmi < 27:
    print('BMI為:',bmi,'你的「體重過重」了，要小心囉，趕快力行「健康體重管理」！')
else:
    print('BMI為:',bmi, '啊～「過度肥胖」啦，需要立刻力行「健康體重管理」囉！')