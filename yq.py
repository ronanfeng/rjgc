import pandas as pd
def read(filename):
        data=pd.read_table(filename,sep='\s+',encoding='ANSI',header=None) #读取数据
        data.columns=['x','y','z']
        gp=data.groupby(by=['x'])  #按照第一列（省）分组
        f=open("C:\\Users\\10543\\Desktop\\yq_out.txt","w+") #输出到指定文件中
        for n,g in gp:
            print(n,file=f)
            g[["y","z"]].to_csv(f,sep='\t',index=False,header=None)#输出后两列（县，人数），取消索引
            print('***',file=f) #每输出一组后用符号分开
        f.close()
        print('归类完成')
def run():
    filename = input("输入文件地址（python）: ") #注意输入的地址格式要与python的格式相匹配
    read(filename)
run()
