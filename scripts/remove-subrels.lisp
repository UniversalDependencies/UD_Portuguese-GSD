
(ql:quickload :cl-conllu)
(ql:quickload :cl-fad)
(ql:quickload :cl-ppcre)

(in-package :conllu.user)

(defun match (tk pat)
  (and (or (equal "*" (car pat))
	   (cl-ppcre:scan (format nil "^(~a)$" (nth 0 pat)) (token-form tk)))
       (equal (nth 2 pat) (token-upostag tk))
       (equal (nth 3 pat) (token-deprel tk))))

(defun fix-deprel (tk)
  (when (or (equal "xcomp:adj" (token-deprel tk))
	    (equal "acl:part" (token-deprel tk)))
    (setf (token-deprel tk) (car (cl-ppcre:split ":" (token-deprel tk))))))

(defun fix-conllu (sentences)
  (mapc (lambda (s) (mapc #'fix-deprel (sentence-tokens s))) sentences))


(defun run ()
  (dolist (f (cl-fad:list-directory #p "documents/"))
    (write-conllu (fix-conllu (read-conllu f)) f)))
