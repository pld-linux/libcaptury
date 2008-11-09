Summary:	X11/GLX video capturing framework
Name:		libcaptury
Version:	0.3.0
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://ftp.de.debian.org/debian/pool/main/libc/libcaptury/%{name}_%{version}~svn158.orig.tar.gz
# Source0-md5:	6911c9965c6d765bd91200ab2f292634
URL:		http://rm-rf.in/libcaptury
BuildRequires:	capseo-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcaptury is a movie capturing framework with its primary goal to
capture the screen of OpenGL games (running on Linux systems).

The goal of this framework is to provide an easy to understand and an
easy to use C API that can be quickly integrated into already existing
applications that need capturing capabilities.

%package devel
Summary:	Header files and develpment documentation for libcaptury
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libcaptury
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for libcaptury.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libcaptury.

%package static
Summary:	Static libcaptury library
Summary(pl.UTF-8):	Biblioteka statyczna libcaptury
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libcaptury library.

%prep
%setup -q -n %{name}-%{version}~svn158.orig

%build
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/captury
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
