%global tl_name hypdvips
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.03
Release:	%{tl_revision}.1
Summary:	Hyperref extensions for use with dvips
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hypdvips
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdvips.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdvips.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The hypdvips package fixes some problems when using hyperref with dvips.
It also adds support for breaking links, file attachments, embedded
documents and different types of GoTo-links. The cooperation of hyperref
with cleveref is improved, which in addition allows an enhanced back-
referencing system.

