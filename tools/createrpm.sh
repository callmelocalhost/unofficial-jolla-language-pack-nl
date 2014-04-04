#!/bin/sh

if [ x"$TSLANG" == "x" -o x"TSLANG" == "xja_JP" ]; then
    TSLANG=ja
fi

PKGNAME=unofficial-jolla-language-pack-${TSLANG}

if [ x"${TOPDIR}" == x ]; then
    TOPDIR=$HOME/rpmbuild
fi 

if [ ! -d ${TOPDIR} ]; then
    rm -rf ${TOPDIR}
    mkdir ${TOPDIR}
fi

for n in SOURCES RPMS SRPMS BUILD BUILDROOT SPECS
do
    if [ ! -d ${TOPDIR}/$n ]; then
                mkdir ${TOPDIR}/$n
    fi  
done

SOURCEFILE=${TOPDIR}/SOURCES/${PKGNAME}.tar.bz2

if [ ! -e ${SOURCEFILE} ]; then
    cd ..
    if [ "$TSLANG" != "ja" ]; then
        rm -rf ${PKGNAME}
        cp -a unofficial-jolla-language-pack-ja ${PKGNAME}
    fi

    tar jcvf ${TOPDIR}/SOURCES/${PKGNAME}.tar.bz2  --exclude rpmbuild --exclude .git --exclude .tx ./${PKGNAME}
    cd ${PKGNAME}
fi

rpmbuild --define "_topdir ${TOPDIR}" -ba rpm/unofficial-jolla-language-pack-${TSLANG}.spec --target noarch

ls -l ${TOPDIR}/RPMS/noarch
ls -l ${TOPDIR}/SRPMS

