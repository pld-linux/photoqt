# TODO
# - with GM?
# - optional (runtime) deps:
#  - XCFtools - https://github.com/j-jorge/xcftools
#  - libqpsd - https://github.com/Code-ReaQtor/libqpsd
%bcond_with	gm	# build with GraphicsMagic

%define	qtver	5.1
Summary:	Simple but powerful Qt-based image viewer
Name:		photoqt
Version:	1.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
# Source0-md5:	bc0233279c86db39dc2482583697c9b3
URL:		http://photoqt.org/
%{?with_gm:BuildRequires:	GraphicsMagick-devel}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Multimedia-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake
BuildRequires:	exiv2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.596
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple but powerful Qt-based image viewer.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DGM=NO \
	-DEXIV2=YES \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/photoqt
%{_desktopdir}/photoqt.desktop
%{_iconsdir}/hicolor/*/apps/photoqt.png
