"""
 * Project name(项目名称)：Python_try_except异常
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:09
 * Version(版本): 1.0
 * Description(描述)：
 args：返回异常的错误编号和描述字符串；
str(e)：返回异常信息，但不包括异常信息的类型；
repr(e)：返回较全的异常信息，包括异常信息的类型。
 """

if __name__ == '__main__':
    try:
        1 / 0
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e.args)
        print(str(e))
        print(repr(e))
