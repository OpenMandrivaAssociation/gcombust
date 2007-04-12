%define name gcombust
%define version 0.1.55
%define release %mkrel 11

Name: %{name}
Summary: Gcombust is a burning cd frontend
Version: %{version}
Release: %{release}
Source: http://www.abo.fi/~jmunsin/gcombust/%{name}-%{version}.tar.bz2
Source4: gcombust-0.1.55-de.po
Patch: gcombust-0.1.55-getopt.patch
Patch1: gcombust-0.1.55-defaults.patch
Patch2: gcombust-0.1.55-gcc4.patch
Patch3: gcombust-0.1.55-desktop.patch
Patch4: gcombust-0.1.55-cdrkit.patch
Group: Archiving/Cd burning
BuildRequires: gtk+-devel
URL: http://www.abo.fi/~jmunsin/gcombust/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: GPL
Requires: cdrkit cdrkit-genisoimage cdrkit-icedax
Requires: cdlabelgen diffutils cdparanoia
BuildRequires: ImageMagick

%description
gcombust is a gtk+ frontend for genisofs, wodim, icedax and
cdlabelgen. It's written in C. It has primitive support for
controlling the directory (root) structure and size of image without
copying files/symlinking or writing 10 lines of arguments and can
maximize disk by hinting which directories/files to use.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n gcombust-%{version}
%patch -p1 -b .getopt
%patch1 -p1 -b .defaults
%patch2 -p1
%patch3 -p1 -b .desktop
%patch4 -p1 -b .cdrkit
cp %SOURCE4  po/de.po

%build
%configure2_5x
%make 

%install
[ "$RPM_BUILD_ROOT" != "/"] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%makeinstall

%find_lang %{name}

# Menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/%{name}" needs="X11" \
icon="%{name}.png" section="System/Archiving/CD Burning" \
title="GCombust" longtitle="Gtk+ frontend for Cd burning" xdg="true"
EOF

#icon
install -d $RPM_BUILD_ROOT/%{_iconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
install -d $RPM_BUILD_ROOT/%{_miconsdir}
convert gcombust.xpm $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
convert gcombust.xpm -scale 32x32 $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
convert gcombust.xpm -scale 16x16 $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%post  
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS TODO COPYING ChangeLog INSTALL NEWS README* THANKS ABOUT-NLS
%{_bindir}/gcombust
%{_datadir}/pixmaps/gcombust.xpm
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/gcombust.desktop


