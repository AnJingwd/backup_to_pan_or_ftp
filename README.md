# backup_to_pan_and_ftp
自动备份各类编程脚本及python，R，conda已安装包信息至百度云盘及FTP服务器

## 主要脚本说明

- backup_main.py ：  备份的主函数
- backup_function.py ：  封装的函数，供主函数调用。百度网盘操作基于bypy包，ftp操作基于ftplib包
- conf.py 所有所需参数的配置文件，默认每隔1天备份一次，可通过days参数修改。同时删除3天前备份的文件
- requirements.py ： 该仓库所依赖的python包，使用python -m pip install -r requirements.py进行批量安装

## 其他脚本

- R_packages_installed.R  ： 获取已经安装的R包及Bioconductor包信息，生成R_installed_requirements.csv文件，只有可以使用Rscripts ipak.R R_installed_requirements.csv进行批量安装

- ipak.R ：用于批量安装R包及Bioconductor包

## 主要函数说明

- find_targeted_files(source_dir,today_dir,pattern_list,exclude_dirs_list="") ： 用于选择需要备份的文件及其目录，source_dir指定需要备份的路径，today_dir指定备份的文件及目录的本地存放位置，pattern_list通过正则表达式列表指定需要备份哪些文件，exclude_dirs_list用于指定不需要备份的目录列表

