import pandas as pd
col=["國語","數學","英文","自然","社會"]
data=[["75","62","85","73","60"],
      ["91","53","56","63","65"],
      ["71","88","51","69","87"],
      ["69","53","87","74","70"]]
ro=["小林","小黃","小陳","小美"]
df=pd.DataFrame(data,index=ro,columns=col)
print(df)
print("-"*30) #我是分隔線1
print("後二位的成績")
print(df.tail(2))
print("-"*30) #我是分隔線2
print("以自然遞減排序")
dfi=df.iloc[0:5,3:4]
print(dfi.sort_values("自然",ascending=False))
print("-"*30) #我是分隔線3
print("輸出第一、三位的數學與自然成績")
print(df.loc[["小林","小陳"],["數學","自然"]])




