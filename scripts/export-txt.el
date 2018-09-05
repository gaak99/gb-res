;;; q&d ox-pandoc "script" for remacs --batch --script
;;  sep18, xps13

(let ((myorgf "~/Desktop/tech/find-job/spring18/resume-gh/gb-res/gb-resume.org")
      (dash_path "/home/gb/.emacs.d/elpa/dash-2.13.0/")
      (ht_path "~/.emacs.d/elpa/ht-2.2/")
      (ox_pandoc_path "~/warez/emacs-lisp/ox-pandoc/"))
  (setq load-path
	(cons (expand-file-name dash_path) load-path))
  (setq load-path
	(cons (expand-file-name ht_path) load-path))
  (setq load-path
	(cons (expand-file-name ox_pandoc_path) load-path))
  (load-library "ox-pandoc")
  (find-file myorgf)
  ;(org-pandoc-export-as-asciidoc)
  (org-pandoc-export-to-asciidoc)
  (sleep-for 2); hack-alert - seems needed so far in batch mode
  )
