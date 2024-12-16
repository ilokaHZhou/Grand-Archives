def min_markers_to_clear_segments(startX, endX):
    # 合并起点和终点形成线段，存储为 (start, end) 的形式
    segments = list(zip(startX, endX))
    
    # 按照线段的结束坐标升序排序
    segments.sort(key=lambda x: x[1])
    
    # 初始化标记物的数量和最后一个标记物的位置
    markers = 0
    last_marker = -float('inf')
    
    # 遍历所有线段
    for start, end in segments:
        # 如果当前线段的起点大于最后一个标记物位置，选择新的标记物（这个marker能划掉的就这么多线段了，准备找下一组能被一个marker划掉的线段）
        if start > last_marker:
            # 将标记物放在当前线段的结束坐标
            last_marker = end
            markers += 1
    
    return markers

# 示例输入
numS = 3
startX = [1, 2, 3, 6]
endX = [5, 4, 6, 7]

# 调用函数
result = min_markers_to_clear_segments(startX, endX)
print("最少需要的标记物数量:", result)
