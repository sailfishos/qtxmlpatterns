Name:       qt5-qtxmlpatterns
Summary:    Qt XML Patterns library
Version:    5.6.3
Release:    1
License:    (LGPLv2 or LGPLv3) with exception or Qt Commercial
URL:        https://www.qt.io
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the XMLPatterns library


%package devel
Summary:    Qt XML Patterns - development files
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the XMLPatterns library development files


#### Build section

%prep
%setup -q -n %{name}-%{version}/%{name}


%build
touch .git
%qmake5

%make_build

%install
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_qt5_includedir}/Qt

#
%fdupes %{buildroot}/%{_includedir}



%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%license LICENSE.LGPLv*
%license LGPL_EXCEPTION.txt
%{_qt5_libdir}/libQt5XmlPatterns.so.5
%{_qt5_libdir}/libQt5XmlPatterns.so.5.*
%{_qt5_bindir}/*

%files devel
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5XmlPatterns.so
%{_qt5_libdir}/libQt5XmlPatterns.prl
%{_qt5_libdir}/pkgconfig/*
%{_qt5_includedir}
%{_qt5_archdatadir}/mkspecs/
%{_libdir}/cmake/


#### No changelog section, separate $pkg.changes contains the history
