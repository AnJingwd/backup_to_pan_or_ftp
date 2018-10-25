# -*- coding: utf-8 -*-

import os,datetime,ConfigParser
from ftplib import FTP
from threading import Timer
from bypy import ByPy


def conf_parse(conf_file):
	cf = ConfigParser.ConfigParser()
	cf.read(conf_file)
	conf_dict = {}
	for section in cf.sections():
		for (key,value) in cf.items(section):
			conf_dict[key] = cf.get(section, key)
	return conf_dict

def ftpconnect(ftpserver,port,username,password):
	ftp=FTP()
	try:
		ftp.connect(ftpserver,port)
	except:
		raise IOError("FTP connect failed!")
	try:
		ftp.login(username,password)
	except:
		raise IOError("FTP login failed!")
	else:
		print("************ftp连接登陆成功*************")
		return ftp

def uploadfile_ftp(ftp,local_file,ftp_path):
	file_name = os.path.basename(local_file)
	file_remote = ftp_path+"/"+file_name
	fp = open(local_file, 'rb')
	bufsize = 1024
	try:
		ftp.storbinary('STOR ' + file_remote,fp,bufsize)
		print("文件{} 上传成功".format(file_name))
		fp.close()
	except:
		print("文件{} 上传失败".format(file_name))

def uploadfile_pan(local_file,remote_path):
	file_name = os.path.basename(local_file)
	bp = ByPy()
	try:
		bp.upload(local_file, remote_path)
		print("文件{} 上传成功".format(file_name))
	except:
		print("文件{} 上传失败".format(file_name))

def delpanfile(remote_file):
	file_name = os.path.basename(remote_file)
	bp = ByPy()
	try:
		bp.delete(remote_file)
		print("文件{} 删除成功".format(file_name))
	except:
		print("文件{} 删除失败".format(file_name))

def delftpfile(ftp,remote_file):
	file_name = os.path.basename(remote_file)
	try:
		ftp.delete(remote_file)
		print("文件{} 删除成功".format(file_name))
	except:
		print("文件{} 删除失败".format(file_name))

def make_today_dir(target_dir):
	time_now = datetime.datetime.now()
	today_dir_name = "back_up_"+ time_now.strftime('%b_%d_%Y_%Hh%Mm%Ss')
	today_dir = os.path.join(target_dir,today_dir_name)
	return (time_now,today_dir)

def find_targeted_files(source_dir,today_dir,pattern_list,exclude_dirs_list=""):
	if os.path.exists(today_dir) == 0:
		os.mkdir(today_dir)
	for pattern in pattern_list:
		pattern_new = ".*" + pattern
		if exclude_dirs_list =="":
			COMMAND = "find " + source_dir +" -regex "+"'"+pattern_new +"'"+ " -exec cp -rp --parents {} " + today_dir +" "+ "\;"
			os.system(COMMAND)
		else:
			exclude_dirs_str = " -path {} -prune ".format(exclude_dirs_list[0])
			for i in exclude_dirs_list[1:]:
				exclude_dirs_str =exclude_dirs_str + "-o -path {} -prune ".format(i)
			COMMAND = "find " + source_dir + exclude_dirs_str +" -o -regex " + pattern_new + " -exec cp -rp --parents {} " + today_dir +" "+ "\;"
			os.system(COMMAND)

def record_requirement(today_dir,mypython,Rscript,R_packages_installed,conda):
	env_dir = os.path.join(today_dir, "env_requirements")
	if os.path.exists(env_dir) == 0:
		os.mkdir(env_dir )
	COMMAND1 =  mypython +" -m pip freeze >" + os.path.join(env_dir,"python_pip_requirements.txt")
	COMMAND2 = Rscript +" "+ R_packages_installed + " " + os.path.join(env_dir, "R_installed_requirements.csv")
	COMMAND3 = conda +" list -e >" + os.path.join(env_dir, "conda_requirements.txt")
	COMMAND4 = "cp -a "+ "~/.bashrc " +env_dir
	os.system(COMMAND1)
	os.system(COMMAND2)
	os.system(COMMAND3)
	os.system(COMMAND4)

def zip_dir(today_dir):
	command_zip = "zip -qr " + today_dir + '.zip' + ' '+ today_dir
	command_rm  = "rm -rf " + today_dir
	os.system(command_zip)
	os.system(command_rm)









