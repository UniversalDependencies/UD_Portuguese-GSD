
(ql:quickload '(:serapeum :cl-conllu))

(in-package :cl-conllu)

;; (defun split (lst num)
;;   (labels ((recurse (lst num acc)
;; 	     (if (null? lst)
;; 		 acc
;; 		 (recurse (subseq lst num) num (append acc (list (subseq lst 0 num)))))))
;;     (recurse lst num '())))


(defun split-and-save (fn path num)
  (let* ((sentences (read-conllu fn))
	 (lists     (serapeum:batches sentences num))
	 (counter   0))
    (mapc (lambda (lst)
	    (write-conllu lst
			  (merge-pathnames (format nil "~a-~4,'0d.conllu" (pathname-name fn) (incf counter))
					   path)))     
	  lists)))

(defun main ()
  (mapc (lambda (fn)
	  (split-and-save fn #P"/Users/ar/work/ud-portuguese-gsd/documents/" 10))
	(directory "../*.conllu")))


