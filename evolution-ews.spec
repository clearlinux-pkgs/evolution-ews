#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : evolution-ews
Version  : 3.32.1
Release  : 33
URL      : https://download.gnome.org/sources/evolution-ews/3.32/evolution-ews-3.32.1.tar.xz
Source0  : https://download.gnome.org/sources/evolution-ews/3.32/evolution-ews-3.32.1.tar.xz
Summary  : MS Exchange integration through Exchange Web Services
Group    : Development/Tools
License  : LGPL-2.1
Requires: evolution-ews-data = %{version}-%{release}
Requires: evolution-ews-lib = %{version}-%{release}
Requires: evolution-ews-license = %{version}-%{release}
Requires: evolution-ews-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : enchant-dev
BuildRequires : evolution-data-server-dev
BuildRequires : evolution-dev
BuildRequires : glib-dev
BuildRequires : intltool
BuildRequires : libmspack-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(camel-1.2)
BuildRequires : pkgconfig(evolution-calendar-3.0)
BuildRequires : pkgconfig(evolution-data-server-1.2)
BuildRequires : pkgconfig(evolution-mail-3.0)
BuildRequires : pkgconfig(evolution-shell-3.0)
BuildRequires : pkgconfig(libebackend-1.2)
BuildRequires : pkgconfig(libebook-1.2)
BuildRequires : pkgconfig(libecal-1.2)
BuildRequires : pkgconfig(libedata-book-1.2)
BuildRequires : pkgconfig(libedata-cal-1.2)
BuildRequires : pkgconfig(libedataserver-1.2)
BuildRequires : pkgconfig(libical)
BuildRequires : pkgconfig(libsoup-2.4)

%description
========================
1. BUILD
$ cd .../sources/evolution-ews
$ mkdir build
$ cd build
$ cmake -G "Unix Makefiles" \
-DCMAKE_INSTALL_PREFIX=/opt/evolution \
-DCMAKE_BUILD_TYPE=Release \
..
$ make -j
$ make -j install

%package data
Summary: data components for the evolution-ews package.
Group: Data

%description data
data components for the evolution-ews package.


%package lib
Summary: lib components for the evolution-ews package.
Group: Libraries
Requires: evolution-ews-data = %{version}-%{release}
Requires: evolution-ews-license = %{version}-%{release}

%description lib
lib components for the evolution-ews package.


%package license
Summary: license components for the evolution-ews package.
Group: Default

%description license
license components for the evolution-ews package.


%package locales
Summary: locales components for the evolution-ews package.
Group: Default

%description locales
locales components for the evolution-ews package.


%prep
%setup -q -n evolution-ews-3.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556997114
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1556997114
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/evolution-ews
cp COPYING %{buildroot}/usr/share/package-licenses/evolution-ews/COPYING
pushd clr-build
%make_install
popd
%find_lang evolution-ews

%files
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/camel-providers/libcamelews.urls

%files data
%defattr(-,root,root,-)
/usr/share/evolution-data-server/ews/windowsZones.xml
/usr/share/evolution/errors/module-ews-configuration.error
/usr/share/metainfo/org.gnome.Evolution-ews.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendews.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendews.so
/usr/lib64/evolution-data-server/camel-providers/libcamelews.so
/usr/lib64/evolution-data-server/registry-modules/module-ews-backend.so
/usr/lib64/evolution-ews/libcamelews-priv.so
/usr/lib64/evolution-ews/libevolution-ews.so
/usr/lib64/evolution/modules/module-ews-configuration.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/evolution-ews/COPYING

%files locales -f evolution-ews.lang
%defattr(-,root,root,-)

