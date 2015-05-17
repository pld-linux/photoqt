# TODO
# - with GM?

Summary:	Simple but powerful Qt-based image viewer
Name:		photoqt
Version:	1.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
# Source0-md5:	bc0233279c86db39dc2482583697c9b3
URL:		http://photoqt.org/
BuildRequires:	GraphicsMagick-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	qt5-linguist
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
