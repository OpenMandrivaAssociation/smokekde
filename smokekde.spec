%define with_kdepimlibs 1

Name:		smokekde
Summary:	KDE4 bindings for SMOKE
Version:	4.12.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	smokeqt-devel >= 1:%{version}
%if %{with_kdepimlibs}
BuildRequires:	kdepimlibs4-devel >= 2:%{version}
%endif
BuildRequires:	okular-devel >= 2:%{version}
BuildRequires:	kate-devel >= 1:%{version}
BuildRequires:	qscintilla-qt4-devel
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(libattica)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(soprano)

%description
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine).

#-----------------------------------------------------------------------------

%define smokesopranoclient_major 3
%define libsmokesopranoclient %mklibname smokesopranoclient %{smokesopranoclient_major}

%package -n %{libsmokesopranoclient}
Summary:	Soprano bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokesopranoclient}
Soprano bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesopranoclient}
%{_kde_libdir}/libsmokesopranoclient.so.%{smokesopranoclient_major}*

#-----------------------------------------------------------------------------

%define smokesopranoserver_major 3
%define libsmokesopranoserver %mklibname smokesopranoserver %{smokesopranoserver_major}

%package -n %{libsmokesopranoserver}
Summary:	Soprano bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokesopranoserver}
Soprano bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesopranoserver}
%{_kde_libdir}/libsmokesopranoserver.so.%{smokesopranoserver_major}*

#------------------------------------------------------------

%define smokekate_major 3
%define libsmokekate %mklibname smokekate %{smokekate_major}

%package -n %{libsmokekate}
Summary:	Kate bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekate}
Kate bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekate}
%{_kde_libdir}/libsmokekate.so.%{smokekate_major}*

#-----------------------------------------------------------------------------

%define smokekdecore_major 3
%define libsmokekdecore %mklibname smokekdecore %{smokekdecore_major}

%package -n %{libsmokekdecore}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekdecore}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekdecore}
%{_kde_libdir}/libsmokekdecore.so.%{smokekdecore_major}*

#-----------------------------------------------------------------------------

%define smokekdeui_major 3
%define libsmokekdeui %mklibname smokekdeui %{smokekdeui_major}

%package -n %{libsmokekdeui}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekdeui}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekdeui}
%{_kde_libdir}/libsmokekdeui.so.%{smokekdeui_major}*

#-----------------------------------------------------------------------------

%define smokekfile_major 3
%define libsmokekfile %mklibname smokekfile %{smokekfile_major}

%package -n %{libsmokekfile}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekfile}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekfile}
%{_kde_libdir}/libsmokekfile.so.%{smokekfile_major}*

#-----------------------------------------------------------------------------

%define smokekio_major 3
%define libsmokekio %mklibname smokekio %{smokekio_major}

%package -n %{libsmokekio}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekio}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekio}
%{_kde_libdir}/libsmokekio.so.%{smokekio_major}*

#-----------------------------------------------------------------------------

%define smokeknewstuff2_major 3
%define libsmokeknewstuff2 %mklibname smokeknewstuff2_ %{smokeknewstuff2_major}

%package -n %{libsmokeknewstuff2}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeknewstuff2}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeknewstuff2}
%{_kde_libdir}/libsmokeknewstuff2.so.%{smokeknewstuff2_major}*

#-----------------------------------------------------------------------------

%define smokeknewstuff3_major 3
%define libsmokeknewstuff3 %mklibname smokeknewstuff3_ %{smokeknewstuff3_major}

%package -n %{libsmokeknewstuff3}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeknewstuff3}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeknewstuff3}
%{_kde_libdir}/libsmokeknewstuff3.so.%{smokeknewstuff3_major}*

#-----------------------------------------------------------------------------

%define smokekhtml_major 3
%define libsmokekhtml %mklibname smokekhtml %{smokekhtml_major}

%package -n %{libsmokekhtml}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekhtml}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekhtml}
%{_kde_libdir}/libsmokekhtml.so.%{smokekhtml_major}*

#-----------------------------------------------------------------------------

%define smokektexteditor_major 3
%define libsmokektexteditor %mklibname smoketexteditor %{smokektexteditor_major}

%package -n %{libsmokektexteditor}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokektexteditor}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokektexteditor}
%{_kde_libdir}/libsmokektexteditor.so.%{smokektexteditor_major}*

#-----------------------------------------------------------------------------

%define smokekparts_major 3
%define libsmokekparts %mklibname smokekparts %{smokekparts_major}

%package -n %{libsmokekparts}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekparts}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekparts}
%{_kde_libdir}/libsmokekparts.so.%{smokekparts_major}*

#-----------------------------------------------------------------------------

%define smokekutils_major 3
%define libsmokekutils %mklibname smokekutils %{smokekutils_major}

%package -n %{libsmokekutils}
Summary:	KDE4 bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokekutils}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekutils}
%{_kde_libdir}/libsmokekutils.so.%{smokekutils_major}*

#-----------------------------------------------------------------------------

%define smokesolid_major 3
%define libsmokesolid %mklibname smokesolid %{smokesolid_major}

%package -n %{libsmokesolid}
Summary:	Solid bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokesolid}
Solid bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesolid}
%{_kde_libdir}/libsmokesolid.so.%{smokesolid_major}*

#-----------------------------------------------------------------------------

%define smokeokular_major 3
%define libsmokeokular %mklibname smokeokular %{smokeokular_major}

%package -n %{libsmokeokular}
Summary:	Okular bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeokular}
Okular bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeokular}
%{_kde_libdir}/libsmokeokular.so.%{smokeokular_major}*

#------------------------------------------------------------

%define libsmokesoprano_major 3
%define libsmokesoprano %mklibname smokesoprano %{libsmokesoprano_major}

%package -n %{libsmokesoprano}
Summary:	Soprano bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokesoprano}
Soprano bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesoprano}
%{_kde_libdir}/libsmokesoprano.so.%{libsmokesoprano_major}*

#------------------------------------------------------------

%define libsmokeplasma_major 3
%define libsmokeplasma %mklibname smokeplasma %{libsmokeplasma_major}

%package -n %{libsmokeplasma}
Summary:	Plasma bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeplasma}
Plasma bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeplasma}
%{_kde_libdir}/libsmokeplasma.so.%{libsmokeplasma_major}*

#------------------------------------------------------------

%define libsmokenepomuk_major 3
%define libsmokenepomuk %mklibname smokenepomuk %{libsmokenepomuk_major}

%package -n %{libsmokenepomuk}
Summary:	Nepomuk bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokenepomuk}
Nepomuk bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokenepomuk}
%{_kde_libdir}/libsmokenepomuk.so.%{libsmokenepomuk_major}*

#------------------------------------------------------------
%if %{with_kdepimlibs}
%define libsmokeakonadi_major 3
%define libsmokeakonadi %mklibname smokeakonadi %{libsmokeakonadi_major}

%package -n %{libsmokeakonadi}
Summary:	Akondi bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeakonadi}
Akondi bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeakonadi}
%{_kde_libdir}/libsmokeakonadi.so.%{libsmokeakonadi_major}*
%endif

#------------------------------------------------------------

%define libsmokeattica_major 3
%define libsmokeattica %mklibname smokeattica %{libsmokeattica_major}

%package -n %{libsmokeattica}
Summary:	Attica bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokeattica}
Attica bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeattica}
%{_kde_libdir}/libsmokeattica.so.%{libsmokeattica_major}*

#------------------------------------------------------------

%define libsmokenepomukquery_major 3
%define libsmokenepomukquery %mklibname smokenepomukquery %{libsmokenepomukquery_major}

%package -n %{libsmokenepomukquery}
Summary:	Nepomuk bindings for SMOKE
Group:		Development/KDE and Qt

%description -n %{libsmokenepomukquery}
Nepomuk bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokenepomukquery}
%{_kde_libdir}/libsmokenepomukquery.so.%{libsmokenepomukquery_major}*

#------------------------------------------------------------

%package devel
Summary:	Header files for %{name}
Group:		Development/KDE and Qt
Requires:	smokeqt-devel >= 1:%{version}
Requires:	okular-devel >= 2:%{version}
Requires:	kate-devel >= 1:%{version}
%if %{with_kdepimlibs}
Requires:	%{libsmokeakonadi} = %{EVRD}
Requires:	kdepimlibs4-devel >= 2:%{version}
%endif
Requires:	%{libsmokeattica} = %{EVRD}
Requires:	%{libsmokekate} = %{EVRD}
Requires:	%{libsmokekdecore} = %{EVRD}
Requires:	%{libsmokekdeui} = %{EVRD}
Requires:	%{libsmokekfile} = %{EVRD}
Requires:	%{libsmokekhtml} = %{EVRD}
Requires:	%{libsmokekio} = %{EVRD}
Requires:	%{libsmokeknewstuff2} = %{EVRD}
Requires:	%{libsmokeknewstuff3} = %{EVRD}
Requires:	%{libsmokekparts} = %{EVRD}
Requires:	%{libsmokektexteditor} = %{EVRD}
Requires:	%{libsmokekutils} = %{EVRD}
Requires:	%{libsmokenepomuk} = %{EVRD}
Requires:	%{libsmokenepomukquery} = %{EVRD}
Requires:	%{libsmokeokular} = %{EVRD}
Requires:	%{libsmokeplasma} = %{EVRD}
Requires:	%{libsmokesolid} = %{EVRD}
Requires:	%{libsmokesoprano} = %{EVRD}
Requires:	%{libsmokesopranoclient} = %{EVRD}
Requires:	%{libsmokesopranoserver} = %{EVRD}
Conflicts:	smoke4-devel < 1:4.6.90

%description devel
Devel files for %{name}

%files devel
%{_includedir}/smoke/attica_smoke.h
%{_includedir}/smoke/kdecore_smoke.h
%{_includedir}/smoke/kdeui_smoke.h
%{_includedir}/smoke/kfile_smoke.h
%{_includedir}/smoke/khtml_smoke.h
%{_includedir}/smoke/kio_smoke.h
%{_includedir}/smoke/knewstuff2_smoke.h
%{_includedir}/smoke/knewstuff3_smoke.h
%{_includedir}/smoke/kparts_smoke.h
%{_includedir}/smoke/ktexteditor_smoke.h
%{_includedir}/smoke/kutils_smoke.h
%{_includedir}/smoke/nepomuk_smoke.h
%{_includedir}/smoke/nepomukquery_smoke.h
%{_includedir}/smoke/okular_smoke.h
%{_includedir}/smoke/plasma_smoke.h
%{_includedir}/smoke/solid_smoke.h
%{_includedir}/smoke/soprano_smoke.h
%{_includedir}/smoke/sopranoclient_smoke.h
%{_includedir}/smoke/sopranoserver_smoke.h
%{_includedir}/smoke/kate_smoke.h
%{_kde_libdir}/libsmokekate.so
%if %{with_kdepimlibs}
%{_includedir}/smoke/akonadi_smoke.h
%{_kde_libdir}/libsmokeakonadi.so
%endif
%{_kde_libdir}/libsmokeattica.so
%{_kde_libdir}/libsmokekdecore.so
%{_kde_libdir}/libsmokekdeui.so
%{_kde_libdir}/libsmokekfile.so
%{_kde_libdir}/libsmokekhtml.so
%{_kde_libdir}/libsmokekio.so
%{_kde_libdir}/libsmokeknewstuff2.so
%{_kde_libdir}/libsmokeknewstuff3.so
%{_kde_libdir}/libsmokekparts.so
%{_kde_libdir}/libsmokektexteditor.so
%{_kde_libdir}/libsmokekutils.so
%{_kde_libdir}/libsmokenepomuk.so
%{_kde_libdir}/libsmokenepomukquery.so
%{_kde_libdir}/libsmokeokular.so
%{_kde_libdir}/libsmokeplasma.so
%{_kde_libdir}/libsmokesolid.so
%{_kde_libdir}/libsmokesoprano.so
%{_kde_libdir}/libsmokesopranoclient.so
%{_kde_libdir}/libsmokesopranoserver.so
%{_kde_datadir}/smokegen/kde-config.xml

#------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0
- Add pkgconfig(shared-desktop-ontologies) to BuildRequires

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sun Jul 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.2mib2010.2
+ Revision: 770534
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Wed Feb 01 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:4.8.0-2
+ Revision: 770534
- build with kdepimlibs
- build against working kate..

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762506
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758091
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 744570
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-2
+ Revision: 744388
- Fix typo in requires

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739325
- New upstream tarball $NEW_VERSION
- New upstream tarball 4.7.80

* Mon Nov 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 730563
- Import smokekde

