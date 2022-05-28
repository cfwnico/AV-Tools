import os

# 把程序所在文件夹下中所有文件的文件名中的英文重命名成大写。
# 不处理文件后缀名,不处理子文件夹中的文件,不处理文件夹名称。


def proc_filename(workdir):
    value = 0
    text_list = [
        "~nyap2p.com",
        "-c",
        "_2k",
        "@蜂鳥@fengniao151.vip-",
        "hhd800.com@",
        "freedl.org@",
        "_x1080x",
    ]
    error_list = []
    for i in os.scandir(path=workdir):
        if i.is_file():
            file_name = i.name
            for text in text_list:
                file_name = file_name.replace(text, "")
                text_upper = text.upper()
                file_name = file_name.replace(text_upper, "")
            file_path = os.path.join(workdir, file_name)
            if os.path.exists(file_path):
                continue
            try:
                os.rename(i.path, file_path)
            except FileExistsError:
                error_list.append(i.path)
            print(file_path)
            value += 1
    return value, error_list


def upper_filename(workdir):  # 文件名中的英文重命名成大写
    value = 0  # 计数
    error_list = []
    for i in os.scandir(path=workdir):  # 遍历程序所在目录下所有对象
        if i.is_file():  # 仅处理文件
            base, ext = os.path.splitext(i.name)  # 返回文件名和拓展名
            filerename = os.path.join(workdir, base.upper() + ext)  # 合并大写处理后的文件名与路径
            if filerename == i.path:
                continue
            try:
                os.rename(i.path, filerename)  # 重命名
            except FileExistsError:
                error_list.append(i.path)
                continue
            print(filerename)  # 打印
            value += 1  # 计数+1
    return value, error_list


if __name__ == "__main__":
    rootdir = os.path.dirname(os.path.realpath(__file__))  # 获取本体程序所在目录
    try:
        proc_count1, error_list1 = proc_filename(rootdir)
        proc_count2, error_list2 = upper_filename(rootdir)
        error_count1 = len(error_list1)
        error_count2 = len(error_list2)
        print(f"处理无用前后缀{proc_count1}个，英文大写改写{proc_count2}个。")
        input(f"共出现个{error_count1}去除前后缀错误，{error_count2}个大写命名错误，按下回车打印错误列表。")
        for i in error_list1:
            print(i)
        input("按下回车继续打印错误列表。")
        for i in error_list2:
            print(i)
        input("处理完毕，按任意键退出。")
    except BaseException as n:
        print(n)
        input("wdnmd出现了未知错误啊！")
