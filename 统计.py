 
def count_words(text):
    '''
    计算文本中每个单词出现的次数
    '''
    # 将文本中的标点符号替换为空格
    for char in '-.,\n':
        text = text.replace(char,' ')
    
    # 将文本分割成单词列表
    words = text.split()
    
    # 统计每个单词出现的次数
    freq = {}
    for word in words:
        freq[word] = freq.get(word,0) + 1
    
    # 输出统计结果
    for word in sorted(freq):
        print(word, freq[word])

# 获取用户输入的文本信息
text = input("请输入需要统计的文本信息：")

# 调用计算函数
count_words(text)
