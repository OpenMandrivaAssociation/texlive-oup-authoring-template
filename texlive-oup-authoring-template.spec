%global tl_name oup-authoring-template
%global tl_revision 79192

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	A general template for journals published by Oxford University Press (OUP)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/oup-authoring-template
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oup-authoring-template.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oup-authoring-template.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a general LaTeX template for journals published by
Oxford University Press (OUP). The template outputs to the three
official page designs (traditional, contemporary, modern) used by many
journals published by OUP, with large, medium and small page options.
For more information see
https://academic.oup.com/journals/pages/authors/preparing_your_
manuscript.

