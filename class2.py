import json
import sqlite3
import datetime

if __name__ == '__main__':
    print("Server\t\t\tPing\t\tDownload\tUpload")
    print("-------------------------------------------------------------------")

    with sqlite3.connect('speedtest.db') as connection:
        rows = connection.execute('SELECT * FROM RESULTS').fetchall()
        
    for x in range(len(rows)):
        # cdo rresht cift pasi nuk duam ti printojme te dhenat e serverit fast
        if(x%2==0):
            print(rows[x][0]+"\t"+str(rows[x][2])+" ms\t\t"+str(rows[x][3])
                  +" Mbps\t\t"+str(rows[x][4])+" Mbps")

    x = len(rows)

    # unaze e pafundme, sa here qe speed.py merr te dhena te reja, shtojme
    # ata rreshta ne output
    while(1):
        with sqlite3.connect('speedtest.db') as connection:
            rows = connection.execute('SELECT * FROM RESULTS').fetchall()

        # nese ndryshon x nga rows, pra nese eshte shtuar nje rresht i ri
        # printo rreshtin e ri
        if(x!=len(rows)):
  
            print(rows[len(rows)-2][0]+"\t"+str(rows[len(rows)-2][2])
                  +" ms\t\t"+str(rows[len(rows)-2][3])
                  +" Mbps\t\t"+str(rows[len(rows)-2][4])+" Mbps")

        x=len(rows)