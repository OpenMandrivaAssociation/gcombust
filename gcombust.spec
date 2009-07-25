%define name	gcombust
%define version	0.1.55
%define release	%mkrel 15

Name:		%{name}
Summary:	Disc writing frontend
Version:	%{version}
Release:	%{release}
Source0:	http://www.abo.fi/~jmunsin/gcombust/%{name}-%{version}.tar.bz2
Source4:	gcombust-0.1.55-de.po
Patch:		gcombust-0.1.55-getopt.patch
Patch1:		gcombust-0.1.55-defaults.patch
Patch2:		gcombust-0.1.55-gcc4.patch
Patch3:		gcombust-0.1.55-desktop.patch
Patch4:		gcombust-0.1.55-cdrkit.patch
Group:		Archiving/Cd burning
URL:		http://www.abo.fi/~jmunsin/gcombust/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	GPLv2+
Requires:	cdrkit cdrkit-genisoimage cdrkit-icedax
Requires:	cdlabelgen diffutils cdparanoia
BuildRequires:	imagemagick
BuildRequires:	gtk+-devel

%description
gcombust is a GTK+ 1.2 frontend for genisofs, wodim, icedax and
cdlabelgen. It's written in C. It has primitive support for
controlling the directory (root) structure and size of image without
copying files/symlinking or writing 10 lines of arguments and can
maximize disk by hinting which directories/files to use.

%prep
rm -rf %{buildroot}

%setup -q -n gcombust-%{version}
%patch -p1 -b .getopt
%patch1 -p1 -b .defaults
%patch2 -p1
%patch3 -p1 -b .desktop
%patch4 -p1 -b .cdrkit
cp %SOURCE4 po/de.po

%build
libtoolize --install --force
%configure2_5x
%make 

%install
[ "%{buildroot}" != "/"] && [ -d %{buildroot} ] && rm -rf %{buildroot}

%makeinstall

%find_lang %{name}

#icon
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert gcombust.xpm %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert gcombust.xpm -scale 32 %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert gcombust.xpm -scale 16 %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post  
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS TODO ChangeLog INSTALL NEWS README* THANKS ABOUT-NLS
%{_bindir}/gcombust
%{_datadir}/pixmaps/gcombust.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/gcombust.desktop

