#!/bin/sh

TODAY=`date +%F`

echo "[INFO] Retrieving RedCAP RECODID survey results for ${TODAY}."
DATA="token=FC27DF4DCB5AC2BC24645C1430435AF3&content=record&format=csv&type=flat&csvDelimiter=&rawOrLabel=raw&rawOrLabelHeaders=raw&exportCheckboxLabel=false&exportSurveyFields=false&exportDataAccessGroups=false&returnFormat=csv"
CURL=`which curl`
$CURL -H "Content-Type: application/x-www-form-urlencoded" \
      -H "Accept: application/json" \
      -X POST \
      -d $DATA \
      https://cru.med.uni-heidelberg.de/redcap/api/ > data/RECODID_RedcapSurvey_${TODAY}.txt \

echo "[INFO] Filtering received survey results."
python3 Covid_Redcap.py -f RECODID_RedcapSurvey_${TODAY}.txt > data/Survey_Summary_${TODAY}.txt
