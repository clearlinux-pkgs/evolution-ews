#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
Name     : evolution-ews
Version  : 3.52.1
Release  : 82
URL      : https://download.gnome.org/sources/evolution-ews/3.52/evolution-ews-3.52.1.tar.xz
Source0  : https://download.gnome.org/sources/evolution-ews/3.52/evolution-ews-3.52.1.tar.xz
Summary  : No detailed summary available
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
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libebackend-1.2)
BuildRequires : pkgconfig(libebook-1.2)
BuildRequires : pkgconfig(libecal-2.0)
BuildRequires : pkgconfig(libedata-book-1.2)
BuildRequires : pkgconfig(libedata-cal-2.0)
BuildRequires : pkgconfig(libedataserver-1.2)
BuildRequires : pkgconfig(libical-glib)
BuildRequires : pkgconfig(libsoup-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n evolution-ews-3.52.1
cd %{_builddir}/evolution-ews-3.52.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713795803
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713795803
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/evolution-ews
cp %{_builddir}/evolution-ews-%{version}/COPYING %{buildroot}/usr/share/package-licenses/evolution-ews/4df5d4b947cf4e63e675729dd3f168ba844483c7 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang evolution-ews
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/camel-providers/libcamelews.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelmicrosoft365.urls

%files data
%defattr(-,root,root,-)
/usr/share/evolution-data-server/ews/windowsZones.xml
/usr/share/evolution/errors/module-ews-configuration.error
/usr/share/metainfo/org.gnome.Evolution-ews.metainfo.xml

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendews.so
/V3/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendmicrosoft365.so
/V3/usr/lib64/evolution-data-server/calendar-backends/libecalbackendews.so
/V3/usr/lib64/evolution-data-server/calendar-backends/libecalbackendmicrosoft365.so
/V3/usr/lib64/evolution-data-server/camel-providers/libcamelews.so
/V3/usr/lib64/evolution-data-server/camel-providers/libcamelmicrosoft365.so
/V3/usr/lib64/evolution-data-server/registry-modules/module-ews-backend.so
/V3/usr/lib64/evolution-data-server/registry-modules/module-microsoft365-backend.so
/V3/usr/lib64/evolution-ews/libcamelews-priv.so
/V3/usr/lib64/evolution-ews/libevolution-ews.so
/V3/usr/lib64/evolution-ews/libevolution-microsoft365.so
/V3/usr/lib64/evolution/modules/module-ews-configuration.so
/V3/usr/lib64/evolution/modules/module-microsoft365-configuration.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendews.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendmicrosoft365.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendews.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendmicrosoft365.so
/usr/lib64/evolution-data-server/camel-providers/libcamelews.so
/usr/lib64/evolution-data-server/camel-providers/libcamelmicrosoft365.so
/usr/lib64/evolution-data-server/registry-modules/module-ews-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-microsoft365-backend.so
/usr/lib64/evolution-ews/libcamelews-priv.so
/usr/lib64/evolution-ews/libevolution-ews.so
/usr/lib64/evolution-ews/libevolution-microsoft365.so
/usr/lib64/evolution/modules/module-ews-configuration.so
/usr/lib64/evolution/modules/module-microsoft365-configuration.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/evolution-ews/4df5d4b947cf4e63e675729dd3f168ba844483c7

%files locales -f evolution-ews.lang
%defattr(-,root,root,-)

