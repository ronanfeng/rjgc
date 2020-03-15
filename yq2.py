import pandas as pd
def read(file1,file2,c):
        a="全部省"
        data=pd.read_table(file1,sep='\s+',encoding='ANSI',header=None) #读取数据
        data.columns=['x','y','z']
        gp=data.groupby(by=['x'])  #按照第一列（省）分组
        #if else判断用户选择输出的省份
        if a == c :#输出全部省
            
            f=open(file2,"w+") #输出到指定文件中
            for n,g in gp:
                
                print(n,file=f)#输出组名
                g[["y","z"]].to_csv(f,sep='\t',index=False,header=None)#输出后两列（县，人数），取消索引
                print('***',file=f) #每输出一组后用符号分开
            f.close()#关闭文件
            input('输出完成，输入任意键退出：')
        else:#输出指定省
            f=f=open(file2,"w+")
            g1=gp.get_group(c)
            print(c,file=f)
            g1[["y","z"]].to_csv(f,sep='\t',index=False,header=None)
            f.close()
        
            input('输出完成，输入任意键退出：')
def run():
    file1,file2,c = input("请依次输入读入文件,输出文件,输出省: ").split() #注意输入之间空格
    read(file1,file2,c)
run()
