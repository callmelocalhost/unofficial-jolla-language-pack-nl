Name:           unofficial-jolla-translations-nl
Version:        0.8.2
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
* Sat Sep 25 2015 Jarno de Wit <jarno@callmelocalhost.com> - 0.8.2
- Bugfixes;
- Some more translated strings;
* Sat Sep 12 2015 Jarno de Wit <jarno@callmelocalhost.com> - 0.8.1
- Some more translated strings added
* Sat Sep 12 2015 Jarno de Wit <jarno@callmelocalhost.com> - 0.8.0
- New translation for v1.1.9.28
* Fri Jan 15 2015 Jarno de Wit <jarno@callmelocalhost.com> - 0.7.0
- New translation souces
* Wed Jul 23 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.6.1-1
- Double check file names
* Wed Jul 23 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.6-1
- New translation souces 1.0.7.x
* Tue Apr 22 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.5.1-1
- Switch from nl to nl_NL
* Sun Apr 20 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.5-1
- First complete translated and reviewed release.
* Mon Apr 14 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.4.1-1
- Bugfix
* Sat Apr 12 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.4-1
- Bring up to date with Sailfish 1.0.5.16 (Paarlampi)
- Improvements on over 50% of the files, not gonna name them all;
* Tue Apr 10 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.3-1
- Fixes in sailfishsilica-qt5;
- Improvements on lipstick-jolla-home, lipstick-jolla-home-facebook, sailfishsilica-qt5, contacts, jolla-email, settings-bluethooth, settings-accounts, gallery;
* Thu Apr 08 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.2-1
- Fixes on some really anoying translation errors;
- Improvements on alarm-ui, calendar, lipstick-jolla-home-twitter, lipstick-jolla-home-facebook, lipstick, lipstick-jolla-home, jolla-email, sailfishsilica-qt5;
* Mon Apr 07 2014 Jarno de Wit <jarno@callmelocalhost.com> - 0.1-1
- Initial release;
