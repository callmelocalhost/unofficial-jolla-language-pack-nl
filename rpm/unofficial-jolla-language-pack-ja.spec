Name: unofficial-jolla-language-pack-ja
Version:	0.0.1
Release:	0.0.0.jolla
Summary: Unofficial Japanese language pack for Jolla	

Group: Qt/Qt		
License: GPL	
URL: http://qtquick.me		
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Takahiro HASHIMOTO

%define INSTALLDIR %{buildroot}/usr/share

%description
%{summary}

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{INSTALLDIR}
mkdir -p %{INSTALLDIR}/{translations,jolla-supported-languages}
cp -a usr/share/translations/*-ja_JP.qm %{INSTALLDIR}/translations/
cp -a usr/share/jolla-supported-languages/ja.conf %{INSTALLDIR}/jolla-supported-languages/

%clean
rm -rf ${buildroot}

%files
%{_datadir}/translations/*-ja_JP.qm
%{_datadir}/jolla-supported-languages/ja.conf

%changelog
* Tue Mar 18 2014 Takahiro HASHIMOTO <kenya888@gmail.com> 0.0.1-0.0.0.jolla
- Initial RPM and source release
