import pandas as pd



cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1",
        "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]

df = pd.read_csv('magic04.data',names = cols)

print(df.columns)  
# columns 返回所有列名字



print(df.columns[:-1]) 
 # 这是 Python 的切片操作（slicing）：[:-1] 表示：从开头到倒数第二个元素（不包括最后一个）



print(df.columns[:])
# 返回全部列特征的名字


print(df[df.columns[:-1]]) 
# 返回全部特征列（全部）



print(df[df.columns[:-1]].values)
# values
# 这是 Pandas 的一个属性，把 DataFrame 转成 NumPy 数组（numpy array）
# 因为大多数机器学习模型（如 sklearn）要求输入是 数组格式，而不是 DataFrame。


