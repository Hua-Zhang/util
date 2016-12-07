# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs
export  JAVA_HOME=/home/rd/share/jdk1.8.0_65
export  JRE_HOME=${JAVA_HOME}/jre
export  CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib

PATH=/home/rd/share/git.2.7.2/bin:$HOME/bin:${JAVA_HOME}/bin:$PATH

export PATH

# C
# export C_INCLUDE_PATH=XXXX:$C_INCLUDE_PATH
# CPP
#export CPLUS_INCLUDE_PATH=/home/rd/zhanghua/MLtools/maxent_use/include/:$CPLUS_INCLUDE_PATH

#动态链接库搜索路径：
export LD_LIBRARY_PATH=/home/rd/zhanghua/MLtools/maxent_use/lib/:$LD_LIBRARY_PATH
#静态链接库搜索路径：
export LIBRARY_PATH=/home/rd/zhanghua/MLtools/maxent_use/lib/:$LIBRARY_PATH
