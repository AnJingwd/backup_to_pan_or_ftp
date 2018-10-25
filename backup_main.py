#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Timer
import datetime


import os,sys
'''import customized module'''
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(current_path)
import backup_function as myfunction

conf_file = os.path.join(current_path,"conf.py")
conf = myfunction.conf_parse(conf_file)

def backup_main(conf):
	(time_now,today_dir) = myfunction.make_today_dir(eval(conf["target_dir"]))
	myfunction.find_targeted_files(eval(conf["source_dir"]), today_dir,eval(conf["pattern_list"]), \
								   eval(conf["exclude_dirs_list"]))
	myfunction.record_requirement(today_dir,eval(conf["python"]),eval(conf["rscript"]),\
								  eval(conf["r_packages_installed"]),eval(conf["conda"]))
	myfunction.zip_dir(today_dir)

	three_days_ago_time = (time_now - datetime.timedelta(days=3)).strftime('%b_%d_%Y_%Hh%Mm%Ss')
	three_days_ago_file = eval(conf["remote_path"]) + "back_up_" + three_days_ago_time + ".zip"

	if eval(conf["baidu_pan"]) == "yes":
		myfunction.uploadfile_pan(today_dir+".zip",eval(conf["remote_path"]))
		"""delete file of 3 days ago from pan and local """
		myfunction.delpanfile(three_days_ago_file)
		local_file = eval(conf["target_dir"])+ "back_up_"+three_days_ago_time+".zip"
		os.system("rm {local_file}".format())
	else:
		ftp = myfunction.ftpconnect(eval(conf["ftpserver"]), eval(conf["port"]), \
								eval(conf["username"]), eval(conf["password"]))
		myfunction.uploadfile_ftp(ftp, today_dir+".zip", eval(conf["remote_path"]))
		"""delete file of 3 days ago from ftp and local """
		myfunction.delftpfile(ftp,three_days_ago_file)
		os.system("rm {local_file}".format())
		ftp.quit()

def back_up_upload_loop():
	time_s = int(eval(conf["days"]))*24*60*60
	t = Timer(time_s, back_up_upload_loop)
	t.start()
	print("start to back up again")
	backup_main(conf)


back_up_upload_loop()