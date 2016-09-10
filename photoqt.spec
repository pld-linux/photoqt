#
# Conditional build:
%bcond_without	gmagick		# GraphicsMagick support

%define	qt_ver	5.3
Summary:	Simple but powerful Qt-based image viewer
Summary(pl.UTF-8):	Prosta, ale mająca duże możliwości przeglądarka obrazków oparta na Qt
Name:		photoqt
Version:	1.4.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
#Source0Download: http://photoqt.org/down/
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
# Source0-md5:	f708ccf9f4e01ad3fac2e893c4f14014
URL:		http://photoqt.org/
%{?with_gmagick:BuildRequires:	GraphicsMagick-c++-devel}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.8
BuildRequires:	exiv2-devel
BuildRequires:	libraw-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-linguist >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.596
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Sql >= %{qt_ver}
Requires:	Qt5Sql-sqldriver-sqlite3 >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	hicolor-icon-theme
# psd imageformat plugin
Suggests:	libqpsd-qt5
Suggests:	xcftools
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
%cmake .. \
	%{!?with_gmagick:-DGM=OFF} \
	-DEXIV2=ON

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
%{_datadir}/appdata/photoqt.appdata.xml
%{_desktopdir}/photoqt.desktop
%{_iconsdir}/hicolor/*x*/apps/photoqt.png
