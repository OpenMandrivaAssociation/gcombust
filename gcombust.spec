%define name	gcombust
%define version	0.1.55
%define release	18

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



%changelog
* Wed Jul 27 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.55-17mdv2012.0
+ Revision: 691842
- rebuild

* Sat Jul 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.55-16mdv2011.0
+ Revision: 399733
- fix build
- fix naming of patch 0

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1.55-14mdv2009.0
+ Revision: 245738
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.55-12mdv2008.1
+ Revision: 136426
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.1.55-12mdv2008.0
+ Revision: 91134
- rebuild for 2008
- don't package COPYING
- fd.o icons
- update xdg menu patch - drop X-Mandriva category, correct icon location, drop obsolete Encoding tag
- drop old menu
- new license policy
- spec clean


* Sun Jan 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.55-11mdv2007.0
+ Revision: 114645
- update patch 4 for the new burnfree option in wodim

* Sun Jan 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.55-10mdv2007.1
+ Revision: 105284
- fix description

* Sun Jan 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.55-9mdv2007.1
+ Revision: 105267
- Import gcombust

* Sun Jan 07 2007 Götz Waschk <waschk@mandriva.org> 0.1.55-9mdv2007.1
- fix patch 0
- support cdrkit
- update German translation

* Wed Aug 02 2006 Götz Waschk <waschk@mandriva.org> 0.1.55-8mdv2007.0
- fix desktop file

* Wed Aug 02 2006 Götz Waschk <waschk@mandriva.org> 0.1.55-7mdv2007.0
- xdg menu

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.1.55-6mdk
- Rebuild

* Fri May 20 2005 Götz Waschk <waschk@mandriva.org> 0.1.55-5mdk
- fix build with gcc 4

* Thu Sep 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.55-4mdk
- fix patch 1

* Sun Sep 05 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.55-3mdk
- use ImageMagick for the icons
- adjust some default values

* Fri Sep 03 2004 Marcel Pol <mpol@mandrake.org> 0.1.55-2mdk
- fix menusection

* Wed May 12 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.55-1mdk
- patch: load selection file from command line
- move desktop entry file
- update german translation
- macro fix
- new version

