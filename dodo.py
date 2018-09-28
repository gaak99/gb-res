### q&d resume format conversion doit(1) build script
##  --gb sep18

# DOIT_CONFIG = {
#     'verbosity': 2
# }

debugmemaybe=False

res_dir="/home/gb/Desktop/tech/find-job/spring18/resume-gh/gb-res"
res_base_f="gb-resume"
res_org_f=res_dir + "/" + res_base_f + ".org"
res_html_f=res_dir + "/" + res_base_f + ".html"

emacs25="/usr/local/bin/emacs"
remacs="~/warez/remacs-final/remacs/src/remacs" # remacs much newer code base than 25.3
emacs=emacs25 #choose wisely
emacs_opts_common="-Q --batch"
cmd_org2html=emacs + " " + emacs_opts_common + " " + res_org_f + " --funcall org-html-export-to-html --kill"

git_push='git push origin master'

git_add_html="git add " + res_base_f + ".html" + ' ' + res_base_f + '.org'
git_commit_html="git commit -m doit_auto_update " + res_base_f + ".html" + ' ' + res_base_f + '.org'
full_cmd_org2html=cmd_org2html + " && " + git_add_html + " && " + git_commit_html  + '&&' + git_push
if debugmemaybe:
    print("gbdebug_full_org2html: %s" % full_cmd_org2html)

res_txt_f=res_dir + "/" + res_base_f + ".txt"
export_txt_el="scripts/export-txt.el"
cmd_org2txt=emacs + " " + emacs_opts_common + " " + "--script" + " " + export_txt_el + " --kill"

git_add_txt="git add " + res_base_f + ".txt"
git_commit_txt="git commit -m doit_auto_update " + res_base_f + ".txt"
full_cmd_org2txt=cmd_org2txt + " && " + git_add_txt + " && " + git_commit_txt + '&&' + git_push
if debugmemaybe:
    print("gbdebug_full_org2txt: %s" % full_cmd_org2txt)

def task_res_org2html():
    return {'actions': [full_cmd_org2html],
            'file_dep': [res_org_f],
            'targets': [res_html_f]
            }

def task_res_org2txt():
    return {'actions': [full_cmd_org2txt],
            'file_dep': [res_org_f],
            'targets': [res_txt_f]
            }

io_base_f='index.html'
io_dir='../gaak99.github.io/resume/'
io_f=io_dir + io_base_f
cmd_io_update='cp ' + res_html_f + ' ' + io_f

git_add_io='git add ' + io_base_f
git_commit_io='git commit -m doit_auto_update ' + io_base_f
full_cmd_io_update=cmd_io_update + '&&' + 'cd ' + io_dir + '&&' + git_add_io + '&&' + git_commit_io  + '&&' + git_push
if debugmemaybe:
    print("gbdebug_full_cmd_io_update: %s" % full_cmd_io_update)

def task_res_io_update():
    return {'actions': [full_cmd_io_update],
            'file_dep': [res_html_f],
            'targets': [io_f]
            }
