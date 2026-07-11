%global tl_name oldstyle
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Old style numbers in OT1 encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/oldstyle
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oldstyle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Font information needed to load the cmmi and cmmib fonts for use to
produce oldstyle numbers.

