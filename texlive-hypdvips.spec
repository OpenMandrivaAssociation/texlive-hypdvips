# revision 23377
# category Package
# catalog-ctan /macros/latex/contrib/hypdvips
# catalog-date 2011-06-07 18:10:36 +0200
# catalog-license lppl1.3
# catalog-version 2.03
Name:		texlive-hypdvips
Version:	2.03
Release:	1
Summary:	Hyperref extensions for use with dvips
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hypdvips
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdvips.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdvips.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The hypdvips package fixes some problems when using hyperref
with dvips. It also adds support for breaking links, file
attachments, embedded documents and different types of GoTo-
links. The cooperation of hyperref with cleveref is improved,
which in addition allows an enhanced back-referencing system.

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
%{_texmfdistdir}/tex/latex/hypdvips/hypdvips.sty
%doc %{_texmfdistdir}/doc/latex/hypdvips/README
%doc %{_texmfdistdir}/doc/latex/hypdvips/hypdvips.pdf
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ex1.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ex2.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ex3.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ex4.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ex5.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ex6.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ex7.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/graph.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/icon_draft.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/ids.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/logfile.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/openmsg_six.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/openmsg_sixinbrowser.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/paperclip.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/pushpin.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/images/tag.eps
%doc %{_texmfdistdir}/doc/latex/hypdvips/manifest.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
