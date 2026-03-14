import os
import shutil

def copy_files(src, dest):
    if (os.path.exists(dest)):
        shutil.rmtree(dest)
    os.mkdir(dest)
    
    if (os.path.exists(src) and os.path.exists(dest)):
        print("paths exist")
        dir_list = os.listdir(src)
        print(dir_list)
        if dir_list is not None or len(dir_list) > 1:
            for dir in dir_list:
                dir_path = os.path.join(src, dir)
                print("dir_path", dir_path)
                if os.path.isfile(dir_path):
                    shutil.copy(dir_path, dest)
                    print(f"copied {dir_path}")

                else:
                    new_dir = os.path.join(dest, dir)
                    os.mkdir(new_dir)
                    print(f"created {new_dir}")
                    print(f"copying files {os.path.join(src, dir_path)} to {os.path.join(dest, dir_path)}")
                    copy_files(os.path.join(src, dir), os.path.join(dest, dir))

        else:
            print("copy finished")
            return
            

#copy_files("../static", "../public")