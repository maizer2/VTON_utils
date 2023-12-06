# VITON data_tools

```VITON_file_tree
-- VITON
|-- image
|   |-- 000000_0.jpg  # original
|   |-- 000001_0.jpg
|   |-- ...
|-- cloth
|   |-- 000000_1.jpg  # in-shop clothing
|   |-- 000001_1.jpg
|-- ...
```

### make pairs_txt_files

```
python3 DressCode_pairs_txt.py --data_path "./data/VITON" \
                               --train_ratio 0.6 \
                               --validation_ratio 0.2 \
                               --test_ratio 0.2
```
