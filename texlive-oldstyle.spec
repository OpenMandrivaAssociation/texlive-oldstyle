Name:		texlive-oldstyle
Version:	15878
Release:	2
Summary:	Old style numbers in OT1 encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oldstyle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
