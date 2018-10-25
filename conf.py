[baseconf]
ftpserver = 'YOUR FTP SERVER'
username = 'USERNAME'
password = 'PASSWARD'
port=21

[softwares]
python="YOURPATH/python"
Rscript = "YOURPATH/Rscript"
R_packages_installed = "YOURPATH/R_packages_installed.R"
conda="YOURPATH/conda"

[dirs]
source_dir = "YOURPATH/scripts"
target_dir = "YOURPATH//backup_scripts"
remote_path = "back_up/"
exclude_dirs_list=["YOURDIR"]

[others]
pattern_list = [".py",".pl",".sh",".R"]
days=1

[ways]
baidu_pan="yes"
FTP="no"