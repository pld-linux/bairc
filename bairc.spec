Summary:	IRC client written entirely in BASH
Summary(pl):	Klient IRC napisany wy³±cznie w BASH
Name:		bairc
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	https://www.darkwired.org/pub/code/miniprojects/bairc/%{name}-%{version}.tar.gz
# Source0-md5:	4bc884aa5db0bd12d5f94846c58f1d6e
URL:		https://www.darkwired.org/pub/code/miniprojects/bairc/
Requires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bourne Again IRC Client is a single-file client written entirely in
BASH. It supports basic commands and has a nice GUI.

%description -l pl
Bourne Again IRC Client jest sk³adaj±cym siê z tylko jednego pliku
klientem IRC napisanym w BASH. Wspierwa podstawowe komendy oraz
posiada ³adne GUI.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bairc-1.2.bash $RPM_BUILD_ROOT%{_bindir}/bairc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
