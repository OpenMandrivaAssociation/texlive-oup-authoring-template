Name:		texlive-oup-authoring-template
Version:	64491
Release:	2
Summary:	A general template for journals published by Oxford University Press (OUP)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oup-authoring-template
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oup-authoring-template.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oup-authoring-template.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a general LaTeX template for journals
published by Oxford University Press (OUP). The template
outputs to the three official page designs (traditional,
contemporary, modern) used by many journals published by OUP,
with large, medium and small page options. For more information
see
https://academic.oup.com/journals/pages/authors/preparing_your_
manuscript.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/oup-authoring-template
%doc %{_texmfdistdir}/doc/latex/oup-authoring-template

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
