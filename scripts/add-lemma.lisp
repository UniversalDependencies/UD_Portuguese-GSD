
(ql:quickload :cl-conllu)
(ql:quickload :cl-fad)
(ql:quickload :cl-ppcre)

(in-package :conllu.user)

(defun match (tk pat)
  (and (or (equal "*" (car pat))
	   (cl-ppcre:scan (format nil "^(~a)$" (nth 0 pat)) (token-form tk)))
       (equal (nth 2 pat) (token-upostag tk))
       (equal (nth 3 pat) (token-deprel tk))))

(defun add-lemma (tk)
  (let* ((patterns '(("[,\\.()-:\"?/!]"    "*"  "PUNCT" "punct")
		     ("o|a|um"             "*"  "DET"   "det")
		     ("uma"                "um" "DET"   "det")
		     ("e|ou|mas"           "*"  "CCONJ" "cc")
		     ("que"                "*"  "CCONJ" "mark")
		     ("O|A|As|Os|as"       "o"  "DET"   "det")
		     ("de|em|com|para|por|como" "*" "ADP" "case")
		     ("Em" "em" "ADP" "case")))
	 (p  (find tk patterns :test #'match)))
    (when (and (equal "_" (token-lemma tk)) p)
    (if (equal "*" (cadr p))
	(setf (token-lemma tk) (token-form tk))
	(setf (token-lemma tk) (cadr p))))))

(defun fix-conllu (sentences)
  (mapc (lambda (s) (mapc #'add-lemma (sentence-tokens s))) sentences))

;; to replicate
;; (write-conllu (fix-corpus (read-conllu "bosque.udep.conll")) "bosque.fixed")
(defun run ()
  (dolist (f (cl-fad:list-directory #p "documents/"))
    (write-conllu (fix-conllu (read-conllu f)) f)))
