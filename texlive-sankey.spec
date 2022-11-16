Name:		texlive-sankey
Version:	61874
Release:	1
Summary:	Draw Sankey diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sankey
License:	lppl1.3 gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sankey.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sankey.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sankey.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros and an environment for creating
Sankey diagrams, i.e. flow diagrams in which the width of the
arrows is proportional to the flow rate.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/sankey
%{_texmfdistdir}/tex/latex/sankey
%doc %{_texmfdistdir}/doc/latex/sankey

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
