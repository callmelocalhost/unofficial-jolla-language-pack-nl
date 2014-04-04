Name: unofficial-jolla-language-pack-nl
Version:  0.0.1
Release:  0.0.0.jolla
Summary: Unofficial Dutch language pack for Jolla  

Group: Qt/Qt    
License: GPL  
URL:  https://github.com/callmelocalhost/unofficial-jolla-language-pack-nl   
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Jarno de Wit

%define INSTALLDIR %{buildroot}/usr/share

%description
%{summary}

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{INSTALLDIR}
mkdir -p %{INSTALLDIR}/{translations,jolla-supported-languages}
cp -a usr/share/translations/*-nl_NL.qm %{INSTALLDIR}/translations/
cp -a usr/share/jolla-supported-languages/nl.conf %{INSTALLDIR}/jolla-supported-languages/

%clean
rm -rf ${buildroot}

%files
%{_datadir}/translations/*-nl_NL.qm
%{_datadir}/jolla-supported-languages/nl.conf

%changelog
* Fri Apr 04 2014 Jarno de Wit <jarno@callmelocalhost.com> 0.0.1-0.0.0.jolla
- Reworking Japanese translation to Dutch translation.
* Tue Mar 18 2014 Takahiro HASHIMOTO <kenya888@gmail.com> 0.0.1-0.0.0.jolla
- Initial RPM and source release
