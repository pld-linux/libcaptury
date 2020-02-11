Summary:	X11/GLX video capturing framework
Summary(pl.UTF-8):	Szkielet do przechwytywania obrazu z X11/GLX
Name:		libcaptury
Version:	0.3.0
Release:	5
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.debian.org/debian/pool/main/libc/libcaptury/%{name}_%{version}~svn158.orig.tar.gz
# Source0-md5:	6911c9965c6d765bd91200ab2f292634
Patch0:		unresolved.patch
URL:		http://rm-rf.in/libcaptury
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	capseo-devel >= 0.1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.17.2
BuildRequires:	xorg-lib-libX11-devel >= 1.0.0
BuildRequires:	xorg-lib-libXfixes-devel >= 1.0.0
Requires:	capseo >= 0.1.0
Requires:	xorg-lib-libX11 >= 1.0.0
Requires:	xorg-lib-libXfixes >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcaptury is a movie capturing framework with its primary goal to
capture the screen of OpenGL games (running on Linux systems).

The goal of this framework is to provide an easy to understand and an
easy to use C API that can be quickly integrated into already existing
applications that need capturing capabilities.

%description -l pl.UTF-8
libcaptury to szkielet do przechwytywania obrazu ruchomego, którego
głównym celem jest przechwytywanie ekranu z gier OpenGL (działających
pod Linuksem).

Celem tego szkieletu jest zapewnienie łatwego do zrozumienia oraz
prostego w użyciu API języka C, które można szybko zintegrować do
istniejących aplikacji wymagających przechwytywania obrazu.

%package devel
Summary:	Header files for libcaptury
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcaptury
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	capseo-devel >= 0.1.0
Requires:	libstdc++-devel
Requires:	xorg-lib-libX11-devel >= 1.0.0
Requires:	xorg-lib-libXfixes-devel >= 1.0.0

%description devel
Header files for libcaptury.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcaptury.

%package static
Summary:	Static libcaptury library
Summary(pl.UTF-8):	Biblioteka statyczna libcaptury
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcaptury library.

%description static -l pl.UTF-8
Biblioteka statyczna libcaptury.

%prep
%setup -q -n %{name}-%{version}~svn158.orig
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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libcaptury.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaptury.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaptury.so
%{_libdir}/libcaptury.la
%{_includedir}/captury
%{_pkgconfigdir}/libcaptury.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcaptury.a
