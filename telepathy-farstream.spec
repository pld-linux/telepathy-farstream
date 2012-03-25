Summary:	Telepathy client to handle media streaming channels
Name:		telepathy-farstream
Version:	0.2.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-farstream/%{name}-%{version}.tar.gz
# Source0-md5:	9a5de84f1f4bb4505cc982b4a7fea539
URL:		http://telepathy.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	farstream-devel >= 0.1.0
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gtk-doc >= 1.17
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.5
BuildRequires:	python-gstreamer-devel >= 0.10.10
BuildRequires:	python-pygobject-devel >= 2.12.0
BuildRequires:	telepathy-glib-devel >= 0.17.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-farstream is a Telepathy client that uses Farsight and
GStreamer to handle media streaming channels. It's used as a
background process by other Telepathy clients, rather than presenting
any user interface of its own.

%package devel
Summary:	Header files for telepathy-farstrean library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-farstrean
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.74
Requires:	farstream-devel >= 0.1.0
Requires:	glib2-devel >= 1:2.30.0
Requires:	gstreamer-devel
Requires:	telepathy-glib-devel >= 0.17.5

%description devel
Header files for telepathy-farstream library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-farstrean.

%package static
Summary:	Static telepathy-farstream library
Summary(pl.UTF-8):	Statyczna biblioteka telepathy-farstream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static telepathy-farstream library.

%description static -l pl.UTF-8
Statyczna biblioteka telepathy-farstream.

%package apidocs
Summary:	telepathy-farstream library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki telepathy-farstream
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
telepathy-farstream library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki telepathy-farstream.

%package -n python-telepathy-farstream
Summary:	telepathy-farstream Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do telepathy-farstream
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-telepathy-farstream
telepathy-farstream Python bindings.

%description -n python-telepathy-farstream -l pl.UTF-8
Wiązania Pythona do telepathy-farstream.

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

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la} \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-farstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-farstream.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-farstream.so
%{_includedir}/telepathy-1.0/telepathy-farstream
%{_pkgconfigdir}/telepathy-farstream.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy-farstream.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-farstream

%files -n python-telepathy-farstream
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/tpfarstream.so
