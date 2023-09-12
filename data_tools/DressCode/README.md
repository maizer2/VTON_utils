# DressCode data_tools

```DressCode_file_tree
-- dresses
|   |-- images
|   |   |-- 000000_0.jpg  # original
|   |   |-- 000000_1.jpg  # in-shop clothing
|   |   |-- 000001_0.jpg
|   |   |-- 000001_1.jpg
|   |   |-- ...
|   |-- ...
|-- lower_body
|   |-- images
|   |-- ...
`-- upper_body
|   |-- images
|   |-- ...
```

### make pairs_txt_files

```
python3 DressCode_pairs_txt.py --data_path "./data/DressCode" \
                               --train_ratio 0.6 \
                               --validation_ratio 0.2 \
                               --test_ratio 0.2
```
