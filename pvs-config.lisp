;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; -*- Mode: Lisp -*- ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(in-package :cl-user)

(export '(*pvs-path* *pvs-binary-type* bye))

(defparameter *pvs-path* "/homes/owre/pvs3.3")

;;; The *pvs-binary-type* is used to be able to build PVS under several
;;; lisps/platforms without rerunning configure each time

(defvar *pvs-binary-type*
  #+(and allegro sparc) "fasl"		; Sun4
  #+(and allegro rios) "rfasl"		; PowerPC/RS6000
  #+(and allegro hpux) "hfasl"		; HP 9000
  #+(and allegro linux x86) "lfasl"		; Intel x86
  #+(and allegro macosx powerpc) "mfasl" ; Mac OS X powerpc
  #+(and allegro macosx x86) "nfasl"	; Mac OS X intel
  #+(and lucid lcl4.1 sparc) "sbin"	; Sun4 new Lucid
  #+(and lucid (not lcl4.1) sparc) "obin" ; Sun4 old Lucid
  #+(and lucid rios) "rbin"		; PowerPC/RS6000
  #+(and lucid mips) "mbin"		; DEC
    ;;; These are experimental
  #+gcl "o"
  #+(and cmu linux) "x86f"
  #+(and cmu darwin) "ppcf"
  #+(and cmu solaris) "sparcf"
  #+(and clisp pc386) "clfasl"
  #+harlequin-common-lisp "wfasl"
  )

#+allegro
(eval-when (eval load)
  (setq *ignore-package-name-case* t))

#+allegro
(eval-when (eval load)
  (setq excl:*fasl-default-type* *pvs-binary-type*)
  (setq system:*load-search-list*
	(list #p"" (make-pathname :type *pvs-binary-type*)
	      #p(:type "cl") #p(:type "lisp"))))

#+cmu
(eval-when (eval load)
  (setq extensions:*load-object-types*
	(remove "fasl" extensions:*load-object-types* :test #'string=)))

#+allegro
(setq *cltl1-in-package-compatibility-p* t)

#+lucid
(unless (fboundp 'bye)
  (defun bye (&optional (exit-status 0))
    (quit exit-status)))

#+allegro
(defun bye (&optional (exit-status 0))
  (excl:exit exit-status))

#+harlequin-common-lisp
(defun bye (&optional (exit-status 0))
  (system::bye exit-status))

#+cmu
(defun bye (&optional (exit-status 0))
  (unix:unix-exit exit-status))
