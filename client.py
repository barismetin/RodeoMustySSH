#!/usr/bin/env python3
#-*-coding:utf-8-*-
import socket
import os
import crypt
host = "ip"

port = 7888
bufferdata = 1024
addr = (host,port)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



deneme = 0
while deneme < 3:
    kadi = input("Kullanıcı Adı: ")
    sifre = input("Sifre : ")
    kadi = crypt.sifrele(kadi)
    sifre = crypt.sifrele(sifre)
    s.sendto(kadi,addr)
    s.sendto(sifre,addr)
    (data,addr) = s.recvfrom(bufferdata)
    data = data.decode("utf-8")
    if data == "True":

        while True:


            data = input("Komut Girmelisin!:")
            sdata = data.encode("utf-8")
            s.sendto(sdata,addr)
            if data == "exit":
                break
            elif data == "git":
                komut = input("Konum Belirtiniz : ")
                komut = komut.encode("utf-8")
                s.sendto(komut,addr)
            elif data == "onizle":
                komut = input("Dosya adı giriniz : ")
                komut = komut.encode("utf-8")
                s.sendto(komut,addr)
            elif data == "dosyaolustur":
                komut = input("Dosya Adı Giriniz : ")
                komut = komut.encode("utf-8")
                s.sendto(komut,addr)
            (data,addr) = s.recvfrom(bufferdata)
            data = data.decode("utf-8")



            if data == " ":
                pass


            else:
                print(data)

        s.close()
        os._exit(0)
    else:
        deneme= deneme+1
        denemehk = 3-deneme
        print("Kullanıcı adı ve şifre hatalı tekrar deneyiniz.Kalan deneme hakkınız ", +denemehk)
