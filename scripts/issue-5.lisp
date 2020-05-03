
(ql:quickload :cl-conllu)

(let (res)
  (dolist (fn (directory "*.conllu"))
    (let ((resfile nil)
	  (changed nil)
	  (sentences (read-conllu fn)))
      (dolist (s sentences)
	(dolist (tk (sentence-tokens s))
	  (if (equal "XXXXX" (token-misc tk))
	      (progn
		(setf (token-misc tk) "_"
		      changed t)
		(push (list fn (sentence-id s) (token-id tk)) resfile)))))
      (push resfile res)
      (if changed (write-conllu sentences fn))))
  (with-open-file (out "issue-5.log" :direction :output :if-exists :supersede)
    (write res :stream out))
  (mapcar #'length res))

;; ouput (153 11 15)
