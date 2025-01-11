import math

# 输入
mins = input("Input render time for 4 frames (mins): ")
frames = input("Input number of frames: ")

# 解析输入
mins = [y for y in mins.split(':')]  # 直接按冒号分割

fmins = []
for n in range(0, len(mins), 2):
    if n+1 < len(mins):  # 确保不会超出范围
        fmins.append(float(mins[n]) + float(mins[n+1]) / 60)
    else:
        fmins.append(float(mins[n]))  # 如果没有分钟部分，直接添加小时部分

# 计算平均渲染时间
avg = sum(fmins) / len(fmins)

# 总渲染时间（分钟）
total_minutes = avg * int(frames)

# 总渲染时间（小时）
total_hours = total_minutes / 60

# 分离小时和分钟
frac, whole = math.modf(total_hours)
formatted_hours = str(int(whole)) + ":" + str(int(round(frac * 60)))

# 输出
print("Estimated total render time (hrs): ", formatted_hours)
print("Estimated total render time (mins): ", total_minutes)

# 等待用户按任意键退出
input("Press any key to exit...")
