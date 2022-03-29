"""
 * Project name(项目名称)：Python_try_except异常
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:02
 * Version(版本): 1.0
 * Description(描述)：
 try:
    可能产生异常的代码块
except [ (Error1, Error2, ... ) [as e] ]:
    处理异常的代码块1
except [ (Error3, Error4, ... ) [as e] ]:
    处理异常的代码块2
except  [Exception]:
    处理其它异常

(Error1, Error2,...) 、(Error3, Error4,...)：其中，Error1、Error2、Error3 和 Error4 都是具体的异常类型。
        显然，一个 except 块可以同时处理多种异常。
[as e]：作为可选参数，表示给异常类型起一个别名 e，这样做的好处是方便在 except 块中调用异常类型（后续会用到）。
[Exception]：作为可选参数，可以代指程序可能发生的所有异常情况，其通常用在最后一个 except 块。

首先执行 try 中的代码块，如果执行过程中出现异常，系统会自动生成一个异常类型，并将该异常提交给 Python 解释器，此过程称为捕获异常。
当 Python 解释器收到异常对象时，会寻找能处理该异常对象的 except 块，如果找到合适的 except 块，
则把该异常对象交给该 except 块处理，这个过程被称为处理异常。
如果 Python 解释器找不到处理异常的 except 块，则程序运行终止，Python 解释器也将退出。
 """

if __name__ == '__main__':
    try:
        a = int(input("输入被除数："))
        b = int(input("输入除数："))
        c = a / b
        print("您输入的两个数相除的结果是：", c)
    except ValueError as e:
        print("出现异常")
        print("异常内容：", str(e))
    except ArithmeticError as e:
        print("出现异常")
        print("异常内容：", str(e))
    except:
        print("其它异常")
        print("程序运行结束")
