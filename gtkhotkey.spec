%define major 1

%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		gtkhotkey
Version:	0.2.1
Release:	1
Summary:	Platform Independent Hotkey Handling for GTK+ Applications
License:	LGPLv3+
Group:		System/Libraries
Url:		http://launchpad.net/gtkhotkey/
Source0:		%{name}-%{version}.tar.bz2
Patch0:		gtkhotkey-glib-2.31.patch
Patch1:		gtkhotkey-0.2.1-linkage.patch
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
GtkHotkey is simple library offering a platform independent way for GTK+
applications to manage and bind desktop-wide hotkeys.

%package -n %{libname}
Summary:	Platform Independent Hotkey Handling for GTK+ Applications
Group:		System/Libraries

%description -n %{libname}
GtkHotkey is simple library offering a platform independent way for GTK+
applications to manage and bind desktop-wide hotkeys.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/GNOME and GTK+
Requires:	pkgconfig(glib-2.0)
Requires:	pkgconfig(gtk+-2.0)
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
GtkHotkey is simple library offering a platform independent way for GTK+
applications to manage and bind desktop-wide hotkeys.  This package contains
all necessary include files and libraries needed to develop applications that
require these.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_prefix}/doc

%files -n %{libname}
%doc AUTHORS COPYING NEWS README
%{_libdir}/libgtkhotkey.so.%{major}*

%files -n %{develname}
%{_datadir}/gtk-doc/html/gtkhotkey
%{_includedir}/gtkhotkey-1.0/
%{_libdir}/libgtkhotkey.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jun 21 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2.1-1
+ Revision: 806640
- Update BuildRequires
- Add patch1 to fix linkage
- imported package gtkhotkey

