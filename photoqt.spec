# TODO
# - with GM?
# - optional (runtime) deps:
#  - XCFtools - https://github.com/j-jorge/xcftools
#  - libqpsd - https://github.com/Code-ReaQtor/libqpsd
#
# Conditional build:
%bcond_with	gm	# build with GraphicsMagic

%define	qt_ver	5.1
Summary:	Simple but powerful Qt-based image viewer
Summary(pl.UTF-8):	Prosta, ale mająca duże możliwości przeglądarka obrazków oparta na Qt
Name:		photoqt
Version:	1.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
# Source0-md5:	bc0233279c86db39dc2482583697c9b3
URL:		http://photoqt.org/
%{?with_gm:BuildRequires:	GraphicsMagick-devel}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake
BuildRequires:	exiv2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-linguist >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.596
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Multimedia >= %{qt_ver}
Requires:	Qt5Sql >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple but powerful Qt-based image viewer.

%description -l pl.UTF-8
Prosta, ale mająca duże możliwości przeglądarka obrazków oparta na Qt.

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
