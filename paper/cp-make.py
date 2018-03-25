import glob
import os
#hid-sp18-*
hids = glob.glob("../../C:/Users/Surya/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/root/github/cloudmesh-community/hid-sample")

for d in hids:
    if os.path.isdir(d):
        command = ("cp Makefile {d}/paper".format(d=d))
        print (command)
        os.system(command)
