Name:		texlive-oldstyle
Version:	0.2
Release:	1
Summary:	Old style numbers in OT1 encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oldstyle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Font information needed to load the cmmi and cmmib fonts for
use to produce oldstyle numbers.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/oldstyle/Ucmm.fd
%{_texmfdistdir}/tex/latex/oldstyle/oldstyle.sty
%doc %{_texmfdistdir}/doc/latex/oldstyle/oldstyle.pdf
#- source
%doc %{_texmfdistdir}/source/latex/oldstyle/oldstyle.dtx
%doc %{_texmfdistdir}/source/latex/oldstyle/oldstyle.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
