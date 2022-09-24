#USAGE: ie3.sh input_vcf_file nucleotide_of_interest
nucoi=$2

grep -v "#" $1 | awk '{if ($4)==$nucoi) {print $5}}' | sort | uniq -c






grep -v pro=$pro | awk '{if ($4) == pro) {print $5}}' | sort | uniq -c