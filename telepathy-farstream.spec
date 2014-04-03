Summary:	Telepathy client to handle media streaming channels
Summary(pl.UTF-8):	Klient Telepathy do obsługi kanałów strumieni multimedialnych
Name:		telepathy-farstream
Version:	0.6.1
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-farstream/%{name}-%{version}.tar.gz
# Source0-md5:	53e3a69bdee7b301e2fdd2f2d254e385
URL:		http://telepathy.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	farstream-devel >= 0.2.0
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-doc >= 1.17
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel >= 0.19.0
Requires:	dbus-glib >= 0.74
Requires:	dbus-libs >= 0.60
Requires:	farstream >= 0.2.0
Requires:	glib2 >= 1:2.32.0
Requires:	telepathy-glib >= 0.19.0
Obsoletes:	python-telepathy-farstream
Obsoletes:	telepathy-farsight < 0.0.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-farstream is a Telepathy client that uses Farstream and
GStreamer to handle media streaming channels. It's used as a
background process by other Telepathy clients, rather than presenting
any user interface of its own.

%description -l pl.UTF-8
telepathy-farstream to klient Telepathy wykorzystujący biblioteki
Farstream oraz GStreamer do obsługi kanałów strumieni multimedialnych.
Jest używany jako proces w tle przez innych klientów Telepathy, sam
nie prezentuje żadnego interfejsu użytkownika.

%package devel
Summary:	Header files for telepathy-farstrean library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-farstrean
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.74
Requires:	farstream-devel >= 0.2.0
Requires:	glib2-devel >= 1:2.32.0
Requires:	gstreamer-devel >= 1.0
Requires:	telepathy-glib-devel >= 0.19.0
Obsoletes:	telepathy-farsight-devel < 0.0.20

%description devel
Header files for telepathy-farstream library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-farstrean.

%package static
Summary:	Static telepathy-farstream library
Summary(pl.UTF-8):	Statyczna biblioteka telepathy-farstream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	telepathy-farsight-static < 0.0.20

%description static
Static telepathy-farstream library.

%description static -l pl.UTF-8
Statyczna biblioteka telepathy-farstream.

%package apidocs
Summary:	telepathy-farstream library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki telepathy-farstream
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	telepathy-farsight-apidocs < 0.0.20
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
telepathy-farstream library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki telepathy-farstream.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-farstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-farstream.so.3
%{_libdir}/girepository-1.0/TelepathyFarstream-0.6.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-farstream.so
%{_includedir}/telepathy-1.0/telepathy-farstream
%{_pkgconfigdir}/telepathy-farstream.pc
%{_datadir}/gir-1.0/TelepathyFarstream-0.6.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy-farstream.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-farstream
