import serial
import MySQLdb
import RPi.GPIO as r
import time as t

r.setmode(r.BCM)
buzzer=<pin_number>
buzzer1=<pin_number>
r.setup(buzzer,r.OUT)
r.setup(buzzer1,r.OUT)
r.setup(22,r.IN)
r.setup(23,r.IN)
r.setup(24,r.IN)
r.setup(27,r.IN)
r.setup(4,r.OUT)
flag=0
def read_rfid():
    ser=serial.Serial("/dev/ttyAMA0")
    ser.baudrate = 9600
    data=ser.read(4)
    ser.close()
    return data
db=MySQLdb.connect("localhost","root","rev","inventory")
cur = db.cursor()
id = read_rfid()
print(id)
cur.execute("select * from <table_name> where voter_id= %s",(id,);)
for i in cur.fetchall:
    voter_id= str(i[1])
    voter_name=str(i[2])
    chk=int(i[7])
    if(chk==1)
    {
        r.output(buzzer,r.HIGH)
        sleep(10)
    }
    elif(chk==0)
    {
        r.output(buzzer1,r.HIGH)
        sleep(10)
        flag=1
        
        
    }
def get_vote():
    if(flag==1):
        b1=b2=b3=b4=False
        while(b1== False and b2==False and b3==False and b4==False):
            b1=r.input(22)
            b2=r.input(23)
            b3=r.input(24)
            b4=r.input(27)
