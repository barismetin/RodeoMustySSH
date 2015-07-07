#!/usr/bin/env python3
#-*-coding:utf-8-*-
import socket
import os
import subprocess
import crypt
def loginkontrol(kadi,sfire):
    a = "rodeo"
    b = "musty"
    if kadi == a:
        if sifre == b:
            return True
        else:
            return False
    else:
        return False
host = ""
port = 7888
bufferdata = 1024
addr = (host,port)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr)
print("Giriş Bekleniyor")
hatalideneme = 0

(data,addr) = s.recvfrom(bufferdata)
data = data.decode("utf-8")
while True:
    kadi = crypt.sifrecoz(data)
    (data,addr) = s.recvfrom(bufferdata) 
    data = data.decode("utf-8")
    sifre = crypt.sifrecoz(data) 
    if loginkontrol(kadi,sifre) == True:
        print("Giriş Kabul Edildi :) ")
        data = "True".encode("utf-8")
        s.sendto(data,addr)
        while True:
            (data,addr) = s.recvfrom(bufferdata)
            data = data.decode("utf-8")
            print(data)
            if data == "exit":
                break
            elif data == "listele":
                c1 = subprocess.check_output("ls",shell=True)

                s.sendto(c1,addr)
            elif data == "git":
                (data,addr) = s.recvfrom(bufferdata)
                ss = data.decode("utf-8")

                try:
                    c1 = os.chdir(ss)
                    c1 = "Gidildi.".encode("utf-8")
                    s.sendto(c1,addr)
                except FileNotFoundError:
                    c1 = "Böyle bir klasör yok".encode("utf-8")
                    s.sendto(c1,addr)
            elif data == "onizle":
                (data,addr) = s.recvfrom(bufferdata)
                ss = data.decode("utf-8")
                try:
                    ss = "cat " + ss
                    c1 = subprocess.check_output(ss,shell=True)
                    s.sendto(c1,addr)
                except FileNotFoundError:
                    c1 = "Bu isimde bir dosya yok.".encode("utf-8")
                    s.sendto(c1,addr)
            elif data == "dosyaolustur":
                (data,addr) = s.recvfrom(bufferdata)
                ss = data.decode("utf-8")
                if os.path.exists(ss) == True:
                    s.sendto("Böyle bir dosya zaten var".encode("utf-8"),addr)
                else:
                    open(ss,"a").close()
                    s.sendto("Dosya Oluşturuldu.".encode("utf-8"),addr)
        s.close()
        os._exit(0)

    else:
        s.sendto("hatalı".encode("utf-8"),addr)
        print("hatalı deneme")
        if hatalideneme == 3:
            s.close()
            os._exit(0)
        else:
            hatalideneme = hatalideneme+1
