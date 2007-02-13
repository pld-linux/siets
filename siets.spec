%define		_snap	20060810
%define		_rel	0.4
Summary:	siets - search engines platform
Summary(pl.UTF-8):	siets - platforma dla wyszukiwarek
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

# XXX: FHS - is it possible to fix?
%define		_prefix		/usr/local/siets
%define		_bindir		%{_prefix}/bin
%define		_sbindir	%{_prefix}/crawler/bin
%define		_cgidir		/home/services/apache/cgi-bin/siets
%define		_htmldir	/home/services/apache/html/siets
%define		_sysconfdir	/etc/siets

%description
Siets is an innovative software platform for development and operation
of high performance search engines.

Benefit from its simplicity to use, quality of functions, XML-based
platform independence, use of industry's best-practice standards,
scalability through Linux clustering and low-cost.

%description -l pl.UTF-8
siets to innowacyjna platforma programowa do tworzenia i działania
wysoko wydajnych wyszukiwarek.

Zalety tej platformy to prostota użycia, jakość funkcji, niezależność
od platformy opartej na XML, użycie najlepiej sprawdzonych standardów
przemysłowych, skalowalność poprzez klastry Linuksowe oraz niska cena.

%prep
%setup -q -c -T
sh %{SOURCE0} --tar xf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_cgidir},%{_htmldir}}

# siets
install server/bin/siets-alertd $RPM_BUILD_ROOT%{_bindir}
install server/bin/siets-ctrld $RPM_BUILD_ROOT%{_bindir}
install server/bin/siets-dicd $RPM_BUILD_ROOT%{_bindir}
install server/bin/siets-dispd $RPM_BUILD_ROOT%{_bindir}
install server/bin/siets-docd $RPM_BUILD_ROOT%{_bindir}
install server/bin/siets-load $RPM_BUILD_ROOT%{_bindir}
install server/bin/siets-masterd $RPM_BUILD_ROOT%{_bindir}
install server/bin/siets-mtxd $RPM_BUILD_ROOT%{_bindir}
install server/bin/sietsco $RPM_BUILD_ROOT%{_bindir}
install server/bin/managed-xml $RPM_BUILD_ROOT%{_bindir}
install server/spec/suse/managedctl $RPM_BUILD_ROOT%{_bindir}
install server/bin/archive-handler $RPM_BUILD_ROOT%{_bindir}

# crawler
install server/spec/suse/crawldctl $RPM_BUILD_ROOT%{_sbindir}
install server/bin/crawld $RPM_BUILD_ROOT%{_sbindir}
install server/bin/cpy $RPM_BUILD_ROOT%{_sbindir}
install server/bin/downloader $RPM_BUILD_ROOT%{_sbindir}
install server/bin/down_manager $RPM_BUILD_ROOT%{_sbindir}
install server/bin/dom_manager $RPM_BUILD_ROOT%{_sbindir}
install server/bin/run_crawler $RPM_BUILD_ROOT%{_sbindir}

install sem/cgi-bin/api.cgi $RPM_BUILD_ROOT%{_cgidir}
install sem/cgi-bin/geteml.cgi $RPM_BUILD_ROOT%{_cgidir}
install sem/cgi-bin/api-ws.cgi $RPM_BUILD_ROOT%{_cgidir}
install sem/cgi-bin/api-ws.disco $RPM_BUILD_ROOT%{_cgidir}
#install %{_cgidir}/api.html
#install %{_cgidir}/api.wsdl

cp -a server/api/search.html $RPM_BUILD_ROOT%{_htmldir}
cp -a server/api/mail_form.html $RPM_BUILD_ROOT%{_htmldir}
cp -a server/api/parop.js $RPM_BUILD_ROOT%{_htmldir}

install -d $RPM_BUILD_ROOT%{_prefix}/crawler/conf/char_stats
cp -a server/conf/char_stats/*.stat $RPM_BUILD_ROOT%{_prefix}/crawler/conf/char_stats

install -d $RPM_BUILD_ROOT%{_prefix}/conf/templates
cp -a server/conf/templates/*.xml $RPM_BUILD_ROOT%{_prefix}/conf/templates
install -D server/conf/content.type $RPM_BUILD_ROOT%{_prefix}/crawler/conf/content.type

install -D server/extensions/antiword/bin/antiword $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/antiword/bin/antiword
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/antiword/data
cp -a server/extensions/antiword/data/* $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/antiword/data
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/antiword/lic
cp -a server/extensions/antiword/lic/* $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/antiword/lic

install -D server/extensions/pdftotext/bin/pdftotext $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/pdftotext/bin/pdftotext
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/pdftotext/lic
cp -a server/extensions/pdftotext/lic/* $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/pdftotext/lic

install -D server/extensions/ps2ascii/bin/ps2ascii $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/ps2ascii/bin/ps2ascii
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/ps2ascii/lic
cp -a ./server/extensions/ps2ascii/lic/* $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/ps2ascii/lic

install -D server/extensions/rtf2html/bin/rtf2html $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/rtf2html/bin/rtf2html
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/rtf2html/lic
cp -a server/extensions/rtf2html/lic/* $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/rtf2html/lic

install -d $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/xlspptToHtml/bin
install server/extensions/xlspptToHtml/bin/ppthtml $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/xlspptToHtml/bin
install server/extensions/xlspptToHtml/bin/xlhtml $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/xlspptToHtml/bin
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/xlspptToHtml/lic
cp -a server/extensions/xlspptToHtml/lic/* $RPM_BUILD_ROOT%{_prefix}/crawler/extensions/xlspptToHtml/lic

install server/bin/archive-handler $RPM_BUILD_ROOT%{_bindir}/archive-handler
install -d $RPM_BUILD_ROOT%{_prefix}/log
install -d $RPM_BUILD_ROOT%{_prefix}/data
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/crawl_tasks
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/log

install -d $RPM_BUILD_ROOT%{_prefix}/conf
cp -a server/conf/access.xml $RPM_BUILD_ROOT%{_prefix}/conf/access.xml
cp -a server/conf/managed_inst_cfg.xml $RPM_BUILD_ROOT%{_prefix}/conf/managed_inst_cfg.xml
install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -a server/conf/siets_cfg.xml $RPM_BUILD_ROOT%{_sysconfdir}/siets_cfg.xml
install -d $RPM_BUILD_ROOT%{_prefix}/crawler/conf
cp -a server/conf/crawld_cfg.xml $RPM_BUILD_ROOT%{_prefix}/crawler/conf/crawld_cfg.xml
install -d $RPM_BUILD_ROOT%{_cgidir}
cp -a sem/cgi-bin/config.txt $RPM_BUILD_ROOT%{_cgidir}/config.txt
cp -a sem/cgi-bin/config.xml $RPM_BUILD_ROOT%{_cgidir}/config.xml

install -d $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/0 $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/10 $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/20 $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/30 $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/40 $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/common $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/images $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/js $RPM_BUILD_ROOT%{_htmldir}/templates
cp -a sem/templates/style $RPM_BUILD_ROOT%{_htmldir}/templates

#TYPE=BIN APP=SEM %{_htmldir}/index.html
cp -a sem/startpage/index.html $RPM_BUILD_ROOT%{_htmldir}

install sem/cgi-bin/sem.cgi $RPM_BUILD_ROOT%{_cgidir}/sem.cgi
install -d $RPM_BUILD_ROOT%{_htmldir}/log
install -d $RPM_BUILD_ROOT%{_htmldir}/tmp
install -d $RPM_BUILD_ROOT/tmp/siets
install -d $RPM_BUILD_ROOT/tmp/siets/sessions

#TYPE=PAR APP=SEM vercode=1.1.0
install -d $RPM_BUILD_ROOT%{_htmldir}/conf
cp -a sem/conf/manager_cfg.xml $RPM_BUILD_ROOT%{_htmldir}/conf
#TYPE=LIC APP=GEN %{_prefix}/licence.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%config %{_sysconfdir}/siets_cfg.xml
%attr(755,root,root) %{_cgidir}/api-ws.cgi
%attr(755,root,root) %{_cgidir}/api-ws.disco
%attr(755,root,root) %{_cgidir}/api.cgi
%attr(755,root,root) %{_cgidir}/config.txt
%attr(755,root,root) %{_cgidir}/config.xml
%attr(755,root,root) %{_cgidir}/geteml.cgi
%attr(755,root,root) %{_cgidir}/sem.cgi
%dir %{_htmldir}/conf
%{_htmldir}/conf/manager_cfg.xml
%{_htmldir}/index.html
%{_htmldir}/mail_form.html
%{_htmldir}/parop.js
%{_htmldir}/search.html
%dir %{_htmldir}/templates
%{_htmldir}/templates/*
%attr(755,root,root) %{_bindir}/archive-handler
%attr(755,root,root) %{_bindir}/managed-xml
%attr(755,root,root) %{_bindir}/managedctl
%attr(755,root,root) %{_bindir}/siets-alertd
%attr(755,root,root) %{_bindir}/siets-ctrld
%attr(755,root,root) %{_bindir}/siets-dicd
%attr(755,root,root) %{_bindir}/siets-dispd
%attr(755,root,root) %{_bindir}/siets-docd
%attr(755,root,root) %{_bindir}/siets-load
%attr(755,root,root) %{_bindir}/siets-masterd
%attr(755,root,root) %{_bindir}/siets-mtxd
%attr(755,root,root) %{_bindir}/sietsco
%dir %{_prefix}/conf
%{_prefix}/conf/access.xml
%{_prefix}/conf/managed_inst_cfg.xml
%dir %{_prefix}/conf/templates
%{_prefix}/conf/templates/config_template.xml
%{_prefix}/conf/templates/default_desc.xml
%{_prefix}/conf/templates/mail_config.xml
%{_prefix}/conf/templates/mail_desc.xml
%{_prefix}/conf/templates/mail_policy.xml
%{_prefix}/conf/templates/policy_template.xml
%attr(755,root,root) %{_sbindir}/cpy
%attr(755,root,root) %{_sbindir}/crawld
%attr(755,root,root) %{_sbindir}/crawldctl
%attr(755,root,root) %{_sbindir}/dom_manager
%attr(755,root,root) %{_sbindir}/down_manager
%attr(755,root,root) %{_sbindir}/downloader
%attr(755,root,root) %{_sbindir}/run_crawler
%dir %{_prefix}/crawler
%dir %{_prefix}/crawler/conf
%{_prefix}/crawler/conf/content.type
%{_prefix}/crawler/conf/crawld_cfg.xml
%dir %{_prefix}/crawler/conf/char_stats
%{_prefix}/crawler/conf/char_stats/EN_CP1257.stat
%{_prefix}/crawler/conf/char_stats/LV_CP1257.stat
%{_prefix}/crawler/conf/char_stats/LV_ISO88594.stat
%{_prefix}/crawler/conf/char_stats/LV_UTF8.stat
%{_prefix}/crawler/conf/char_stats/RU_CP1251.stat
%{_prefix}/crawler/conf/char_stats/RU_KOI8R.stat
%{_prefix}/crawler/conf/char_stats/RU_UTF8.stat

%dir %{_prefix}/crawler/extensions
%dir %{_prefix}/crawler/extensions/antiword
%dir %{_prefix}/crawler/extensions/antiword/bin
%attr(755,root,root) %{_prefix}/crawler/extensions/antiword/bin/antiword
%{_prefix}/crawler/extensions/antiword/data
%{_prefix}/crawler/extensions/antiword/lic

%dir %{_prefix}/crawler/extensions/pdftotext
%dir %{_prefix}/crawler/extensions/pdftotext/bin
%attr(755,root,root) %{_prefix}/crawler/extensions/pdftotext/bin/pdftotext
%{_prefix}/crawler/extensions/pdftotext/lic

%dir %{_prefix}/crawler/extensions/ps2ascii
%dir %{_prefix}/crawler/extensions/ps2ascii/bin
%attr(755,root,root) %{_prefix}/crawler/extensions/ps2ascii/bin/ps2ascii
%{_prefix}/crawler/extensions/ps2ascii/lic

%dir %{_prefix}/crawler/extensions/rtf2html
%dir %{_prefix}/crawler/extensions/rtf2html/bin
%attr(755,root,root) %{_prefix}/crawler/extensions/rtf2html/bin/rtf2html
%{_prefix}/crawler/extensions/rtf2html/lic

%dir %{_prefix}/crawler/extensions/xlspptToHtml
%dir %{_prefix}/crawler/extensions/xlspptToHtml/bin
%attr(755,root,root) %{_prefix}/crawler/extensions/xlspptToHtml/bin/ppthtml
%attr(755,root,root) %{_prefix}/crawler/extensions/xlspptToHtml/bin/xlhtml
%{_prefix}/crawler/extensions/xlspptToHtml/lic
