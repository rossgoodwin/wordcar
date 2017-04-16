cd /home/rg/projects/wc3/torch-rnn
/home/rg/torch/install/bin/th sample_zoedtry.lua -checkpoint "$1" &
cd /home/rg/projects/wc3/densecap
/home/rg/torch/install/bin/th run_model.lua &

