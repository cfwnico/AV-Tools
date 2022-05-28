import os
from shutil import move, rmtree


# 先遍历qb下所有文件夹
# 然后继续遍历文件夹下的所有文件
# 如果其中文件拓展名包含".!qB"，就不对这个文件夹做处理
# 不包含".!qB"的情况下，获得所有需要移动的文件(文件大小大于700MB)路径，和移动的目标路径
# 全部完成之后，包含".!qB"：不处理，不包含".!qB"：移动文件，然后删除源目录。


def file_have_qB(path: str):
    """检测路径下的文件是否含有".!qB"的文件，有返回True，无返回False。注意：不会检测子文件夹。"""
    scandir = os.scandir(path)
    for i in scandir:
        if i.is_file():
            _, file_ext = os.path.splitext(i.path)
            if file_ext == ".!qB":
                return True
    return False


def get_move_info(path: str):
    """返回一个list，包含路径下大于700MB的文件路径。注意：不会检测子文件夹。"""
    file_path_list = []
    scandir = os.scandir(path)
    for i in scandir:
        if i.is_file():
            if os.path.getsize(i.path) > 734003200:
                file_path_list.append(i.path)
    return file_path_list


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.normpath(root_dir)
    av_folder = os.scandir(root_dir)
    for i in av_folder:
        if i.is_dir() and i.name != "番剧":
            if file_have_qB(i.path):
                print(f"{i.path}包含.!qB文件，跳过处理！")
                continue
            else:
                file_list = get_move_info(i.path)
                for path in file_list:
                    file_name = os.path.basename(path)
                    src_path = path
                    dst_path = os.path.join(root_dir, file_name)
                    move(src_path, dst_path)
                    print(f"移动文件：{src_path} -> {dst_path}")
                rmtree(i.path)
                print(f"删除文件夹：{i.path}")
input("处理完毕！")
