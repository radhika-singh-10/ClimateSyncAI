#!/usr/bin/env bash
set -e
echo "Starting model fetch…"
if [ -n "$MODEL_BUCKET" ] && [ -n "$MODEL_PREFIX" ]; then
  mkdir -p /app/sarimax_models
  aws s3 sync "s3://$MODEL_BUCKET/$MODEL_PREFIX" /app/sarimax_models --no-progress
  ls -1 /app/sarimax_models
else
  echo "MODEL_BUCKET or MODEL_PREFIX not set; skipping S3 sync."
fi
