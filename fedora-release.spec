%define release_name Goethe
%define release_version 6

Summary:	Fedora Core release files
Name:		fedora-release
Version:	6.1
Release:	1
License:	GFDL
Group:		System Environment/Base
URL:		http://fedoraproject.org
Source:		fedora-release-%{version}.tar.gz
Obsoletes:	redhat-release
Provides:	redhat-release
Requires:	fedora-release-notes >= %{release_version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Fedora Core release files

%prep
%setup -q -n fedora-release-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
echo "Fedora Core release %{release_version} (%{release_name})" > $RPM_BUILD_ROOT/etc/fedora-release
cp $RPM_BUILD_ROOT/etc/fedora-release $RPM_BUILD_ROOT/etc/issue
echo "Kernel \r on an \m" >> $RPM_BUILD_ROOT/etc/issue
cp $RPM_BUILD_ROOT/etc/issue $RPM_BUILD_ROOT/etc/issue.net
echo >> $RPM_BUILD_ROOT/etc/issue
ln -s fedora-release $RPM_BUILD_ROOT/etc/redhat-release
mkdir -p $RPM_BUILD_ROOT/usr/share/eula $RPM_BUILD_ROOT/usr/share/firstboot/modules
cp -f eula.txt $RPM_BUILD_ROOT/usr/share/eula/eula.en_US
cp -f eula.py $RPM_BUILD_ROOT/usr/share/firstboot/modules/eula.py

mkdir -p -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
for file in RPM-GPG-KEY* ; do
	install -m 644 $file $RPM_BUILD_ROOT/etc/pki/rpm-gpg
done

mkdir -p -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in fedora*repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0644,root,root) /etc/fedora-release
/etc/redhat-release
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/*
%doc eula.txt GPL 
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
/usr/share/firstboot/modules/eula.py*
/usr/share/eula/eula.en_US
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/*

%changelog
* Thu Oct  5 2006 Jesse Keating <jkeating@redhat.com> - 6.1-1
- replace old mirror files with new mirrorlist cgi system

* Thu Oct  5 2006 Jesse Keating <jkeating@redhat.com> - 6-1
- Rebuild for Fedora Core 6 release

* Tue Sep  5 2006 Jesse Keating <jkeating@redhat.com> - 5.92-1
- Bump for FC6 Test3

* Thu Jul 27 2006 Jesse Keating <jkeating@redhat.com> - 5.91.1-1
- Convert deprecated gtk calls. (#200242)
- Fix some of the versioning

* Sun Jul 23 2006 Jesse Keating <jkeating@redhat.com> - 5.91-4
- Bump for FC6 Test2
- Remove release-notes content, now standalone package
- Don't replace issue and issue.net if the end user has modified it
- Require fedora-release-notes
- Cleanups

* Mon Jun 19 2006 Jesse Keating <jkeating@redhat.com> - 5.90-3
- Cleanups

* Thu Jun 15 2006 Jesse Keating <jkeating@redhat.com> - 5.90-1
- Update for 5.90

* Wed May 24 2006 Jesse Keating <jkeating@redhat.com> - 5.89-rawhide.2
- Update to get new devel repo file
- merge minor changes from external cvs .spec file

* Wed Apr 19 2006 Jesse Keating <jkeating@redhat.com> - 5.89-rawhide.1
- Look, a changelog!
- Removed duplicate html/css content from doc dir.
- Add lynx as a buildreq

