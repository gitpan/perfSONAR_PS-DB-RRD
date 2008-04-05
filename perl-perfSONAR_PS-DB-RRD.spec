Name:           perl-perfSONAR_PS-DB-RRD
Version:        0.09
Release:        1%{?dist}
Summary:        perfSONAR_PS::DB::RRD Perl module
License:        distributable, see LICENSE
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/perfSONAR_PS-DB-RRD/
Source0:        http://www.cpan.org/modules/by-module/perfSONAR_PS/perfSONAR_PS-DB-RRD-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(Data::Compare)
Requires:       perl(Log::Log4perl) >= 1
Requires:       perl(Params::Validate) >= 0.64
Requires:       perl(RRDp) >= 1.2
Requires:       perl(perfSONAR_PS::Common) >= 0.09
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
perfSONAR_PS::DB::RRD is a module that provides a perfSONAR_PS::DB interface
to an RRD database.

%prep
%setup -q -n perfSONAR_PS-DB-RRD-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README perl-perfSONAR_PS-DB-RRD.spec
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Mar 27 2008 aaron@internet2.edu 0.09-1
- Specfile autogenerated.
