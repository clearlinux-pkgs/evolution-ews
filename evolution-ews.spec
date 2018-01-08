#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : evolution-ews
Version  : 3.26.4
Release  : 11
URL      : https://download.gnome.org/sources/evolution-ews/3.26/evolution-ews-3.26.4.tar.xz
Source0  : https://download.gnome.org/sources/evolution-ews/3.26/evolution-ews-3.26.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: evolution-ews-lib
Requires: evolution-ews-data
Requires: evolution-ews-locales
BuildRequires : cmake
BuildRequires : enchant-dev
BuildRequires : evolution-data-server-dev
BuildRequires : evolution-dev
BuildRequires : glib-dev
BuildRequires : intltool
BuildRequires : libmspack-dev

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
Requires: evolution-ews-data

%description lib
lib components for the evolution-ews package.


%package locales
Summary: locales components for the evolution-ews package.
Group: Default

%description locales
locales components for the evolution-ews package.


%prep
%setup -q -n evolution-ews-3.26.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515420466
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1515420466
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang evolution-ews

%files
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/camel-providers/libcamelews.urls

%files data
%defattr(-,root,root,-)
/usr/share/appdata/evolution-ews.metainfo.xml
/usr/share/evolution-data-server/ews/windowsZones.xml
/usr/share/evolution/errors/module-ews-configuration.error

%files lib
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendews.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendews.so
/usr/lib64/evolution-data-server/camel-providers/libcamelews.so
/usr/lib64/evolution-data-server/registry-modules/module-ews-backend.so
/usr/lib64/evolution-ews/libcamelews-priv.so
/usr/lib64/evolution-ews/libevolution-ews.so
/usr/lib64/evolution/modules/module-ews-configuration.so

%files locales -f evolution-ews.lang
%defattr(-,root,root,-)

