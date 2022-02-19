import torch
import numpy
import matplotlib

a = 4
b = 4
a, b = b, a
print(1)

# 这个写法中，__name__表示该文件的文件名，当该模块直接执行时，其值为 文件名.py， 当该模块被调用而执行时，其值为 文件名;
# 而__main__为一常量， 其值始终为 文件名.py;
# 因此在直接执行时，该语句后的语句也执行
# 而调用执行时，该语句后的语句不执行
if __name__ == '__main__':
    print(2)
#efwwefwfwwfw

#ffewfwfwfwfw uiuiuiuuuiuiuuiuuuii

# print(torch.__version__)
# print('gpu', torch.cuda.is_available())



#dev change 23:41