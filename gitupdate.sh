#! /usr/bin/bash

array_name=(
bashion_ktv 
netEase 
pythonLearn 
);

bash_str=$(pwd)/
bash_log=log.md

for i in ${array_name[@]};
do
    log=$bash_str$bash_log
    use_str=$bash_str$i
    date >> $log
    echo '###'$use_str >> $log
    echo '-------------NOW IS :--------------'
    pwd
    cd $use_str
    git add *  > /dev/null
    git commit -m 'sudo commit' > /dev/null
    git status >> $log
    git push origin master >> $log
    git status >> $log
    echo '---------' >> $log
    echo '' >> $log
done

