
(ql:quickload '(:dexador :cl-ppcre :yason :cl-conllu :alexandria))

(defun proc-reports ()
  (reduce (lambda (res fn) 
	    (let ((data (reduce (lambda (res a)
				  (multiple-value-bind (m r) 
				      (ppcre:scan-to-strings "\\[Line [0-9]+ Sent ((train|test|dev)-s[0-9]+) Node [0-9]+\\]" a)
				    (if m (cons (aref r 0) res) res)))
				(uiop:read-file-lines fn) :initial-value nil))) 
	      (if data (cons (list 'file (pathname-name fn) 'sents (remove-duplicates data :test #'equal)) res) res))) 
	  (directory "reports/pt_gsd-ud-*.report") :initial-value nil))


;; total number of sentences
(loop for a in (proc-reports)
      sum (length (getf a 'sents)))

(defun get-sentences (fn sents)
  (let* ((as (cl-conllu:read-conllu (make-pathname :name fn
						   :directory '(:RELATIVE "documents")
						   :type "conllu")))
	 (bs (loop for s in as
		   collect (if (member (cl-conllu:sentence-id s) sents :test #'equal)
			       (let* ((new (do-parse (cl-conllu:sentence-text s)))
				      (new-meta (cl-conllu:sentence-meta new))
				      (tb (alexandria:alist-hash-table (cl-conllu:sentence-meta s))))
				 (setf (gethash "generator" tb)      (cdr (assoc "generator" new-meta :test #'equal))
				       (gethash "udpipe_model" tb)   (cdr (assoc "udpipe_model" new-meta :test #'equal))
				       (cl-conllu:sentence-meta new) (alexandria:hash-table-alist tb))
				 new)
			       s))))
    (cl-conllu:write-conllu bs (make-pathname :name fn :directory '(:RELATIVE "documents") :type "new"))))

(defun do-parse (sent)
  "returns a text representation of a sentence in conllu format."
  (let* ((response (dex:post "http://lindat.mff.cuni.cz/services/udpipe/api/process" 
			     :content `(("tagger" . "")
					("parser" . "") 
					("tokenizer" . "presegmented")
					("model" . "portuguese-bosque-ud-2.12-230717")
					("data" . ,sent))))
	 (result (gethash "result" (yason:parse response))))
    (with-input-from-string (in result)
      (car (cl-conllu:read-conllu in)))))



