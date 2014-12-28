Summary:	Integrated LaTeX Environment for the GNOME desktop
Name:		latexila
Version:	2.8.2
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/latexila/2.8/%{name}-%{version}.tar.xz
# Source0-md5:	a76efc40fdd84b7b37e06f70c2aaa349
URL:		http://projects.gnome.org/latexila/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	enchant-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	gtk+3-devel >= 3.6.0
BuildRequires:	gtksourceview3-devel >= 3.8.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgee0.6-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.581
BuildRequires:	vala >= 2:0.20.0
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.36.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.6.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeXila is an Integrated LaTeX Environment for GNOME.

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
	--disable-silent-rules

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
%{_datadir}/glib-2.0/schemas/org.gnome.latexila.gschema.xml
%{_datadir}/latexila
%{_desktopdir}/latexila.desktop
%{_mandir}/man1/latexila.1*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
