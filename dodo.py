### q&d resume format conversion doit(1) build script
##  --gb sep18

# DOIT_CONFIG = {
#     'verbosity': 2
# }

res_dir="/home/gb/Desktop/tech/find-job/spring18/resume-gh/gb-res"
res_base_f="gb-resume"
res_org_f=res_dir + "/" + res_base_f + ".org"
res_html_f=res_dir + "/" + res_base_f + ".html"

emacs25="/usr/local/bin/emacs"
remacs="~/warez/remacs-final/remacs/src/remacs" # remacs much newer code base than 25.3
emacs_opts_common="-Q --batch"
cmd_org2html=remacs + " " + emacs_opts_common + " " + res_org_f + " --funcall org-html-export-to-html --kill"
#git_add="git add " + res_base_f + ".html"
#git_commit="git commit -m doit_auto_update " + res_base_f + ".html"
#full_cmd_org2html=cmd_org2html + " && " + git_add + " && " + git_commit

print("gbdebug org2html: %s" % cmd_org2html)

def task_res_org2html():
    return {'actions': [cmd_org2html],
            'file_dep': [res_org_f],
            'targets': [res_html_f]
            }
