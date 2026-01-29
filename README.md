# tuebingen.ai stylepack
Style pack for the [Tübingen AI Center](https://tuebingen.ai), with templates for slides, theses, and more. 

This repository contains templates for documents under the branding of the Tübingen AI Center. The bulk of the contents is licensed under the MIT license, with the exception of the logo files, which are ``all rights reserved'' and should only be used by faculty, employees and students of the AI Center, with the correct affiliations. 

The pack currently contains the following LaTeX assets:
* a template for beamer slides, with various macros, available in the `beamer-theme` directory
* a template for Master's and Bachelor's theses that follows the content guidelines of the Tübingen CS department, available in the `thesis-template` directory. 
 
These documents have matching style sheets in the [`tueplots`](https://tueplots.readthedocs.io/) python library, which can be used to generate plots that match the style of the documents.

## Installation

If you would like to contribute to this repository, please feel free to open an issue or a pull request. In particular, we welcome proposals for templates for posters, and PhD theses.

Let's assume the following sample project structure

```
icml_2026/
|- slides.tex
|- latexmkrc
|- ...
```

and that that `icml_2026/` is the working directory (otherwise, execute `cd icml_2026`).

1.  Make sure Git LFS is installed. (e.g. via `brew install git-lfs` on macOS)

2.  Install the required fonts on your system (see section 'Fonts' below).

3.  Clone the theme repo into `icml_2026/theme`:
    ```sh
    git clone https://github.com/philipphennig/tueaistylepack.git icml_2026/theme
    ```
    If `icml_2026/` is (or lies in) a Git repo itself, we can use a [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules):
    ```sh
    cd icml_2026
    git submodule add https://github.com/philipphennig/tueaistylepack.git theme
    ```

4.  Add
    ```TeX
    \usetheme{tueai}
    ```
    to the preamble of `icml_2026/slides.tex`.

5.  To make sure that {pdf,Lua,Xe}LaTeX finds the theme files, make sure to add the line
    ```Perl
    ensure_path("TEXINPUTS", "./theme//");
    ```
    to `icml_2026/latexmkrc` and compile via `latexmk slides.tex`.
    Moreover, if you want to use LuaLaTeX or XeLaTeX to compile the document, add
    ```Perl
    $pdf_mode = <mode>;
    $dvi_mode = 0;
    $postscript_mode = 0;
    ```
    to `icml_2026/latexmkrc`, replacing `<mode>` with `4` for LuaLaTeX or `5` for XeLaTeX.
    Note that the custom fonts only work with {Lua,Xe}LaTeX.
    If you work with Visual Studio Code, adding
    ```TeX
    %!LW recipe=latexmk (latexmkrc)
    as the first line in `icml_2026/slides.tex` will ensure that LaTeX Workshop compiles the document using the information provided in `icml_2026/latexmkrc`.

## Fonts

The theme uses the [Roboto](https://fonts.google.com/specimen/Roboto) and [+Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) Families (Light, Regular, Medium, etc.). The latter is an open replacement for the Circular font family used in the Tübingen AI Center's corporate design, and can be downloaded for free from [Google Fonts](https://fonts.google.com/) via the links above.

## Contributors

This repo is maintained by Philipp Hennig, who also wrote the thesis template. The beamer template is based on an earlier template built by Philipp Hennig and Marvin Pförtner. We are grateful to Peter Nicholas Krämer for maintaining `tueplots`, including the hooks in there for this style pack.

The color scheme, the Tübingen AI Logo, and various other design assets were developed by [Franziska Schwarz](https://www.franziska-schwar.de). 