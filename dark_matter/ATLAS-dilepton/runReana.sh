ana=ATLAS-LAPP-DM
reana-client create -w $ana
reana-client create -n $ana -f reana-$ana.yaml
export REANA_WORKON=$ana
reana-client upload
reana-client start
