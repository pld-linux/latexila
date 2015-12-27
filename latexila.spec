Summary:	Integrated LaTeX Environment for the GNOME desktop
Summary(pl.UTF-8):	Zintegrowane środowisko LaTeXowe dla GNOME
Name:		latexila
Version:	3.18.2
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/latexila/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	9fe44a13d9a574a07dd70a9cd5cf5d6a
Patch0:		%{name}-gspell.patch
URL:		https://wiki.gnome.org/Apps/LaTeXila
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.12.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gspell-devel >= 0.2
BuildRequires:	gtk+3-devel >= 3.14
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtksourceview3-devel >= 3.18
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgee-devel >= 0.10
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.581
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.26
BuildRequires:	vala-gspell >= 0.2
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.40
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.40
Requires:	gsettings-desktop-schemas
Requires:	gspell >= 0.1
Requires:	gtk+3 >= 3.14
Requires:	gtksourceview3 >= 3.18
Requires:	hicolor-icon-theme
Requires:	libgee >= 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeXila is an Integrated LaTeX Environment for GNOME.

%description -l pl.UTF-8
LaTeXila to zintegrowane środowisko LaTeXowe dla GNOME.

%prep
%setup -q
%patch0 -p1

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
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/latexila
%{_datadir}/appdata/latexila.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.latexila.gschema.xml
%{_datadir}/latexila
%{_desktopdir}/latexila.desktop
%{_iconsdir}/hicolor/*x*/apps/latexila.png
%{_iconsdir}/hicolor/scalable/apps/latexila.svg
%{_mandir}/man1/latexila.1*
%{_gtkdocdir}/latexila
