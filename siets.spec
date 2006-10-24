%define		_snap	20060810
%define		_rel	0.1
Summary:	siets
Name:		siets
Version:	3.4.3
Release:	0.%{_snap}.%{_rel}
License:	?
Group:		Applications
Source0:	http://www.siets.biz/server/download/files_out_there/SIETS-%{_snap}.setup
# NoSource0-md5:	f8b752004df7bb77c98aed5853390866
NoSource:	0
URL:		http://www.siets.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Siets is an innovative software platform for development and operation
of high performance search engines.

Benefit from its simplicity to use, quality of functions, XML-based
platform independence, use of industry's best-practice standards,
scalability throgh Linux clustering and low-cost.

%prep
%setup -q -c -T
sh %{SOURCE0} --tar xf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
