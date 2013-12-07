# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/oldstyle
# catalog-date 2009-03-08 21:39:02 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-oldstyle
Version:	0.2
Release:	4
Summary:	Old style numbers in OT1 encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oldstyle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Font information needed to load the cmmi and cmmib fonts for
use to produce oldstyle numbers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 754528
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719159
- texlive-oldstyle
- texlive-oldstyle
- texlive-oldstyle
- texlive-oldstyle

