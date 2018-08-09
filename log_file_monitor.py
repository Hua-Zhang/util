
# 不能运行，只是示例代码

# 第一种做法
logfile=’access.log’

command=’tail -f ‘+logfile+’|grep “timeout”‘

popen=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

while True:

   line=popen.stdout.readline().strip()

   print line
   
   
# 第二种做法
import time

file = open(‘access.log’)

while 1:

   where = file.tell()

   line = file.readline()

   if not line:

       time.sleep(1)

       file.seek(where)

   else:

       print line
       
# 第三种做法
import time

def follow(thefile):

   thefile.seek(0,2)

   while True:

       line = thefile.readline()

       if not line:

           time.sleep(0.1)

           continue

       yield line

if __name__ == ‘__main__’:

   logfile = open(“access-log”,”r”)

   loglines = follow(logfile)

   for line in loglines:

       print line
