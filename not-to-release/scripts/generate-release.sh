
cat documents/pt_gsd-ud-dev-*.conllu > pt_gsd-ud-dev.conllu
cat documents/pt_gsd-ud-train-*.conllu > pt_gsd-ud-train.conllu
cat documents/pt_gsd-ud-test-*.conllu > pt_gsd-ud-test.conllu

awk '$0 ~ /^# sent_id =/ {print substr($4,8)}' pt_gsd-ud-train.conllu > a
sort -n < a > b
diff a b
rm a b

awk '$0 ~ /^# sent_id =/ {substr($4,6)}' pt_gsd-ud-dev.conllu > a
sort -n < a > b
diff a b
rm a b

awk '$0 ~ /^# sent_id =/ {print substr($4,7)}' pt_gsd-ud-test.conllu > a
sort -n < a > b
diff a b
rm a b

