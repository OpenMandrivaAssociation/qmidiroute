%define name    qmidiroute
%define version 0.3.0
%define release %mkrel 1 

Name:           %{name} 
Summary:        MIDI router and filter utility
Version:        %{version} 
Release:        %{release}

Source:         http://dl.sf.net/alsamodular/%{name}-%{version}.tar.bz2
URL:            http://alsamodular.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
BuildRequires:  alsa-lib-devel qt4-devel

%description
MIDI router and filter utility for the ALSA sequencer.

%prep 
%setup -q  
%if %mdkversion >= 201000
iconv -f=latin1 -t=utf8 man/de/%{name}.1 -o man/de/%{name}.1
iconv -f=latin1 -t=utf8 man/fr/%{name}.1 -o man/fr/%{name}.1
%endif

%build 
%configure 
%make
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{__mkdir} -p %{buildroot}%{_datadir}/pixmaps
%{__install} -m 0644 src/pixmaps/qmidiroute_48.xpm %{buildroot}%{_datadir}/pixmaps

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QMidiRoute
Comment=MIDI Filter and Router
Exec=%{_bindir}/%{name}
Icon=qmidiroute_48
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
Encoding=UTF-8
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/qmidiroute_48.xpm
%docdir %{_mandir}/man1/*
%{_mandir}/man1/*
%{_mandir}/de/man1/*
%{_mandir}/fr/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop

