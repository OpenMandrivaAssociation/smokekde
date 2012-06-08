%define with_kdepimlibs 1
Name:smokekde
Summary: KDE4 bindings for SMOKE 
Version: 4.8.4
Release: 1
Epoch:   1
Group: Graphical desktop/KDE
License: GPLv2 LGPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz
BuildRequires: smokeqt-devel >= 1:%version
%if %with_kdepimlibs
BuildRequires: kdepimlibs4-devel >= 2:%version
%endif
BuildRequires: okular-devel >= 2:%version
BuildRequires: kate-devel >= 1:%version
BuildRequires: qscintilla-qt4-devel

%description
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

#-----------------------------------------------------------------------------

%define smokesopranoclient_major 3
%define libsmokesopranoclient %mklibname smokesopranoclient %{smokesopranoclient_major}

%package -n   %{libsmokesopranoclient}
Summary:      Soprano bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokesopranoclient}
Soprano bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesopranoclient}
%_kde_libdir/libsmokesopranoclient.so.%{smokesopranoclient_major}*

#-----------------------------------------------------------------------------

%define smokesopranoserver_major 3
%define libsmokesopranoserver %mklibname smokesopranoserver %{smokesopranoserver_major}

%package -n   %{libsmokesopranoserver}
Summary:      Soprano bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokesopranoserver}
Soprano bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesopranoserver}
%_kde_libdir/libsmokesopranoserver.so.%{smokesopranoserver_major}*

#------------------------------------------------------------

%define smokekate_major 3
%define libsmokekate %mklibname smokekate %{smokekate_major}

%package -n %{libsmokekate}
Summary: Kate bindings for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokekate}
Kate bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekate}
%_kde_libdir/libsmokekate.so.%{smokekate_major}*

#-----------------------------------------------------------------------------

%define smokekdecore_major 3
%define libsmokekdecore %mklibname smokekdecore %{smokekdecore_major}

%package -n   %{libsmokekdecore}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokekdecore}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekdecore}
%_kde_libdir/libsmokekdecore.so.%{smokekdecore_major}*

#-----------------------------------------------------------------------------

%define smokekdeui_major 3
%define libsmokekdeui %mklibname smokekdeui %{smokekdeui_major}

%package -n   %{libsmokekdeui}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokekdeui}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekdeui}
%_kde_libdir/libsmokekdeui.so.%{smokekdeui_major}*

#-----------------------------------------------------------------------------

%define smokekfile_major 3
%define libsmokekfile %mklibname smokekfile %{smokekfile_major}

%package -n   %{libsmokekfile}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokekfile}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekfile}
%_kde_libdir/libsmokekfile.so.%{smokekfile_major}*

#-----------------------------------------------------------------------------

%define smokekio_major 3
%define libsmokekio %mklibname smokekio %{smokekio_major}

%package -n   %{libsmokekio}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokekio}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekio}
%_kde_libdir/libsmokekio.so.%{smokekio_major}*

#-----------------------------------------------------------------------------

%define smokeknewstuff2_major 3
%define libsmokeknewstuff2 %mklibname smokeknewstuff2_ %{smokeknewstuff2_major}

%package -n   %{libsmokeknewstuff2}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeknewstuff2}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeknewstuff2}
%_kde_libdir/libsmokeknewstuff2.so.%{smokeknewstuff2_major}*

#-----------------------------------------------------------------------------

%define smokeknewstuff3_major 3
%define libsmokeknewstuff3 %mklibname smokeknewstuff3_ %{smokeknewstuff3_major}

%package -n   %{libsmokeknewstuff3}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeknewstuff3}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeknewstuff3}
%_kde_libdir/libsmokeknewstuff3.so.%{smokeknewstuff3_major}*

#-----------------------------------------------------------------------------

%define smokekhtml_major 3
%define libsmokekhtml %mklibname smokekhtml %{smokekhtml_major}

%package -n   %{libsmokekhtml}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokekhtml}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekhtml}
%_kde_libdir/libsmokekhtml.so.%{smokekhtml_major}*

#-----------------------------------------------------------------------------

%define smokektexteditor_major 3
%define libsmokektexteditor %mklibname smoketexteditor %{smokektexteditor_major}

%package -n   %{libsmokektexteditor}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokektexteditor}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokektexteditor}
%_kde_libdir/libsmokektexteditor.so.%{smokektexteditor_major}*

#-----------------------------------------------------------------------------

%define smokekparts_major 3
%define libsmokekparts %mklibname smokekparts %{smokekparts_major}

%package -n   %{libsmokekparts}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokekparts}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekparts}
%_kde_libdir/libsmokekparts.so.%{smokekparts_major}*

#-----------------------------------------------------------------------------

%define smokekutils_major 3
%define libsmokekutils %mklibname smokekutils %{smokekutils_major}

%package -n   %{libsmokekutils}
Summary:      KDE4 bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokekutils}
KDE4 bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokekutils}
%_kde_libdir/libsmokekutils.so.%{smokekutils_major}*

#-----------------------------------------------------------------------------

%define smokesolid_major 3
%define libsmokesolid %mklibname smokesolid %{smokesolid_major}

%package -n   %{libsmokesolid}
Summary:      Solid bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokesolid}
Solid bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesolid}
%_kde_libdir/libsmokesolid.so.%{smokesolid_major}*

#-----------------------------------------------------------------------------

%define smokeokular_major 3
%define libsmokeokular %mklibname smokeokular %{smokeokular_major}

%package -n   %{libsmokeokular}
Summary:      Okular bindings for SMOKE
Group:        Development/KDE and Qt

%description -n %{libsmokeokular}
Okular bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeokular}
%_kde_libdir/libsmokeokular.so.%{smokeokular_major}*

#------------------------------------------------------------

%define libsmokesoprano_major 3
%define libsmokesoprano %mklibname smokesoprano %{libsmokesoprano_major}

%package -n %{libsmokesoprano}
Summary: Soprano bindings for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokesoprano}
Soprano bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokesoprano}
%_kde_libdir/libsmokesoprano.so.%{libsmokesoprano_major}*

#------------------------------------------------------------

%define libsmokeplasma_major 3
%define libsmokeplasma %mklibname smokeplasma %{libsmokeplasma_major}

%package -n %{libsmokeplasma}
Summary: Plasma bindings for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokeplasma}
Plasma bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeplasma}
%_kde_libdir/libsmokeplasma.so.%{libsmokeplasma_major}*

#------------------------------------------------------------

%define libsmokenepomuk_major 3
%define libsmokenepomuk %mklibname smokenepomuk %{libsmokenepomuk_major}

%package -n %{libsmokenepomuk}
Summary: Nepomuk bindings for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokenepomuk}
Nepomuk bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokenepomuk}
%_kde_libdir/libsmokenepomuk.so.%{libsmokenepomuk_major}*

#------------------------------------------------------------
%if %with_kdepimlibs
%define libsmokeakonadi_major 3
%define libsmokeakonadi %mklibname smokeakonadi %{libsmokeakonadi_major}

%package -n %{libsmokeakonadi}
Summary: Akondi bindings for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokeakonadi}
Akondi bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeakonadi}
%_kde_libdir/libsmokeakonadi.so.%{libsmokeakonadi_major}*
%endif

#------------------------------------------------------------

%define libsmokeattica_major 3
%define libsmokeattica %mklibname smokeattica %{libsmokeattica_major}

%package -n %{libsmokeattica}
Summary: Attica bindings for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokeattica}
Attica bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokeattica}
%_kde_libdir/libsmokeattica.so.%{libsmokeattica_major}*

#------------------------------------------------------------

%define libsmokenepomukquery_major 3
%define libsmokenepomukquery %mklibname smokenepomukquery %{libsmokenepomukquery_major}

%package -n %{libsmokenepomukquery}
Summary: Nepomuk bindings for SMOKE
Group: Development/KDE and Qt

%description -n %{libsmokenepomukquery}
Nepomuk bindings for SMOKE (Scripting Meta Object Kompiler Engine)

%files -n %{libsmokenepomukquery}
%_kde_libdir/libsmokenepomukquery.so.%{libsmokenepomukquery_major}*

#------------------------------------------------------------

%package devel
Summary: Header files for %{name}
Group: Development/KDE and Qt
Requires: smokeqt-devel >= 1:%version
Requires: okular-devel >= 2:%version
Requires: kate-devel >= 1:%version
%if %with_kdepimlibs
Requires: %{libsmokeakonadi} = %epoch:%version-%release
Requires: kdepimlibs4-devel >= 2:%version
%endif
Requires: %{libsmokeattica} = %epoch:%version-%release
Requires: %{libsmokekate} = %epoch:%version-%release
Requires: %{libsmokekdecore} = %epoch:%version-%release
Requires: %{libsmokekdeui} = %epoch:%version-%release
Requires: %{libsmokekfile} = %epoch:%version-%release
Requires: %{libsmokekhtml} = %epoch:%version-%release
Requires: %{libsmokekio} = %epoch:%version-%release
Requires: %{libsmokeknewstuff2} = %epoch:%version-%release
Requires: %{libsmokeknewstuff3} = %epoch:%version-%release
Requires: %{libsmokekparts} = %epoch:%version-%release
Requires: %{libsmokektexteditor} = %epoch:%version-%release
Requires: %{libsmokekutils} = %epoch:%version-%release
Requires: %{libsmokenepomuk} = %epoch:%version-%release
Requires: %{libsmokenepomukquery} = %epoch:%version-%release
Requires: %{libsmokeokular} = %epoch:%version-%release
Requires: %{libsmokeplasma} = %epoch:%version-%release
Requires: %{libsmokesolid} = %epoch:%version-%release
Requires: %{libsmokesoprano} = %epoch:%version-%release
Requires: %{libsmokesopranoclient} = %epoch:%version-%release
Requires: %{libsmokesopranoserver} = %epoch:%version-%release
Conflicts: smoke4-devel < 1:4.6.90

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
%_kde_libdir/libsmokekate.so
%if %with_kdepimlibs
%{_includedir}/smoke/akonadi_smoke.h
%_kde_libdir/libsmokeakonadi.so
%endif
%_kde_libdir/libsmokeattica.so
%_kde_libdir/libsmokekdecore.so
%_kde_libdir/libsmokekdeui.so
%_kde_libdir/libsmokekfile.so
%_kde_libdir/libsmokekhtml.so
%_kde_libdir/libsmokekio.so
%_kde_libdir/libsmokeknewstuff2.so
%_kde_libdir/libsmokeknewstuff3.so
%_kde_libdir/libsmokekparts.so
%_kde_libdir/libsmokektexteditor.so
%_kde_libdir/libsmokekutils.so
%_kde_libdir/libsmokenepomuk.so
%_kde_libdir/libsmokenepomukquery.so
%_kde_libdir/libsmokeokular.so
%_kde_libdir/libsmokeplasma.so
%_kde_libdir/libsmokesolid.so
%_kde_libdir/libsmokesoprano.so
%_kde_libdir/libsmokesopranoclient.so
%_kde_libdir/libsmokesopranoserver.so
%_kde_datadir/smokegen/kde-config.xml

#------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

