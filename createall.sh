#!/bin/sh

TOOLSDIR=tools
OPT=

if [ x"$TSLANG" == "x" ]; then
   TSLANG=ja_JP
fi 

if [ x"$1" == "x-f" ]; then
    OPT=$1
fi

sh ${TOOLSDIR}/inittx.sh $OPT

if [ x"$OPT" == "x-f" ]; then
    sh ${TOOLSDIR}/fetchts.sh $OPT $TSLANG
fi

sh ${TOOLSDIR}/createqm.sh
sh ${TOOLSDIR}/createrpm.sh
