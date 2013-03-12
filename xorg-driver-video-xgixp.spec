Summary:	X.org video drivers for XGI XP adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych XGI XP
Name:		xorg-driver-video-xgixp
Version:	1.8.1
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-xgixp-%{version}.tar.bz2
# Source0-md5:	590ec61b6368fee3805623958eb843cb
Patch0:		build.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.2
Provides:	xorg-driver-video
Requires:	xorg-xserver-libdri >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	XFree86-driver-xgi < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video drivers for XGI XP adapters:
- Volari 8300

%description -l pl.UTF-8
Sterowniki obrazu X.org do kart graficznych XGI XP:
- Volari 8300

%prep
%setup -q -n xf86-video-xgixp-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/xgixp_drv.so
%{_mandir}/man4/xgixp.4*
