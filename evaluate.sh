#!/bin/bash

info="[SCRIPT INFO]"

function evaluate() {
	#for ipdb in ${LIST_PDBS_BASIC[@]}; do
	#for ipdb in ${LIST_PDBS_MAX_8_ROTBONDS[@]}; do
	for ipdb in ${LIST_PDBS_FULL[@]}; do
    	echo " "
    	for ipopsize in ${LIST_PSIZES[@]}; do
			echo " "
			for ilsmet in ${LS_METHODS[@]}; do
				echo " "
				$1 \
				-lsmet ${ilsmet} \
				-lsit 300 -lsrat 100.000000 -smooth 0.500 \
				-nev ${NEV} -ngen ${NGEN} -nrun ${NRUN} -psize ${ipopsize}\
				-lfile ${EVAL_INPUTS_20_DIR}/${ipdb}/rand-0.pdbqt \
				-xraylfile ${EVAL_INPUTS_20_DIR}/${ipdb}/flex-xray.pdbqt \
				-ffile ${EVAL_INPUTS_20_DIR}/${ipdb}/protein.maps.fld \
				-resnam $2/${ipdb}_${ipopsize}_${ilsmet}_"`date +"%Y-%m-%d-%H:%M"`"
			done
      	done
  	done
}
