import time

def countdown(duration):
    '''
    倒计时函数，duration表示倒计时时长（秒）
    '''
    for i in range(duration,0,-1):
        print(i)
        time.sleep(1)
    print("倒计时结束！")

# 测试倒计时函数，倒计时时长为10秒
countdown(10)
