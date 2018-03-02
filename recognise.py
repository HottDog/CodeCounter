# coding=utf-8
import func
path = "E:\\workspace\\python_workspace\\CodeCounter\\test\\main.cpp"
str1 = "sdadasdasd //sdadasdad"
str2 = "/*sdasdasd"


f = func.getFileReadObj(path)
s1 = f.readline()
print(s1)
isSpecial = False;
count = 0;
isBlank = False;
isValid = False;
isComment = False;

StrInfluence = False;
#把字符串删掉
s_process = ""
for s in s1:
    if(s=="\'"): 
        StrInfluence = True
    if(StrInfluence){

    }else{

    }    

    
    
    
