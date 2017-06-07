# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific aliases and functions
alias php='/home/rd/viw/drive/bin/php'
alias hadoop='/home/rd/share/hadoop/bin/hadoop';
alias dcs='php -f /home/rd/tools/dcs/dcs.php'

alias nn_tools='/home/rd/tools/nn_tools';

alias webcrawler='php -f /home/rd/tools/webcrawler/bin/wc.php'
alias wc_tools='php -f /home/rd/tools/webcrawler/bin/wc_tools.php'
alias wc_seek='php -f /home/rd/tools/webcrawler/bin/wc_seek.php'
alias vp_tools='php -f /home/rd/tools/webcrawler/bin/vp_tools.php'
alias wc2vp='php -f /home/rd/tools/webcrawler/bin/wc2vp.php'

alias webcrawler_v1='php -f /home/rd/tools/webcrawler/bin/wc_v1.php'
alias wc_seek_v1='php -f /home/rd/tools/webcrawler/bin/wc_seek_v1.php'

alias maxent='/home/rd/zhanghua/MLtools/maxent_use/bin/maxent'

alias distribute_client='python /home/rd/share/dcs/distribute_client.py'

alias ant='/home/rd/share/ant.1.9.3/bin/ant'
alias sshpass='/home/rd/share/sshpass-1.05/bin/sshpass'
alias php='/home/rd/viw/php/bin/php'

alias scala='/home/rd/share/scala-2.12.0-M3/bin/scala'
alias cmake='/home/rd/share/cmake/bin/cmake'

alias grep='grep --color=auto'

CRFPP_HOME_PATH=/home/rd/zhanghua/MLtools/crfpp_use
export PATH=${CRFPP_HOME_PATH}/bin:${PATH}
export C_INCLUDE_PATH=${CRFPP_HOME_PATH}/include:${C_INCLUDE_PATH}
export CPLUS_INCLUDE_PATH=${CRFPP_HOME_PATH}/include:${CPLUS_INCLUDE_PATH}
export LIBRARY_PATH=${CRFPP_HOME_PATH}/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=${CRFPP_HOME_PATH}/lib:$LD_LIBRARY_PATH

OPENBLAS_HOME_PATH=/home/rd/share/open-BLAS
export PATH=${OPENBLAS_HOME_PATH}/bin:${PATH}
export C_INCLUDE_PATH=${OPENBLAS_HOME_PATH}/include:${C_INCLUDE_PATH}
export CPLUS_INCLUDE_PATH=${OPENBLAS_HOME_PATH}/include:${CPLUS_INCLUDE_PATH}
export LIBRARY_PATH=${OPENBLAS_HOME_PATH}/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=${OPENBLAS_HOME_PATH}/lib:$LD_LIBRARY_PATH
export OPENBLAS=${OPENBLAS_HOME_PATH}

export LD_LIBRARY_PATH=/home/rd/gcc-build/gcc.4.8.5/lib64:/home/rd/gcc-build/gcc.4.8.5/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/lib:/lib64:$LD_LIBRARY_PATH


# added by Anaconda2 2.4.1 installer
export PATH="/home/rd/share/python/anaconda2/bin:$PATH"
#export PKG_CONFIG_PATH=/home/rd/share/python/anaconda2/lib/pkgconfig/:${PKG_CONFIG_PATH}
export PYTHON_LIBRARIES=/home/rd/share/python/anaconda2/lib/libpython2.7.so:${PYTHON_LIBRARIES}
export PYTHON_INCLUDE_DIRS=/home/rd/share/python/anaconda2/include/python2.7/:${PYTHON_INCLUDE_DIRS}

# pixman
export PIXMAN=/data/rd/share/open-CV/pixman
export CPLUS_INCLUDE_PATH=${PIXMAN}/include:${CPLUS_INCLUDE_PATH}
export LD_LIBRARY_PATH=${PIXMAN}/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=${PIXMAN}/lib/pkgconfig:$PKG_CONFIG_PATH

# cario
export CAIRO=/home/rd/share/open-CV/cairo
export PATH=${CAIRO}/bin:${PATH}
export CPLUS_INCLUDE_PATH=${CAIRO}/include:${CPLUS_INCLUDE_PATH}
export LD_LIBRARY_PATH=${CAIRO}/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=${CAIRO}/lib/pkgconfig:$PKG_CONFIG_PATH

#libpng
export LIBPNG=/home/rd/share/open-CV/libpng
export PATH=${LIBPNG}/bin:${PATH}
export CPLUS_INCLUDE_PATH=${LIBPNG}/include:${CPLUS_INCLUDE_PATH}
export LD_LIBRARY_PATH=${LIBPNG}/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=${LIBPNG}/lib/pkgconfig:$PKG_CONFIG_PATH

#opencv
OPENCV_HOME_PATH=/home/rd/share/open-CV/opencv
export PATH=${OPENCV_HOME_PATH}/bin:${PATH}
export C_INCLUDE_PATH=${OPENCV_HOME_PATH}/include:${C_INCLUDE_PATH}
export CPLUS_INCLUDE_PATH=${OPENCV_HOME_PATH}/include:${CPLUS_INCLUDE_PATH}
export LIBRARY_PATH=${OPENCV_HOME_PATH}/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=${OPENCV_HOME_PATH}/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=${OPENCV_HOME_PATH}/lib/pkgconfig/:${PKG_CONFIG_PATH}

alias l='ls -lthr'

abspath ()
{
     who=`whoami`;
     cwd=`pwd`;
     if [[ "$1" == "/"* ]]; then
         path=$1;
     else
         path=$cwd/$1;
     fi;
     echo $who@$HOSTNAME:$path
}
