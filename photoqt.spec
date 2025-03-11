# TODO:
# VIDEO_MPV (upstream on by default) (BR: libmpv)
# LIBVIPS (upstream off by default) (BR: glib2, vips, vips-cpp)
#
# Conditional build:
%bcond_without	gmagick		# GraphicsMagick support

%define	qt_ver	5.9
Summary:	Simple but powerful Qt-based image viewer
Summary(pl.UTF-8):	Prosta, ale mająca duże możliwości przeglądarka obrazków oparta na Qt
Name:		photoqt
Version:	3.3
Release:	2
License:	GPL v2+
Group:		X11/Applications
#Source0Download: http://photoqt.org/down/
Source0:	https://photoqt.org/downloads/source/%{name}-%{version}.tar.gz
# Source0-md5:	d06988f0c505266bffbd187b6a4e8379
Patch0:		%{name}-pychromecast.patch
URL:		https://photoqt.org/
BuildRequires:	DevIL-devel
BuildRequires:	FreeImage-devel
%{?with_gmagick:BuildRequires:	GraphicsMagick-c++-devel}
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16
BuildRequires:	exiv2-devel >= 0.26
BuildRequires:	libarchive-devel
BuildRequires:	libraw-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt5-devel
BuildRequires:	pugixml-devel
BuildRequires:	python3-pychromecast
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
%patch -P 0 -p1

%build
%cmake -B build \
	-DEXIV2=ON \
	%{!?with_gmagick:-DGM=OFF} \
	-DVIDEO_MPV=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# no longer installed by default?
cp -p org.photoqt.PhotoQt.standalone.desktop $RPM_BUILD_ROOT%{_desktopdir}

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
%doc CHANGELOG README.md
%attr(755,root,root) %{_bindir}/photoqt
%{_datadir}/metainfo/org.photoqt.PhotoQt.metainfo.xml
%{_desktopdir}/org.photoqt.PhotoQt.desktop
%{_desktopdir}/org.photoqt.PhotoQt.standalone.desktop
%{_iconsdir}/hicolor/*x*/apps/org.photoqt.PhotoQt.png
