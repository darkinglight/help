syntax enable
set expandtab autoindent
set tabstop=4
set shiftwidth=4
set softtabstop=4
set number cursorline hls ic

set nocompatible              " be iMproved, required
set nu
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'ervandew/supertab'
Plugin 'fatih/vim-go'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/nerdcommenter'
Bundle 'majutsushi/tagbar'
Plugin 'Yggdroot/LeaderF'
Plugin 'jiangmiao/auto-pairs'
map <F8> :TagbarToggle<CR>
map <F3> :NERDTreeMirror<CR>
map <F3> :NERDTreeToggle<CR>
let g:tagbar_autopreview = 1
let g:tagbar_sort = 0
let g:tagbar_autofocus = 1  "这是tagbar一打开，光标即在tagbar页面内，默认在vim打开的文件内"
call vundle#end()            " required
filetype plugin indent on    " required
