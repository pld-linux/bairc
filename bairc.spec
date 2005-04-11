Summary:	IRC client written entirely in BASH
Summary(pl):	Klient IRC napisany wy³±cznie w BASH
Name:		bairc
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	https://www.darkwired.org/pub/code/miniprojects/bairc/%{name}-%{version}.tar.gz
# Source0-md5:	515e626ce3e4c12dd2eaff0f0d0e383f
URL:		https://www.darkwired.org/pub/code/miniprojects/bairc/
Requires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bourne Again IRC Client is a single-file client written entirely in
BASH. It supports basic commands and has a nice GUI.

%description -l pl
Bourne Again IRC Client jest sk³adaj±cym siê z tylko jednego pliku
klientem IRC napisanym w BASH. Wspiera podstawowe komendy oraz
posiada ³adne GUI.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}-%{version}.bash $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
