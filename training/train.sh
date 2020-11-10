#!/usr/bin/env bash

echo "Training the model..."

#"Yep, you are right, we are not really training any model here, just pretending."

if [ -f model.pkl ]; then
    rm model.pkl
fi
cp hyperparams.json model.pkl
echo "{\"loss\": 1.$(jq '.n_layers' hyperparams.json)}" > metrics.json
