%global debug_package   %{nil}
%global import_path     github.com/gorilla/mux
%global gopath          %{_datadir}/gocode
%global commit          136d54f81f00414c45c3c68dd47e98cc97519c5e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-gorilla-mux
Version:        0
Release:        0.16.git%{shortcommit}%{?dist}
Summary:        A powerful URL router and dispatcher for golang
License:        BSD
URL:            http://www.gorillatoolkit.org/pkg/mux
Source0:        https://github.com/gorilla/mux/archive/%{commit}/mux-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Package gorilla/mux implements a request router and dispatcher.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of
registered routes and calls a handler for the route that matches the URL or
other conditions.

%package devel
Requires:       golang
Requires:       golang(github.com/gorilla/context)
Summary:        A powerful URL router and dispatcher for golang
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
Package gorilla/mux implements a request router and dispatcher.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of
registered routes and calls a handler for the route that matches the URL or
other conditions.

This package contains library source intended for building other packages
which use gorilla/mux.


%prep
%setup -n %setup -n mux-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}


%files devel
%doc LICENSE README.md
%dir %{gopath}/src/github.com/gorilla
%dir %{gopath}/src/github.com/gorilla/mux
%{gopath}/src/%{import_path}/*.go

%changelog
* Tue Jan 27 2015 jchaloup <jchaloup@redhat.com> - 0-0.16.git136d54f
- bump the release
  related: #1147843

* Thu Jul 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.15.git
- do not own dirs owned by golang
- archfulness and defattr for el6 handled separately

* Wed Jun 18 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> 0-0.12.git
- Resolves: rhbz#1108720 - update for docker 1.0.0
- Resolves: rhbz#1110512 - restrict arch to x86_64

* Sat May 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.git
- update to commit 136d54f81f (required for docker 1.0
https://github.com/dotcloud/docker/issues/5908 )

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.gite718e93
- add check

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.11.gite718e93
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.10.gite718e93
- require golang 1.2 and later

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.gite718e93
- double quotes removed from provides and br

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.8.gite718e93
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.7.gite718e93
- exclusivearch as per golang package
- debug_package nil

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.6.gite718e93
- install just the source code for devel package

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.gite718e93
- Version format changed
- docdir changed
- debuginfo no longer generated
- package owns all directories in import_path

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> gite718e93-4
- only devel package generated
- Provides moved to devel package

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> gite718e93-3
- Depends on golang("github.com/gorilla/context"), not golang directly
- Pkg archives handled (thanks to Vincent Batts (vbatts@redhat.com)
- Devel package generated

* Wed Aug 28 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-2
- Fixed permissions

* Mon Aug 26 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-1
- Initial fedora package
