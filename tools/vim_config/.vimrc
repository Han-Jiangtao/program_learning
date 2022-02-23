" Han vimrc
" 显示行号
set number 
" 不与vi兼容
set nocompatible
" 语法高亮
syntax on
" 显示当前工作模式
set showmode
" 显示当前指令
set showcmd
" 使用utf-8编码
set encoding=utf-8
" 文件类型检测开启
filetype on
" 文件类型检测插件开启
filetype plugin on
" 文件后缀检测锁进
filetype indent on
" tab自动转换为空格
set expandtab
" tab和缩进替换为四个空格
set tabstop=4
" << 和 >> 为移动4字符
set shiftwidth=4
" tab转化为4个空格
set softtabstop=4
" 光标所在行高亮
set cursorline
" 光标所在列高亮
set cursorcolumn
" 高亮第120列字符限制
set colorcolumn=120
" 自动高亮配对字符，如左右括号
set showmatch
" 高亮显示匹配结果
set hlsearch
" 每输入一个字符即跳转到匹配的第一个位置
set incsearch
" 搜索忽略大小写
set ignorecase
" 出错时不要出声
set noerrorbells
" 出错时，视觉提示
set visualbell
" 多文件编辑时，自动切换至当前文件工作目录
set autochdir
" 记录1000次历史操作
set history=1000
" 显示标尺
set ruler
" 保存.vimrc立即生效
autocmd BufWritePost $MYVIMRC source $MYVIMRC
" 显示不可见字符譬如tab和空格
set list
" 显示空格和tab
set listchars=tab:>-,trail:.,eol:<
" unix回车换行
set fileformat=unix
" vim使用系统剪切板
set clipboard=unnamed
" 显示编辑文件名
set laststatus=2
" 显示编辑文件绝对路径
set statusline+=%F
" 显示中文帮助
if version >= 603
    " 主要由helptags控制，如果没有设置则遍历$runtimepath/doc
    " runtimepath可以set runtimepath?来查询
    set helplang=cn
    set encoding=utf-8
endif
" 设置自定义<leader>
" let mapleader="\<space>"
let mapleader=","
" insert mode remap
" 自动补全对称字符
inoremap ( ()<ESC>i
inoremap { {}<ESC>i
inoremap [ []<ESC>i
inoremap " ""<ESC>i
inoremap ' ''<ESC>i
inoremap < <><ESC>i
" 按键映射
inoremap jj <ESC>

" Plug accelerator key
" nerdtree plug accelerator"
nnoremap <leader>d :NERDTreeToggle<CR>
nnoremap <leader>v :NERDTreeFind<CR>
let NERDTreeShowHidden=1
let NERDTreeIgnore = ['\.pyc','\~$','\.swp', '\.git']
" markdown-preview.vim plug accelerator
nmap <silent> <leader>8 <Plug>MarkdownPreview        " for normal mode
imap <silent> <leader>8 <Plug>MarkdownPreview        " for insert mode
nmap <silent> <leader>9 <Plug>StopMarkdownPreview    " for normal mode
imap <silent> <leader>9 <Plug>StopMarkdownPreview    " for insert mode

call plug#begin("~/.vim/autoplug")
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'ctrlpvim/ctrlp.vim'
Plug 'iamcco/mathjax-support-for-mkdp'
Plug 'iamcco/markdown-preview.vim'
call plug#end()
