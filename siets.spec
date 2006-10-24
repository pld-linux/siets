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

%define		_prefix		/usr/local/siets
%define		_bindir		%{_prefix}/bin
%define		_sbindir	%{_prefix}/crawler/bin
%define		_cgidir		/home/services/apache/cgi-bin/siets
%define		_htmldir	/home/services/apache/html/siets

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
#install /home/services/apache/cgi-bin/siets/api.html
#install /home/services/apache/cgi-bin/siets/api.wsdl

cp -a server/api/search.html $RPM_BUILD_ROOT%{_htmldir}
cp -a server/api/mail_form.html $RPM_BUILD_ROOT%{_htmldir}
cp -a server/api/parop.js $RPM_BUILD_ROOT%{_htmldir}

cp -a server/conf/char_stats/*.stat $RPM_BUILD_ROOT/usr/local/siets/crawler/conf/char_stats

install -d $RPM_BUILD_ROOT/usr/local/siets/conf/templates
cp -a server/conf/templates/*.xml $RPM_BUILD_ROOT/usr/local/siets/conf/templates
install -D server/conf/content.type $RPM_BUILD_ROOT/usr/local/siets/crawler/conf/content.type

install -D server/extensions/antiword/bin/antiword $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/antiword/bin/antiword
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/antiword/data
cp -a server/extensions/antiword/data/* $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/antiword/data
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/antiword/lic
cp -a server/extensions/antiword/lic/* $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/antiword/lic

install -D server/extensions/pdftotext/bin/pdftotext $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/pdftotext/bin/pdftotext
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/pdftotext/lic
cp -a server/extensions/pdftotext/lic/* $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/pdftotext/lic

install -D server/extensions/ps2ascii/bin/ps2ascii $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/ps2ascii/bin/ps2ascii
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/ps2ascii/lic
cp -a ./server/extensions/ps2ascii/lic/* $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/ps2ascii/lic

install -D server/extensions/rtf2html/bin/rtf2html $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/rtf2html/bin/rtf2html
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/rtf2html/lic
cp -a server/extensions/rtf2html/lic/* $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/rtf2html/lic

install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/xlspptToHtml/bin
install server/extensions/xlspptToHtml/bin/ppthtml $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/xlspptToHtml/bin
install server/extensions/xlspptToHtml/bin/xlhtml $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/xlspptToHtml/bin
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/xlspptToHtml/lic
cp -a server/extensions/xlspptToHtml/lic/* $RPM_BUILD_ROOT/usr/local/siets/crawler/extensions/xlspptToHtml/lic

install server/bin/archive-handler $RPM_BUILD_ROOT/usr/local/siets/bin/archive-handler
install -d $RPM_BUILD_ROOT/usr/local/siets/log
install -d $RPM_BUILD_ROOT/usr/local/siets/data
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/crawl_tasks
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/log


install -d $RPM_BUILD_ROOT/usr/local/siets/conf
cp -a server/conf/access.xml $RPM_BUILD_ROOT/usr/local/siets/conf/access.xml
cp -a server/conf/managed_inst_cfg.xml $RPM_BUILD_ROOT/usr/local/siets/conf/managed_inst_cfg.xml
install -d $RPM_BUILD_ROOT/etc/siets
cp -a server/conf/siets_cfg.xml $RPM_BUILD_ROOT/etc/siets/siets_cfg.xml
install -d $RPM_BUILD_ROOT/usr/local/siets/crawler/conf
cp -a server/conf/crawld_cfg.xml $RPM_BUILD_ROOT/usr/local/siets/crawler/conf/crawld_cfg.xml
install -d $RPM_BUILD_ROOT/home/services/apache/cgi-bin/siets
cp -a sem/cgi-bin/config.txt $RPM_BUILD_ROOT/home/services/apache/cgi-bin/siets/config.txt
cp -a sem/cgi-bin/config.xml $RPM_BUILD_ROOT/home/services/apache/cgi-bin/siets/config.xml

install -d $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/0 $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/10 $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/20 $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/30 $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/40 $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/common $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/images $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/js $RPM_BUILD_ROOT/home/services/apache/html/siets/templates
cp -a sem/templates/style $RPM_BUILD_ROOT/home/services/apache/html/siets/templates

#TYPE=BIN APP=SEM /home/services/apache/html/siets/index.html
cp -a sem/startpage/index.html $RPM_BUILD_ROOT/home/services/apache/html/siets

install sem/cgi-bin/sem.cgi $RPM_BUILD_ROOT/home/services/apache/cgi-bin/siets/sem.cgi
install -d $RPM_BUILD_ROOT/home/services/apache/html/siets/log
install -d $RPM_BUILD_ROOT/home/services/apache/html/siets/tmp
install -d $RPM_BUILD_ROOT/tmp/siets
install -d $RPM_BUILD_ROOT/tmp/siets/sessions

#TYPE=PAR APP=SEM vercode=1.1.0
install -d $RPM_BUILD_ROOT/home/services/apache/html/siets/conf
cp -a sem/conf/manager_cfg.xml $RPM_BUILD_ROOT/home/services/apache/html/siets/conf
#TYPE=LIC APP=GEN /usr/local/siets/licence.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config /etc/siets/siets_cfg.xml
/home/services/apache/cgi-bin/siets/api-ws.cgi
/home/services/apache/cgi-bin/siets/api-ws.disco
/home/services/apache/cgi-bin/siets/api.cgi
/home/services/apache/cgi-bin/siets/config.txt
/home/services/apache/cgi-bin/siets/config.xml
/home/services/apache/cgi-bin/siets/geteml.cgi
/home/services/apache/cgi-bin/siets/sem.cgi
/home/services/apache/html/siets/conf/manager_cfg.xml
/home/services/apache/html/siets/index.html
/home/services/apache/html/siets/mail_form.html
/home/services/apache/html/siets/parop.js
/home/services/apache/html/siets/search.html
/home/services/apache/html/siets/templates/0
/home/services/apache/html/siets/templates/10/10000000
/home/services/apache/html/siets/templates/10/10000000.xsl
/home/services/apache/html/siets/templates/10/10010000
/home/services/apache/html/siets/templates/10/10010000.xsl
/home/services/apache/html/siets/templates/10/10010100
/home/services/apache/html/siets/templates/10/10010110
/home/services/apache/html/siets/templates/10/10010110.xsl
/home/services/apache/html/siets/templates/10/10010111.xsl
/home/services/apache/html/siets/templates/10/10010112
/home/services/apache/html/siets/templates/10/10010112.xsl
/home/services/apache/html/siets/templates/10/10010120
/home/services/apache/html/siets/templates/10/10010120.xsl
/home/services/apache/html/siets/templates/10/10010122.xsl
/home/services/apache/html/siets/templates/10/10010130
/home/services/apache/html/siets/templates/10/10010130.xsl
/home/services/apache/html/siets/templates/10/10010131
/home/services/apache/html/siets/templates/10/10010200
/home/services/apache/html/siets/templates/10/10010200.xsl
/home/services/apache/html/siets/templates/10/10010300
/home/services/apache/html/siets/templates/10/10010300.xsl
/home/services/apache/html/siets/templates/10/10010400
/home/services/apache/html/siets/templates/10/10010500
/home/services/apache/html/siets/templates/10/10010500.xsl
/home/services/apache/html/siets/templates/10/10010600
/home/services/apache/html/siets/templates/10/10010600.xsl
/home/services/apache/html/siets/templates/10/10020000
/home/services/apache/html/siets/templates/10/10020000.xsl
/home/services/apache/html/siets/templates/10/10040000
/home/services/apache/html/siets/templates/10/10040000.xsl
/home/services/apache/html/siets/templates/10/srcLinks.last
/home/services/apache/html/siets/templates/20/20000000
/home/services/apache/html/siets/templates/20/20000000.xsl
/home/services/apache/html/siets/templates/20/20010000
/home/services/apache/html/siets/templates/20/20010000.xsl
/home/services/apache/html/siets/templates/30/30010000
/home/services/apache/html/siets/templates/30/30010000.xsl
/home/services/apache/html/siets/templates/30/30010002
/home/services/apache/html/siets/templates/30/30010002.xsl
/home/services/apache/html/siets/templates/30/30020000
/home/services/apache/html/siets/templates/30/30020000.xsl
/home/services/apache/html/siets/templates/40/40000000
/home/services/apache/html/siets/templates/40/40000000.xsl
/home/services/apache/html/siets/templates/40/40010000
/home/services/apache/html/siets/templates/40/40010000.xsl
/home/services/apache/html/siets/templates/40/40020100
/home/services/apache/html/siets/templates/40/40020100.xsl
/home/services/apache/html/siets/templates/40/40020110
/home/services/apache/html/siets/templates/40/40020110.xsl
/home/services/apache/html/siets/templates/40/40020111
/home/services/apache/html/siets/templates/40/40020111.xsl
/home/services/apache/html/siets/templates/40/40020112
/home/services/apache/html/siets/templates/40/40020112.xsl
/home/services/apache/html/siets/templates/40/40020113
/home/services/apache/html/siets/templates/40/40020113.xsl
/home/services/apache/html/siets/templates/40/40020114
/home/services/apache/html/siets/templates/40/40020115
/home/services/apache/html/siets/templates/40/40020115.xsl
/home/services/apache/html/siets/templates/40/40020116
/home/services/apache/html/siets/templates/40/40020116.xsl
/home/services/apache/html/siets/templates/40/40020117
/home/services/apache/html/siets/templates/40/40020117.xsl
/home/services/apache/html/siets/templates/40/40020118
/home/services/apache/html/siets/templates/40/40020118.xsl
/home/services/apache/html/siets/templates/40/40020119
/home/services/apache/html/siets/templates/40/40020119.xsl
/home/services/apache/html/siets/templates/40/40030000
/home/services/apache/html/siets/templates/40/40030000.xsl
/home/services/apache/html/siets/templates/40/40030100
/home/services/apache/html/siets/templates/40/40030100.xsl
/home/services/apache/html/siets/templates/40/40030200
/home/services/apache/html/siets/templates/40/40030200.xsl
/home/services/apache/html/siets/templates/common/authorization.inc
/home/services/apache/html/siets/templates/common/errors.xml
/home/services/apache/html/siets/templates/common/footer.inc
/home/services/apache/html/siets/templates/common/header.inc
/home/services/apache/html/siets/templates/common/warnings.xml
/home/services/apache/html/siets/templates/images/lo1.gif
/home/services/apache/html/siets/templates/images/uzaugshu.gif
/home/services/apache/html/siets/templates/images/uzleju.gif
/home/services/apache/html/siets/templates/images/x.gif
/home/services/apache/html/siets/templates/js/class/Applet1$Mouse.class
/home/services/apache/html/siets/templates/js/class/Applet1.class
/home/services/apache/html/siets/templates/js/class/DiagonalLayout.class
/home/services/apache/html/siets/templates/js/class/DocHandler.class
/home/services/apache/html/siets/templates/js/class/Grids.class
/home/services/apache/html/siets/templates/js/class/QDParser.class
/home/services/apache/html/siets/templates/js/class/Reporter.class
/home/services/apache/html/siets/templates/js/def.js
/home/services/apache/html/siets/templates/js/dom.js
/home/services/apache/html/siets/templates/js/jsDebugger/gpl.txt
/home/services/apache/html/siets/templates/js/jsDebugger/img/close.jpg
/home/services/apache/html/siets/templates/js/jsDebugger/img/max.jpg
/home/services/apache/html/siets/templates/js/jsDebugger/img/min.jpg
/home/services/apache/html/siets/templates/js/jsDebugger/img/resize.jpg
/home/services/apache/html/siets/templates/js/jsDebugger/img/start.jpg
/home/services/apache/html/siets/templates/js/jsDebugger/img/titlebar.jpg
/home/services/apache/html/siets/templates/js/jsDebugger/img/titlebar_active.jpg
/home/services/apache/html/siets/templates/js/jsDebugger/img/treebar.gif
/home/services/apache/html/siets/templates/js/jsDebugger/img/treebarbottom.gif
/home/services/apache/html/siets/templates/js/jsDebugger/img/treeline.gif
/home/services/apache/html/siets/templates/js/jsDebugger/img/treeminus.gif
/home/services/apache/html/siets/templates/js/jsDebugger/img/treeplus.gif
/home/services/apache/html/siets/templates/js/jsDebugger/index.html
/home/services/apache/html/siets/templates/js/jsDebugger/jsDebugger.js
/home/services/apache/html/siets/templates/js/validator.js
/home/services/apache/html/siets/templates/js/xmlsax.js
/home/services/apache/html/siets/templates/js/xmlw3cdom.js
/home/services/apache/html/siets/templates/style/def.css
/home/services/apache/html/siets/templates/style/default_web_results.xsl
/home/services/apache/html/siets/templates/style/mail_list.xsl
/home/services/apache/html/siets/templates/style/mail_view.xsl
/home/services/apache/html/siets/templates/style/str.replace.template.xsl
/home/services/apache/html/siets/templates/style/url_encode.xsl
/usr/local/siets/bin/archive-handler
/usr/local/siets/bin/managed-xml
/usr/local/siets/bin/managedctl
/usr/local/siets/bin/siets-alertd
/usr/local/siets/bin/siets-ctrld
/usr/local/siets/bin/siets-dicd
/usr/local/siets/bin/siets-dispd
/usr/local/siets/bin/siets-docd
/usr/local/siets/bin/siets-load
/usr/local/siets/bin/siets-masterd
/usr/local/siets/bin/siets-mtxd
/usr/local/siets/bin/sietsco
/usr/local/siets/conf/access.xml
/usr/local/siets/conf/managed_inst_cfg.xml
/usr/local/siets/conf/templates/config_template.xml
/usr/local/siets/conf/templates/default_desc.xml
/usr/local/siets/conf/templates/mail_config.xml
/usr/local/siets/conf/templates/mail_desc.xml
/usr/local/siets/conf/templates/mail_policy.xml
/usr/local/siets/conf/templates/policy_template.xml
/usr/local/siets/crawler/bin/cpy
/usr/local/siets/crawler/bin/crawld
/usr/local/siets/crawler/bin/crawldctl
/usr/local/siets/crawler/bin/dom_manager
/usr/local/siets/crawler/bin/down_manager
/usr/local/siets/crawler/bin/downloader
/usr/local/siets/crawler/bin/run_crawler
/usr/local/siets/crawler/conf/char_stats/EN_CP1257.stat
/usr/local/siets/crawler/conf/char_stats/LV_CP1257.stat
/usr/local/siets/crawler/conf/char_stats/LV_ISO88594.stat
/usr/local/siets/crawler/conf/char_stats/LV_UTF8.stat
/usr/local/siets/crawler/conf/char_stats/RU_CP1251.stat
/usr/local/siets/crawler/conf/char_stats/RU_KOI8R.stat
/usr/local/siets/crawler/conf/char_stats/RU_UTF8.stat
/usr/local/siets/crawler/conf/content.type
/usr/local/siets/crawler/conf/crawld_cfg.xml
/usr/local/siets/crawler/extensions/antiword/bin/antiword
/usr/local/siets/crawler/extensions/antiword/data/8859-1.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-10.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-13.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-14.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-15.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-16.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-2.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-3.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-4.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-5.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-6.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-7.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-8.txt
/usr/local/siets/crawler/extensions/antiword/data/8859-9.txt
/usr/local/siets/crawler/extensions/antiword/data/Default
/usr/local/siets/crawler/extensions/antiword/data/Example
/usr/local/siets/crawler/extensions/antiword/data/MacRoman.txt
/usr/local/siets/crawler/extensions/antiword/data/UTF-8.txt
/usr/local/siets/crawler/extensions/antiword/data/Unicode01
/usr/local/siets/crawler/extensions/antiword/data/Unicode15
/usr/local/siets/crawler/extensions/antiword/data/cp1250.txt
/usr/local/siets/crawler/extensions/antiword/data/cp1251.txt
/usr/local/siets/crawler/extensions/antiword/data/cp1252.txt
/usr/local/siets/crawler/extensions/antiword/data/cp437.txt
/usr/local/siets/crawler/extensions/antiword/data/cp850.txt
/usr/local/siets/crawler/extensions/antiword/data/cp852.txt
/usr/local/siets/crawler/extensions/antiword/data/cp862.txt
/usr/local/siets/crawler/extensions/antiword/data/cp866.txt
/usr/local/siets/crawler/extensions/antiword/data/fontnames
/usr/local/siets/crawler/extensions/antiword/data/fontnames.russian
/usr/local/siets/crawler/extensions/antiword/data/koi8-r.txt
/usr/local/siets/crawler/extensions/antiword/data/koi8-u.txt
/usr/local/siets/crawler/extensions/antiword/data/roman.txt
/usr/local/siets/crawler/extensions/antiword/lic/COPYING
/usr/local/siets/crawler/extensions/antiword/lic/ChangeLog
/usr/local/siets/crawler/extensions/antiword/lic/QandA
/usr/local/siets/crawler/extensions/antiword/lic/ReadMe
/usr/local/siets/crawler/extensions/pdftotext/bin/pdftotext
/usr/local/siets/crawler/extensions/pdftotext/lic/ANNOUNCE
/usr/local/siets/crawler/extensions/pdftotext/lic/CHANGES
/usr/local/siets/crawler/extensions/pdftotext/lic/COPYING
/usr/local/siets/crawler/extensions/pdftotext/lic/INSTALL
/usr/local/siets/crawler/extensions/pdftotext/lic/README
/usr/local/siets/crawler/extensions/ps2ascii/bin/ps2ascii
/usr/local/siets/crawler/extensions/ps2ascii/lic/Copying.htm
/usr/local/siets/crawler/extensions/ps2ascii/lic/Public.htm
/usr/local/siets/crawler/extensions/ps2ascii/lic/README
/usr/local/siets/crawler/extensions/rtf2html/bin/rtf2html
/usr/local/siets/crawler/extensions/rtf2html/lic/README
/usr/local/siets/crawler/extensions/rtf2html/lic/README.orig
/usr/local/siets/crawler/extensions/xlspptToHtml/bin/ppthtml
/usr/local/siets/crawler/extensions/xlspptToHtml/bin/xlhtml
/usr/local/siets/crawler/extensions/xlspptToHtml/lic/AUTHORS
/usr/local/siets/crawler/extensions/xlspptToHtml/lic/COPYING
