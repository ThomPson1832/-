import time

focus_time = 25 # 专注时间（分钟）
break_time = 5 # 休息时间（分钟）
loops = 4 # 运行轮数

for i in range(loops):
    print("开启专注模式...")
    time.sleep(focus_time * 60)
    print("时间到！请开始你的休息。")
    time.sleep(break_time * 60)
    
print("恭喜你完成了所有任务！")
