Name:           unofficial-jolla-translations-nl
Version:        0.2
Release:        1%{?dist}
Summary:        Dutch translations of OS for Jolla
Group:          System/Base

License:        BSD
URL:            http://www.jolla.com/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  qt5-qttools-linguist

BuildArch: noarch

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc
%{_datadir}/translations/*.qm
%{_datadir}/jolla-supported-languages/nl.conf



%changelog
* Thu Apr 08 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.2-1
- Fixes on some really anoying translation errors
- Improvements on alarm-ui, calendar, lipstick-jolla-home-twitter, lipstick-jolla-home-facebook, lipstick, lipstick-jolla-home, jolla-email, sailfishsilica-qt5 
* Mon Apr 07 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.1-1
- Initial release
