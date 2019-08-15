#coding=utf-8
python3 -m pdb xxx.py

输入l 显示源代码
输入n 向下执行一行代码
输入c continue继续执行代码
输入b和所在的行数 break添加断点
输入b 查看断点的序号
输入clear 断点的序号 清除断点
输入s 进入函数，展示调用函数的细节
输入p和变量 输出函数中变量的值
输入q 退出调试
输入r 快速执行到函数的最后一行

交互调试：
	import pdb
	pdb.run('testfun(args)')
程序中埋点：
	import pdb
	pdb.set_trace()



