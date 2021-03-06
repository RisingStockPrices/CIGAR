#!/bin/bash
python main.py \
    --warmup \
    --expr_name 'test' \
    —-batch_size 16 \
    --caption_directory '/home/deokhk/coursework/CIGAR/data/image_retrieval/generated_captions' \
    --caption_file_name 'train_short.json' \
    --data_root '/home/deokhk/coursework/' \
    --test_root '/home/deokhk/coursework/CIGAR/image_retrieval/retrieval_model/ours/train' \
    --target 'lower'