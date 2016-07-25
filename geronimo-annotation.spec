%global pkg_name geronimo-annotation
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global spec_ver 1.1
%global spec_name geronimo-annotation_%{spec_ver}_spec

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.0
Release:          15.7%{?dist}
Summary:          Java EE: Annotation API v1.1
License:          ASL 2.0
URL:              http://geronimo.apache.org/

Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz
BuildArch:        noarch

BuildRequires:    %{?scl_prefix}javapackages-tools
BuildRequires:    %{?scl_prefix}maven-local
BuildRequires:    %{?scl_prefix}geronimo-parent-poms
BuildRequires:    %{?scl_prefix}maven-resources-plugin


%description
This package defines the common annotations.

%package javadoc
Summary:          Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.


%prep
%setup -q -n %{spec_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
sed -i 's/\r//' LICENSE NOTICE
%pom_set_parent org.apache.geronimo.specs:specs:1.4

%mvn_alias : org.apache.geronimo.specs:geronimo-annotation_1.0_spec
%mvn_alias : javax.annotation:jsr250-api
%mvn_alias : org.eclipse.jetty.orbit:javax.annotation

%mvn_file : %{pkg_name} annotation
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-15.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-15.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-15.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-15.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-15.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-15.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-15.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-15
- Mass rebuild 2013-12-27

* Thu Aug 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-14
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-13
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-12
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#917620

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9
- Install NOTICE file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar  6 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-7
- Add javax.annotation:jsr250-api to depmap

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-5
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 4 2010 Chris Spike <chris.spike@arcor.de> 1.0-3
- Added 'org.apache.geronimo.specs:geronimo-annotation_1.0_spec' to maven depmap

* Mon Jul 26 2010 Chris Spike <chris.spike@arcor.de> 1.0-2
- Fixed whitespace/tabs use
- Fixed wrong EOL encoding

* Sun Jul 18 2010 Chris Spike <chris.spike@arcor.de> 1.0-1
- Initial version of the package
