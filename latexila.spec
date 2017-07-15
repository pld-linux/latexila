Summary:	Integrated LaTeX Environment for the GNOME desktop
Summary(pl.UTF-8):	Zintegrowane środowisko LaTeXowe dla GNOME
Name:		latexila
Version:	3.24.2
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/latexila/3.24/%{name}-%{version}.tar.xz
# Source0-md5:	6265082c9dc0efc4b44d836176de816e
URL:		https://wiki.gnome.org/Apps/LaTeXila
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.14
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gspell-devel >= 1.0
BuildRequires:	gtef-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtksourceview3-devel >= 3.24
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgee-devel >= 0.10
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.581
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.34
BuildRequires:	vala-gspell >= 1.0
BuildRequires:	vala-libgee >= 0.10
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.50
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.50
Requires:	gsettings-desktop-schemas
Requires:	gspell >= 1.0
Requires:	gtk+3 >= 3.20
Requires:	gtksourceview3 >= 3.24
Requires:	hicolor-icon-theme
Requires:	libgee >= 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeXila is an Integrated LaTeX Environment for GNOME.

%description -l pl.UTF-8
LaTeXila to zintegrowane środowisko LaTeXowe dla GNOME.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/latexila
%{_datadir}/appdata/org.gnome.latexila.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.latexila.gschema.xml
%{_datadir}/latexila
%{_desktopdir}/org.gnome.latexila.desktop
%{_iconsdir}/hicolor/*x*/apps/latexila.png
%{_iconsdir}/hicolor/scalable/apps/latexila.svg
%{_mandir}/man1/latexila.1*
%{_gtkdocdir}/latexila
%{_datadir}/dbus-1/services/org.gnome.latexila.service
