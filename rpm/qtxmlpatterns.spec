Name:       qt5-qtxmlpatterns
Summary:    Qt XML Patterns library
Version:    5.6.3
Release:    1%{?dist}
License:    (LGPLv2 or LGPLv3) with exception or Qt Commercial
URL:        https://github.com/sailfishos/qtxmlpatterns
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
The Qt XML Patterns module provides support for XPath, XQuery, XSLT,
and XML Schema validation.

%package devel
Summary:    Qt XML Patterns - development files
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
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
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

%fdupes %{buildroot}/%{_includedir}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.LGPLv*
%license LGPL_EXCEPTION.txt
%{_libdir}/libQt5XmlPatterns.so.5
%{_libdir}/libQt5XmlPatterns.so.5.*
%{_qt5_bindir}/*

%files devel
%{_libdir}/libQt5XmlPatterns.so
%{_libdir}/libQt5XmlPatterns.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/
%{_datadir}/qt5/mkspecs/
%{_libdir}/cmake/
